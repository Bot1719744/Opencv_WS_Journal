# Image Thresholding Techniques with OpenCV and Matplotlib

This document provides an overview of different image thresholding techniques using OpenCV and Matplotlib in Python. The following tasks are covered:
- Applying various thresholding techniques (Simple, Adaptive Mean, Adaptive Gaussian, Otsu’s Binarization)
- Displaying the thresholded images using Matplotlib

### Steps

1. **Loading Image**:
   - Use `cv2.imread()` to load the image in grayscale mode.

2. **Applying Thresholding Techniques**:
   - **Simple Thresholding**:
     - Use `cv2.threshold()` with `cv2.THRESH_BINARY` to apply simple thresholding.
   - **Adaptive Mean Thresholding**:
     - Use `cv2.adaptiveThreshold()` with `cv2.ADAPTIVE_THRESH_MEAN_C` to apply adaptive mean thresholding.
   - **Adaptive Gaussian Thresholding**:
     - Use `cv2.adaptiveThreshold()` with `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` to apply adaptive Gaussian thresholding.
   - **Otsu’s Binarization**:
     - Use `cv2.threshold()` with `cv2.THRESH_BINARY + cv2.THRESH_OTSU` to apply Otsu’s binarization.

3. **Displaying Thresholded Images**:
   - Use `plt.imshow()` to display the images in grayscale mode.
   - Use `plt.title()` to add titles to the plots.
   - Use `plt.subplot()` to create subplots for displaying multiple images in a single figure.
   - Use `plt.show()` to display each image or set of images.

### Observations

- Ensure the image file (`scene.jpg`) is in the correct directory or provide the correct path.
- Different thresholding techniques serve various purposes:
  - Simple thresholding is straightforward but may not work well for varying lighting conditions.
  - Adaptive mean and Gaussian thresholding can handle varying lighting by calculating the threshold for small regions.
  - Otsu’s binarization automatically calculates an optimal threshold value based on image histogram.

### Conclusion

This document demonstrates how to apply different thresholding techniques using OpenCV and Matplotlib in Python. Thresholding is a fundamental technique in image processing that converts grayscale images into binary images, which are easier to analyze for object detection and other tasks. Each technique has its unique advantages and use cases.