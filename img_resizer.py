import os
import cv2 
import numpy as np
from PIL import Image

###############################
## 1935 x 2400 e çeviriyor
###############################

images_path = "...denemeverisi"

filelist=os.listdir(images_path)
for filex in filelist:
    img_path = os.path.join(images_path,filex)

    image = Image.open(img_path)

    if image.mode == 'L':
        image = image.convert('RGB')

    width,height = image.size

    oran = 2400 / float(image.size[1]) 
    # print("oran",oran)
    if oran * width < 2808 :
        hedef_genişlik = int((float(image.size[0])*float(oran)))
        # print("hedef genişlik",hedef_genişlik)
        hedef_yukseklik = int((float(image.size[1])*float(oran)))
        # print("hedef yükseklik",hedef_yukseklik)

        new_image = image.resize((hedef_genişlik,hedef_yukseklik),Image.Resampling.LANCZOS)

        
        dif1 = int(float((2808 - hedef_genişlik) / 2))
        dif2 = 2808 - hedef_genişlik - dif1
        edgeLeft = np.zeros((hedef_yukseklik, dif1),np.uint8)
        edgeRight = np.zeros((hedef_yukseklik, dif2),np.uint8)
        new_width = np.concatenate((edgeLeft,new_image,edgeRight),axis=1)
        
        cv2.imwrite(img_path, new_width, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        
    else:
        oran = 1935 / float(image.size[0])


    if oran * height < 2400:
        hedef_genişlik = int((float(image.size[0])*float(oran)))
        # print("hedef genişlik",hedef_genişlik)
        hedef_yukseklik = int((float(image.size[1])*float(oran)))
        # print("hedef yükseklik",hedef_yukseklik)
        new_image = image.resize((hedef_genişlik,hedef_yukseklik),Image.ANTIALIAS)
        
        dif1 = int(float((2400 - hedef_yukseklik) / 2))
        dif2 = 2400 - hedef_yukseklik - dif1
        edgeUp = np.zeros((dif1,hedef_genişlik,3),np.uint8)
        edgeDown = np.zeros((dif2,hedef_genişlik,3),np.uint8)
        new_width = np.concatenate((edgeUp,new_image,edgeDown),axis=0)
        
        cv2.imwrite(img_path, new_width, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        
        print("completed",filex)
