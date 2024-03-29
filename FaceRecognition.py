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
import time
import numpy as np

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
video_capture=cv2.VideoCapture(0)
#cap.set(cv2.CV_CAP_PROP_FPS, 60)
#face_cascade=cv2.CascadeClassifier("C:\\Users\\Ogun\\Desktop\\Deep Learning\\haarcascade_frontalface_default.xml")

process_this_frame = True
while True:
   
    _,frame=video_capture.read()
    frame = cv2.flip(frame, 1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame,model="hog")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(image_face, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(image_face, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
#        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

#pil_image.save("identify.jpg")