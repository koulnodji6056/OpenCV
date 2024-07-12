import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
imgage = cv.imread('New folder\DSC_0310.jpg')
""" THE BELOW FUNCTION IS THERE BECAUSE MY IMAGE SIZE WAS TOO BIGGER THAN THE SIZE SUPPORTED BY MY LOCAL SCREEN  SO YOU CAN SKIP IT"""
def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

img = rescaleFrame(imgage)
cv.imshow("Image", img)
blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)
cv.waitKey(0)
