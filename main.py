from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from ascii_converter import save_ascii_image
from colorama import Fore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['OUTPUT_FOLDER'] = 'static/output_files'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data

        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)
        
        output_file_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{secure_filename(file.filename)}.txt")
        save_ascii_image(file_path, output_file_path, text_colour=Fore.GREEN)

        return render_template('ascii.html', ascii_art=output_file_path, filename=f"{secure_filename(file.filename)}.txt")
    
    return render_template('index.html', form=form)

@app.route('/download/<filename>')
def download_ascii(filename):
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)



        

