from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

import os
import socket


app = Flask(__name__, template_folder='')
app.secret_key = '"super secret key'


@app.route('/')
def index():
    return redirect('/upload')


@app.route('/test')
def test():
    s = 'test'
    print(s)
    return(s)


@app.route('/upload')
def upload():
    return render_template('upload.html')


'''
reference
https://www.tutorialspoint.com/flask/flask_file_uploading.htm
https://www.roytuts.com/python-flask-multiple-files-upload-example/
secret key - https://stackoverflow.com/questions/26080872/secret-key-not-set-in-flask-session-using-the-flask-session-extension
'''
@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    print('uploader')
    if request.method == 'POST':
        # check if the post request has the files part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')

        s = ''
        for file in files:
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            s += '<p>' + filename + '</p>'
            print(filename)

        flash('File(s) successfully uploaded')
        return s


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)

