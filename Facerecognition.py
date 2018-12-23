import cv2
import numpy as np
from threading import *
import playsound
import time


ct=0
blinks=0


def Level2():
    playsound.playsound("beep.wav")

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('MyTraining.yml')
Video = cv2.VideoCapture(0)
time.sleep(3)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))



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
        if count==10:
            print("You are distracted at time",time.ctime())  
            count=0
            ct=0
            p = Thread(target = Level2)
            p.start()

def face(faces):
    dimension=len(faces)
    if (dimension!=0):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            #roi_color=frame[y:y+h,x:x+w]
            id,confidence = recognizer.predict(grey_img[y:y+h,x:x+w])
            print('id is',id)
            print("confidance is",confidence)
            if id == 501 and confidence >30 and confidence <150:
                cv2.putText(frame, 'Shanmukh',(x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,127,255), 1, cv2.LINE_AA)
            if id == 100:
                cv2.putText(frame, 'Obama',(x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
            eye(eyes)
          
    else:
        pass

            
while True:
    check,frame=Video.read()
    grey_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=eye_cascade.detectMultiScale(frame,1.3,5)
    faces=face_cascade.detectMultiScale(frame)
    face(faces)
    cv2.imshow('Captures',frame)
    out.write(frame)
    key=cv2.waitKey(2)
    if key == ord('q'):
        break
    
Video.release()
out.release()
cv2.destroyAllWindows()
