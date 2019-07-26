import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import time
from joblib import Parallel, delayed
import multiprocessing

#Adding allowed extention for photos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def process(img_path):

    encoding_file = img_path.replace("/train/", "/encode/")+".txt"

    if os.path.exists(encoding_file):
        print("encoding exists {}".format(img_path))
        return

    print("processing image {}".format(img_path))

    image = face_recognition.load_image_file(img_path)
    face_bounding_boxes = face_recognition.face_locations(image)
    #class_dir = img_path.split("/")[-2]

    if len(face_bounding_boxes) != 1:
        # If there are no people (or too many people) in a training image, skip the image.
        print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(face_bounding_boxes) < 1 else "Found more than one face"))
    else:
        # Add face encoding for current image to the training set
        fe = face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0]
        fullStr = ','.join([str(elem) for elem in fe ])
        f = open(encoding_file, 'w')
        f.write(fullStr)
        f.close()
    

#Setting train model method
#Trains a k-nearest neighbors classifier for face recognition
def encode(train_dir, verbose=True):
    # Loop through each person in the training set
    files = folders = 0

    f = open('celeba_encodings.txt', 'a')
    f.truncate(0)
    f.close()

    for _, dirnames, filenames in os.walk(train_dir):
        files += len(filenames)
        folders += len(dirnames)

    print("{:,} files, {:,} folders".format(files, folders))

    all_img_paths = []
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            if os.path.splitext(img_path)[1][1:] not in ALLOWED_EXTENSIONS:
                continue
            all_img_paths.append(img_path)

    num_cores = multiprocessing.cpu_count()
    Parallel(n_jobs=num_cores)(delayed(process)(img_path) for img_path in all_img_paths)

if __name__ == "__main__":
    print("Generating face encodings...")
    encode("./faces/train")
    print("Encoding complete!")