import cv2 as cv
#read image
img = cv.imread('New folder\DSC_0310.jpg')
# cv.imshow('my', img)

#rescale function could work for video image, live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#resized image
# resized_image = rescaleFrame(img)
# cv.imshow('image', resized_image) 
# #only for videos
#read video with resize and no resize

# def changeRes(width,height):
#     #live video only
#     capture.set(3,width)
#     capture.set(4,height)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resize', frame_resize)
    # from_resize2 = changeRes(frame)

    # cv.imshow('Video', from_resize2)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()