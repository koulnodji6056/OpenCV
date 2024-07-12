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

#average filter
average = cv.blur(img, (3,3))
cv.imshow("Average", average)
#Gaussian filter
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian", gaussian)
#median filter
median = cv.medianBlur(img, 5)
cv.imshow("Median", median)
#bilateral filter
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)