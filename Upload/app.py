from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      open_file = open(f.filename)
      read_lines = open_file.readlines()
      find_length = len(read_lines)
      return str(find_length)
		
if __name__ == '__main__':
   app.run(debug = True)