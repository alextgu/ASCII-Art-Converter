from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from ascii_converter import generate_ascii_art
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['OUTPUT_FOLDER'] = 'static/output_files'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

class UploadFileForm(FlaskForm):
    file = FileField("Upload Image:", validators=[InputRequired()])
    submit = SubmitField("Convert to ASCII")

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()

    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Convert the image to ASCII art
        ascii_art = generate_ascii_art(file_path)
        ascii_filename = f"{filename.split('.')[0]}.txt"  # Using the original filename without extension

        # Save ASCII art as a text file
        output_file_path = os.path.join(app.config['OUTPUT_FOLDER'], ascii_filename)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(ascii_art)

        # Redirect to the download page with the filename
        return redirect(url_for('download_page', filename=ascii_filename))

    return render_template('index.html', form=form)

@app.route('/download/<filename>')
def download_page(filename):
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    return send_file(filepath, as_attachment=True, download_name=filename, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
