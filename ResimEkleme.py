#!/usr/bin/python
#-*- coding: utf-8 -*-
# -*- coding: cp1254 -*-
# coding: latin1
"""
Created on Tue Jun 25 15:05:28 2019

@author: Ogün Can KAYA
"""

# Yeni bir kayıt eklemek için yapılacak işlemler.
import cv2
import codecs
import sys
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
name = input(u"İsminizi girin: ")
#uniName=unicode(name,"utf-8")
while(True):

    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite("C:\\Users\\Ogun\\Desktop\\FaceRecognition\\known\\"+(name)+".jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()