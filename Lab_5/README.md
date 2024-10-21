# Histogram Analysis with OpenCV and Matplotlib

This document provides an overview of histogram analysis tasks using OpenCV and Matplotlib in Python. The following tasks are covered:
- Calculating and plotting color histograms
- Calculating and plotting grayscale histograms

### Color Histogram

#### Steps
1. **Loading Image**:
   - Use `cv2.imread()` to load the image in color mode.

2. **Initialize Colors for BGR Channels**:
   - Define colors for Blue, Green, and Red channels.

3. **Calculate and Plot Histograms**:
   - Use `cv2.calcHist()` to calculate the histogram for each color channel.
   - Use `plt.plot()` to plot the histogram for each channel.
   - Customize the plot with titles and labels (Pixel Intensity, Frequency).
   - Display the plot with `plt.show()`.

### Grayscale Histogram

#### Steps
1. **Loading Image**:
   - Use `cv2.imread()` to load the image in grayscale mode.

2. **Calculate and Plot Histogram**:
   - Use `cv2.calcHist()` to calculate the histogram for the grayscale image.
   - Use `plt.plot()` to plot the histogram.
   - Customize the plot with titles and labels (Pixel Intensity, Frequency).
   - Display the plot with `plt.show()`.

### Observations

- Ensure the image file (`Logo.jpg`) is in the correct directory or provide the correct path.
- Color histograms are useful for examining the distribution of pixel intensities in different color channels.
- Grayscale histograms help in understanding the overall intensity distribution of an image.

### Conclusion

This document demonstrates how to calculate and plot color and grayscale histograms using OpenCV and Matplotlib in Python. Histogram analysis is a fundamental technique for understanding the distribution of pixel intensities in an image, which is crucial for various image processing tasks.