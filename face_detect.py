import cv2 as cv
import numpy as np
#img = cv.imread('lady.jpg')
img = cv.imread('group 1.jpg')
gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml') 

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')
#Draw the rectangle 
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=5)

cv.imshow('Detected Faces', img)

cv.waitKey(0)