import cv2
import numpy as np


#Part1: Loading Images
img = cv2.imread('Logo.jpg')
gray_img = cv2.imread('Logo.jpg', cv2.IMREAD_GRAYSCALE)


#Part2: Displaying Images
cv2.imshow('logo image', img)
cv2.imshow('logo gray image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Part3: Saving Images
cv2.imwrite('lab_2_image.jpg', img)
