import cv2 as cv
import numpy as np
#Blank imgae test
blank= np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blank', blank)
# img = cv.imread('New folder\DSC_0310.jpg')
# cv.imshow('My-image',img)

#paint the image a certain color
#for a certain raNGE
# blank[200:300, 300:400] = 0,255,0 

# #for a full pixel
# blank[:] = 0,255,0
# cv.imshow('green', blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=cv.FILLED) 
# from origin 0,0 to 250,250 with color and thickness and cv.FILLED or -1 will fill the rectangle
cv.imshow('Rectangle', blank)

#draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)
#draw a line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow('Line', blank)
#write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)