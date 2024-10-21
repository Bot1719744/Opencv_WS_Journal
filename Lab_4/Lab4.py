import cv2
import numpy as np

#Part1: Loading Images
img = cv2.imread('Logo.jpg')
gray_img = cv2.imread('Logo.jpg', cv2.IMREAD_GRAYSCALE)

# Harris Corner Detection
gray = np.float32(gray_img)
harris_corners = cv2.cornerHarris(gray, 5, 3, 0.04)

# Dilate the detected corners to enhance them
harris_corners = cv2.dilate(harris_corners, None)

# SIFT Detector
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray_img, None)

# Draw keypoints
image_with_keypoints = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Threshold for an optimal value
img[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

#Part2: Displaying Images
cv2.imshow('Harris Corners', img)
cv2.imshow('SIFT keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
