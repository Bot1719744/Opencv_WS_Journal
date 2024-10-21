import cv2
import numpy as np
import matplotlib.pyplot as plt


# Part 1: Loading Images
image = cv2.imread('scene.jpg')

# Apply averaging (box filter)
blurred_avg = cv2.blur(image, (5, 5))

# Apply Gaussian blur
blurred_gauss = cv2.GaussianBlur(image, (5, 5), 0)

# Apply median blur
blurred_median = cv2.medianBlur(image, 5)

# Apply bilateral filter
blurred_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Convert BGR to RGB for displaying using plt.imshow()
blurred_avg_rgb = cv2.cvtColor(blurred_avg, cv2.COLOR_BGR2RGB)
blurred_gauss_rgb = cv2.cvtColor(blurred_gauss, cv2.COLOR_BGR2RGB)
blurred_median_rgb = cv2.cvtColor(blurred_median, cv2.COLOR_BGR2RGB)
blurred_bilateral_rgb = cv2.cvtColor(blurred_bilateral, cv2.COLOR_BGR2RGB)

# Display the blurred images
plt.imshow(blurred_avg_rgb)
plt.title("Averaging (Box Filter)")
plt.axis('off')
plt.show()

plt.imshow(blurred_gauss_rgb)
plt.title("Gaussian Blurring")
plt.axis('off')
plt.show()

plt.imshow(blurred_median_rgb)
plt.title("Median Blurring")
plt.axis('off')
plt.show()

plt.imshow(blurred_bilateral_rgb)
plt.title("Bilateral Filtering")
plt.axis('off')
plt.show()
