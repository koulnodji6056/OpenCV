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
cv.imshow("Gray", gray)
#LaplaceLan

lap = cv.Laplacian(img, cv.CV_64F)

lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian", lap)

#Sobel
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel", combined_sobel)

cv.imshow("Image", img)

cv.waitKey(0)