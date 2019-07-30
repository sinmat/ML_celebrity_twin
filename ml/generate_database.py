import math
import os
import os.path
from face_recognition.face_recognition_cli import image_files_in_folder
import time
from tinydb import TinyDB, Query

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
db = TinyDB('db.json')

def create_records(train_dir, verbose=True):
    files = folders = 0
    files_i = folders_i = 0

    f = open('db.json', 'a')
    f.truncate(0)
    f.close()

    for _, dirnames, filenames in os.walk(train_dir):
        files += len(filenames)
        folders += len(dirnames)

    print("{:,} files, {:,} folders".format(files, folders))
    
    all_images = []
    for class_dir in os.listdir(train_dir):
        folders_i += 1
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            files_i += 1
            if os.path.splitext(img_path)[1][1:] not in ALLOWED_EXTENSIONS:
                continue

            encoding_file = img_path.replace("/train/", "/encode/")+".txt"
            if os.path.exists(encoding_file):
                all_images.append({'id': img_path.split("/")[-2], 'image': img_path.split("/")[-1]})

        print("{:,}/{:,} folders {:,}/{:,} files".format(folders_i, folders, files_i, files))

    db.insert_multiple(all_images)        

if __name__ == "__main__":
    print("Generating database...")
    create_records("./faces/train")
    print("Complete!")