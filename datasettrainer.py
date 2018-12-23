

import cv2
import numpy as np
import os

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
Video = cv2.VideoCapture(0)

print("Now you are creating a data set")
folder=input("Enter your Name").capitalize()
path="E:\\Project\\"
os.chdir("E:\Project")
print("enter ur id")
id = input()



# define the name of the directory to be created
try:  
    os.mkdir(folder)
    path=path+str(folder)
 
    os.chdir(path)
except OSError:  
    print ("Creation of the directory  failed")
else:  
    print ("Successfully created the directory ")

global sample

sample=0


print("IN")

while True:
    check,frame=Video.read()
    faces=face_cascade.detectMultiScale(frame,scaleFactor=3.0)
    for (x,y,w,h) in faces:
      
        sample=sample+1
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        op=frame[y:y+h,x:x+w]
        cv2.imwrite(str(folder)+" " + str(id) + " " + str(sample) +  ".jpg",op)
        print("THE VALUE IS",sample)
        cv2.imshow('Captures',frame)
    if(sample==500):
        break
    key=cv2.waitKey(1)
    #if key == ord('q'):
     #  break

Video.release() 
cv2.destroyAllWindows()
for i in os.listdir(path):
    print(i)
