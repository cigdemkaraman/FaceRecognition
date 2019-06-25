# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:48:03 2019

@author: Ogün Can KAYA
"""

import face_recognition
# Bilinen resim ile bilinmeyen başka bir resimi karşılaştırır.
image_of_asli=face_recognition.load_image_file("known/aslienver.jpg")
asli_face_encoding=face_recognition.face_encodings(image_of_asli)[0]

unknown_image=face_recognition.load_image_file("bebek.jpg")
unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces(
        [asli_face_encoding], unknown_face_encoding)

if results[0]:
    print("ASLI")
else:
    print("ASLI Değil")