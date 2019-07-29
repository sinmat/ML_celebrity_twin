import json
import os
from flask import Flask,url_for,request,render_template,jsonify,send_file
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
	return render_template('index.js')

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



#     # Call KNN predict method

    
#     # Assign data to result_dict
#     result_dict['hello'] = "world!"  


#     # Remove tmp image to preserve space
    
#     # Encode result_dict as JSON and return back to user
#     return jsonify(result_dict)

# ## Define KNN predict model function that takes in image as parameter and 
# @app.route('/predict',methods=['GET','POST'])

# ## returns back relevant data as dict
# def knn_predict(img_path = ""):
#     result_dict = {}

#     # Run prediction
    
#     # Assign data to result_dict
#     result_dict['predict'] = "world!" 

#     return result_dict

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)