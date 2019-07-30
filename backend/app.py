#Importing dependencies
import sys
import math
from sklearn import neighbors
import pickle
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import json
import os
import os.path
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask.ext.sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/ml_celebrity_twin'
db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS 

@app.route('/')
def index():
    result_dict = {}
    result_dict['hello'] = "world!" 
    return result_dict

# POST image and return a match JSON dict
@app.route('/match',methods=['GET','POST'])
def match():     
    result_dict = {}

    if request.method == 'POST':
        # read the file
        file = request.files['file']

        # Save the file to the uploads folder
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result_dict["file_location"] = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
            result_dict["file_name"] = filename 
        else:
            result_dict["error"] = "No image uploaded"
   
    # Call KNN predict method
    knn = knn_predict(img_path=result_dict["file_location"], model_path="./models/trained_knn_model.clf")

    if 'error' in knn:
        return knn["error"]

    result_dict["knn"] = knn    


#     # Remove tmp image to preserve space
    
    return result_dict

## Define KNN predict model function that takes in image as parameter and 
## returns back relevant data as dict
def knn_predict(img_path=None, model_path=None):
    response = {}
    
    if not os.path.isfile(img_path):
        response["error"] = "Invalid image path: {}".format(img_path) 
        return response

    if model_path is None:
        response["error"] = "Must supply knn classifier with model_path" 
        return response

    # Load a trained KNN model (if one was passed in)
    with open(model_path, 'rb') as f:
        knn_clf = pickle.load(f)

    # Load image file and find face locations
    X_img = face_recognition.load_image_file(img_path)
    X_face_locations = face_recognition.face_locations(X_img)

    # If no faces are found in the image, return an empty result.
    if len(X_face_locations) == 0:
        response["error"] = "Couldn't find a face in the image"
        return response

    # Find encodings for faces in the test image
    faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    # Use the KNN model to find the best matches for the face
    are_matches = []
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)    
    for i in range(len(X_face_locations)):
        are_matches.append(closest_distances[0][i])

    response["matches"] = []
    for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches):
        if rec:
            response["matches"].append({
                "match": pred,
                "location": loc,
                "distance": rec[0],
            })
        else:
            response["matches"].append({
                "match": "unknown",
                "location": loc,
                "distance": rec[0],
            })

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)