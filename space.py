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
""" YOU CAN ONLY CONVERT FROM GRAY SCAL TO BGR BEFORE HSV NO OTHERWAY """
#BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("L*a*b", lab)
#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
#HSB to BGR
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("BGR", bgr)

cv.imshow("Image", img)
cv.waitKey(0)