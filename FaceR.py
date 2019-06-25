# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:13:39 2019

@author: Ogün Can KAYA
"""

import face_recognition
# Resim içerisinde kaç insan yüzü olduğunu algılıyor ve yazdırıyor.
image=face_recognition.load_image_file("test1.jpg")
face_locations=face_recognition.face_locations(image)
print(face_locations)
print("There are {} people in this image".format(len(face_locations)))