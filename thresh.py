import cv2 as cv
import numpy as np
imgage = cv.imread('New folder\DSC_0310.jpg')
def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

img = rescaleFrame(imgage)
cv.imshow("Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)
#Simple Thresholds
Treshold, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

cv.imshow("Thresh1", thresh)

Treshold, thresh_inv = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)

cv.imshow("Thresh2", thresh_inv)
# Adaptive threshold
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Adaptive", adaptive_thresh)


cv.waitKey(0)