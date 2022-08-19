import cv2 as cv

img = cv.imread('god.jpg')

cv.imshow("photos/god", img)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4,height)


def rescaleFrame(frame, scale = 0.25):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions)


resiz = rescaleFrame(img)

cv.imshow('new', resiz)
cv.waitKey(0)
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    # new = changeRes(frame.shape[1], frame.shape[0])
    cv.imshow('video', frame)
    cv.imshow("resized", frame_resized)
    # cv.imshow('re', new)
    if cv.waitKey(50) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

