import cv2
import numpy as np

#Part1: Loading Images
img = cv2.imread('Logo.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#Part2: Resizing Image
resized_img = cv2.resize(img, (500, 500))

cropped_img = img[80:230, 150:330]

rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.rectangle (resized_img, (0, 0), (250, 250), (0, 0, 0), 10)
cv2.circle (resized_img, (250, 250), 30, (0, 0, 0), 10)
cv2.putText(resized_img, "Lab2", (250, 250), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 10)
line_img = cv2.line(resized_img, (250, 250), (5000, 5000), (0, 0, 0), 20)

cv2.imshow("Line Image", line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
