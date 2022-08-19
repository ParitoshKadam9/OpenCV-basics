import cv2 as cv
import numpy as np

img = cv.imread('photos/ryuga.jpg')

cv.imshow("img", img)

#Transform image ----------------------------------
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 50)

cv.imshow("hero",translated)

#Rotations ----------------------------------------
def rotate(img, angle, rotationP=None):
    (height, width) = img.shape[:2]

    if rotationP is None:
        rotationP = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotationP, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("rot", rotated)

cv.waitKey(0)