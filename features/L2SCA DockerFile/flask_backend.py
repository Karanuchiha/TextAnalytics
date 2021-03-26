from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/l2sca', methods=['POST'])
@cross_origin()
def l2sca():
    data = json.loads(request.data)
    text = data['text']
    text = text.replace('"', '\'')

    os.system('echo "' + text + '" > input_file.txt')
    os.system('python2.7 analyzeText.py input_file.txt output_file.txt')

    f = open('output_file.txt', 'r')
    processing_result = f.read()

    return jsonify({"response": processing_result})

if __name__ == '__main__':
    app.run(debug=True, port=1234, host='0.0.0.0')