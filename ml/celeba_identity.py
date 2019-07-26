import os
from shutil import copyfile

file = open("identity_CelebA.txt", "r") 
for line in file:
    l = line.rstrip().split(' ')
    folder_name = "./train/"+l[1]
    if os.path.isdir(folder_name):
        print("exist")
    else:
        print('creating folder')
        os.makedirs(folder_name)

    image_name = "./img_align_celeba/"+l[0]
    image_name_new = './train/'+l[1]+'/'+l[0]
    os.rename(image_name, image_name_new)