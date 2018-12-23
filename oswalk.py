import os
from PIL import Image
import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
current=0
label=''
facee=[]
ids=[]
for root, dirs, files in os.walk("E:\\Project"):
    for name in dirs:
        os.path.join(root, name)
        print("Hi")
    for name in files:
        path=os.path.join(root, name)
        label=os.path.basename(path)
        label=label.split(' ')
        print(label)
        label=label[1]
        label=label.split('.')
        label=label[0]
        print(label)
        label=int(label)
        pile=Image.open(path).convert("L")#converts into gray scale
        img_array=np.array(pile)
        print(img_array)
        facee.append(img_array)
        ids.append(label)
id_=np.array(ids)
recognizer.train(facee,id_)
recognizer.write("MyTraining.yml")

            
            
