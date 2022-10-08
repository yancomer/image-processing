import numpy as np
from PIL import Image
import os

all_img_path = "...\\separeteclasses"
new_path = "...\\newfolder"
file_list = os.listdir(all_img_path)
count = 0

for file in file_list:
    file_name = os.path.join(all_img_path,file)
    im1 = Image.open(file_name)

    arr = np.array(im1)
    cond = arr==63
    new_arr = np.where(cond, 255, 0)
    out = Image.fromarray(np.uint8(new_arr), 'L')
    new_img_path = os.path.join(new_path,str(count)+".jpg")
    image1 = out.save(new_img_path)
    count += 1

    file_name = os.path.join(all_img_path,file)
    im1 = Image.open(file_name)

    arr = np.array(im1)
    cond = arr==189
    new_arr = np.where(cond, 255, 0)
    out = Image.fromarray(np.uint8(new_arr), 'L')
    new_img_path = os.path.join(new_path,str(count)+".jpg")
    image2 = out.save(new_img_path)
    count += 1 

    file_name = os.path.join(all_img_path,file)
    im1 = Image.open(file_name)

    arr = np.array(im1)
    cond = arr==252
    new_arr = np.where(cond, 255, 0)
    out = Image.fromarray(np.uint8(new_arr), 'L')
    new_img_path = os.path.join(new_path,str(count)+".jpg")
    image2 = out.save(new_img_path)
    count += 1 

    file_name = os.path.join(all_img_path,file)
    im1 = Image.open(file_name)

    arr = np.array(im1)
    cond = arr==126
    new_arr = np.where(cond, 255, 0)
    out = Image.fromarray(np.uint8(new_arr), 'L')
    new_img_path = os.path.join(new_path,str(count)+".jpg")
    image2 = out.save(new_img_path)
    count += 1 