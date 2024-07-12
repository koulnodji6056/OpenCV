import cv2 as cv

imgage = cv.imread('New folder\DSC_0310.jpg')
def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

img = rescaleFrame(imgage)

cv.imshow("Image", img)
# #converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)
# #blur
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)
# #edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)
# #Dillating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("Dilated", dilated)
#Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", eroded)
#converting to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)
#cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)