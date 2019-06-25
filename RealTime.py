# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:55:29 2019

@author: Ogün Can KAYA
"""
# Gerçek zamanlı olarak ekranda gözüken kişiyi verilerin içerisinden tanımaya çalışır.
import face_recognition
from PIL import Image, ImageDraw
import os
import cv2

# %%
path="C:\\Users\\Ogun\\Desktop\\FaceRecognition\\known"
known_face=[]
image_face=[]
for files in os.listdir(path):
    if files.endswith(".jpg"):
        known_face.append(files.split('.jpg')[0])
        image=face_recognition.load_image_file(path+"\\"+files)
        image_face_encoding=face_recognition.face_encodings(image)[0]
        image_face.append(image_face_encoding)
    elif files.endswith(".png"):
        known_face.append(files.split(".png")[0])
        image=face_recognition.load_image_file(path+"\\"+files)
        image_face_encoding=face_recognition.face_encodings(image)[0]
        image_face.append(image_face_encoding)

# %%
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face_locations=face_recognition.face_locations(frame)
    face_encodings=face_recognition.face_encodings(frame,face_locations)
    pil_image=Image.fromarray(frame)
    draw=ImageDraw.Draw(pil_image)
    for (top, right, bottom, left), face_encoding in zip(face_locations,face_encodings):
        matches= face_recognition.compare_faces(image_face,face_encoding)
        name="Unknown Person"
       
        if True in matches:
            first_match_index=matches.index(True)
            name=known_face[first_match_index]
        
#        draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))
        cv2.rectangle(frame,(left,top),(right,bottom),(255,0,0),2)
        text_width,text_height=draw.textsize(name)
#        cv2.rectangle(frame,(left,bottom-text_height),(right,bottom+5), (0,0,0),1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,name,(left+6 , bottom-text_height),font,0.8,(255,255,255),2,cv2.LINE_AA)   
    
    cv2.imshow('img',frame)
    if cv2.waitKey(1)==27:
        break
#    pil_image.show()
del draw
cap.release()
cv2.destroyAllWindows()
#pil_image.save("identify.jpg")