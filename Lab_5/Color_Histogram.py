import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in color mode
img_color = cv2.imread('Logo.jpg')

# Initialize colors for BGR channels
colors = ('b', 'g', 'r')

# Loop through each color channel (Blue, Green, Red)
for i, col in enumerate(colors):
    # Calculate the histogram for each channel
    hist = cv2.calcHist([img_color], [i], None, [256], [0, 256])

    # Plot the histogram for the current channel
    plt.plot(hist, color=col)

plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
