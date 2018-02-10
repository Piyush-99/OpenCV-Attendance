#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:18:48 2018

@author: piyush
"""

import cv2
import os

root = os.path.dirname(os.path.realpath('__file__'))
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read( os.path.join( root, "trained_data.yml"))
subjects = ["Salman Khan", "Shahrukh Khan","Akshay Kumar"]

def predict(test_img):
    img = test_img.copy()
    label, confidence = face_recognizer.predict(img)
    label_text = subjects[label]
    print(confidence)
    print(label_text, "Present")

img_path = os.listdir("cropped_files")
for image in img_path:
    img = cv2.imread(os.path.join(root,"cropped_files",image))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    print(image)
    predict(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
