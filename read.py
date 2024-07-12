import cv2 as cv
#read image

#img = cv.imread('New folder\DSC_0310.jpg')
#cv.imshow('my', img)
#cv.waitKey(0)
#read video
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
