import json
import os
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../ml/faces/train'
ALLOWED_EXTENSIONS = set(['txt','jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route('/')
def index():
    return 'Hello World!!!'

# POST image and return a match JSON dict
@app.route('/match',methods=['GET','POST'])
def match():     
    if request.method == 'POST':
        print(request)

        if request.files.get('file'):
            # read the file
            file = request.files['file']

            # read the filename
            filename = file.filename

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Image Saved!"

   
    # Save image to /tmp and assign it's path to a variable

    # Call KNN predict method
    
    # Assign data to result_dict
    result_dict['hello'] = "world!"  

    #* Call SVM predict method
    #* Assign data to result_dict

    # Remove tmp image to preserve space
    
    # Encode result_dict as JSON and return back to user
    return jsonify(result_dict)

## Define KNN predict model function that takes in image as parameter and 
## returns back relevant data as dict
def knn_predict(img_path = ""):
    result_dict = {}

    # Run prediction
    
    # Assign data to result_dict
    result_dict['hello'] = "world!" 

    return result_dict

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)