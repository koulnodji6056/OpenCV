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
# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(img, contours, -1, (0,255,0), 2)
cv.imshow("Contours", img)
cv.waitKey(0)
