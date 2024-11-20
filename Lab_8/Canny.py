import cv2

# Load an image
image = cv2.imread('flower.png', 0)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display result
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()