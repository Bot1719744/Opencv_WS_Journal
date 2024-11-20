import cv2

# Load an image
image = cv2.imread('flower.png', 0)

# Apply Sobel filter
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3) # Horizontal edges
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3) # Vertical edges

# Combine Sobel X and Y
sobel_combined = cv2.sqrt(sobel_x**2 + sobel_y**2)

# Display result
cv2.imshow("Sobel Edge Detection", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()