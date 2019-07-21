import json

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello World!!!'

@app.route('/data')
def data():
    result_dict = {}
    result_dict['result'] = "Hello World!"  
    return jsonify(result_dict)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)