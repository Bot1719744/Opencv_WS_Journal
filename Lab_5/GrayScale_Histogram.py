import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale mode
img_gray = cv2.imread('Logo.jpg', 0)

# Calculate the Histogram
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

# Plot the grayscale histogram
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()