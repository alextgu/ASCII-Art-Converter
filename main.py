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

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class UploadFileForm(FlaskForm):
    file = FileField("Upload Image", validators=[InputRequired()])
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

        ascii_file = io.BytesIO()
        ascii_file.write(ascii_art.encode('utf-8'))
        ascii_file.seek(0)

        return redirect(url_for('download_page', filename=filename))

    return render_template('index.html', form=form)

@app.route('/download/<filename>')
def download_page(filename):
    # Generate ASCII art file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    ascii_art = generate_ascii_art(file_path)

    # Create an in-memory file to be downloaded
    ascii_file = io.BytesIO()
    ascii_file.write(ascii_art.encode('utf-8'))
    ascii_file.seek(0)

    return send_file(
        ascii_file,
        as_attachment=True,
        download_name=f"{filename}.txt",
        mimetype="text/plain"
    )

if __name__ == '__main__':
    app.run(debug=True)
