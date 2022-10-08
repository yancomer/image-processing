import numpy as np
from PIL import Image
import os

all_img_path = "...\\separeteclasses"
new_path = "...\newfolder"
file_list = os.listdir(all_img_path)
count = 0

def bbox2(img):
    rows = np.any(img, axis=1)
    cols = np.any(img, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    print( rmin, rmax, cmin, cmax)

for file in file_list:
    file_name = os.path.join(all_img_path,file)
    im1 = Image.open(file_name)

    arr = np.array(im1)
    cond = arr==127
    new_arr = np.where(cond, 255, 0)
    out = Image.fromarray(np.uint8(new_arr), 'L')
    new_img_path = os.path.join(new_path,str(count)+".jpg")
    image1 = out.save(new_img_path)
    count += 1

    file_name = os.path.join(all_img_path,file)
    im1 = Image.open(file_name)

    arr = np.array(im1)
    cond = arr==254
    new_arr = np.where(cond, 255, 0)
    out = Image.fromarray(np.uint8(new_arr), 'L')
    new_img_path = os.path.join(new_path,str(count)+".jpg")
    image2 = out.save(new_img_path)
    count += 1  

file_list2 = os.listdir(new_path) 
for file in file_list2:
    file_name = os.path.join(new_path,file)
    im1 = Image.open(file_name)
    print(file_name)
    bbox2(im1)