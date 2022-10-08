# Improting Image class from PIL module
from PIL import Image
import matplotlib.pyplot as plt
import os


# Opens a image in RGB mode
all_img_path = "...\\datasonhali"

filelist=os.listdir(all_img_path)

for filex in filelist:

    img_path = os.path.join(all_img_path,filex)

    im = Image.open(img_path)

    # Setting the points for cropped image  
 

    # Cropped image of above dimension
    # (It will not change orginal image)
    im1 = im.crop((516, 320, 1935, 2080))#left top right bottom

    newsize = (1935, 2400)
    im1 = im1.resize(newsize)

    
    img_no = int(filex.split('.')[0])
    new_img_no = 1000 + img_no
    new_img_path = os.path.join(all_img_path,str(new_img_no)+".jpg")

    im1 = im1.save(new_img_path)
    print("completed",str(new_img_no))
