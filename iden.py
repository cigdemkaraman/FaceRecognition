# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:55:29 2019

@author: Ogün Can KAYA
"""
# Test olarak verilen resimi, verilerin içerisinden bulmaya çalışır ve ekranda gösterir.
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

# %%
test_image=face_recognition.load_image_file("test0.jpg")
face_locations=face_recognition.face_locations(test_image)
face_encodings=face_recognition.face_encodings(test_image,face_locations)

pil_image=Image.fromarray(test_image)

draw=ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations,face_encodings):
    matches= face_recognition.compare_faces(image_face,face_encoding)
    name="Unknown Person"
    
    if True in matches:
        first_match_index=matches.index(True)
        name=known_face[first_match_index]
    
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))
    
    text_width,text_height=draw.textsize(name)
    draw.rectangle(((left,bottom-text_height),(right,bottom+5)), fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6 , bottom-text_height),name,fil=(255,255,255,255))
#del draw
pil_image.show()
pil_image.save("identify.jpg")