import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import time
import numpy as np 

#Adding allowed extention for photos
ALLOWED_EXTENSIONS = {'txt'}

#Setting train model method
#Trains a k-nearest neighbors classifier for face recognition
def train(train_dir="./faces/encode", model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=True):
    X = []
    y = []

    all_encodings_paths = []
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        for encoding_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            if os.path.splitext(encoding_path)[1][1:] not in ALLOWED_EXTENSIONS:
                continue

            all_encodings_paths.append(encoding_path)
            file = open(encoding_path, "r") 
            d = encoding_path.split("/")[-2]
            dx = np.array(file.read().split(",")).astype(np.float64)
            X.append(dx)
            y.append(d)
            file.close()

    print(len(all_encodings_paths))

    # Create and train the KNN classifier
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    # Save the trained KNN classifier
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


if __name__ == "__main__":
    print("Training KNN classifier...")
    classifier = train("./faces/encode", model_save_path="trained_knn_model.clf", n_neighbors=3)
    print("Training complete!")