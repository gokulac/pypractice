import csv
import codecs
from flask import Flask, jsonify, request

# ...
app = Flask(__name__)

@app.route('/', methods=['POST'])
def myroute():
    flask_file = request.files['file']
    if not flask_file:
        return 'Upload a CSV file'
    
    data = []
    stream = codecs.iterdecode(flask_file.stream, 'utf-8')
    for row in csv.reader(stream, dialect=csv.excel):
        if row:
            data.append(row)
            
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)