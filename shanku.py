import cv2
import numpy as np
from threading import *
import playsound
import time


ct=0
blinks=0


def Level2():
    playsound.playsound("Beep.wav")

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
Video = cv2.VideoCapture(0)
time.sleep(3)

def eye(eyes):
    global ct,blinks
    dimensions=len(eyes)
    if(dimensions!=0):
        for (a,b,c,d) in eyes:
            cv2.rectangle(frame,(a,b),(a+c,b+d),(0,127,255),2)
            ct=0
            
    else:
        count= ct
        count=count+1
        ct=count
        blinks=blinks+1
        print("The total number of blinks",blinks)
        if count==5:
            print("You are distracted at time",time.ctime())  
            count=0
            ct=0
            p = Thread(target = Level2)
            p.start()

def face(faces):
    dimension=len(faces)
    if (dimension!=0):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            eye(eyes)
    else:
        pass

            
while True:
    check,frame=Video.read()
    eyes=eye_cascade.detectMultiScale(frame,1.3,5)

    faces=face_cascade.detectMultiScale(frame)
    face(faces)
    cv2.imshow('Captures',frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
Video.release() 
cv2.destroyAllWindows()
