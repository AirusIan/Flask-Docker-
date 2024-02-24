from flask import Flask,request
from flask import render_template
import os
app = Flask(__name__)

UPLOAD_FOLDER = '/app'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.get('/')
def upload():
    return render_template('123.html')

@app.post('/view')
def view():
 
    # Read the File using Flask request
    file = request.files['file']
    # save file in local directory
    #file.save(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return file.filename
 
 
# Main Driver Function
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8070)