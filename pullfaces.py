# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:53:22 2019

@author: Ogün Can KAYA
"""

import face_recognition
from PIL import Image
# Resim içerisinde bulunan yüzü ekranda gösterir.
image=face_recognition.load_image_file("test0.jpg")
face_locations=face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image=image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()