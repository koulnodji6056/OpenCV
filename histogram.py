import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
imgage = cv.imread('New folder\DSC_0310.jpg')
def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

img = rescaleFrame(imgage)
cv.imshow("Image", img)
#Dimension of the mask has to be the same as the imgage
blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow("Gray", gray)
# rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2,), 100, 255, -1)
# cv.imshow('Circle', circle)

mask = cv.bitwise_and(img, img, mask=circle)

cv.imshow('Masked', mask)
#GRayscale histogram
#gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscal Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#Color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)