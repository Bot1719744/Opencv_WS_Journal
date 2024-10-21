# Image Blurring Techniques with OpenCV and Matplotlib

This document provides an overview of different image blurring techniques using OpenCV and Matplotlib in Python. The following tasks are covered:
- Applying various blurring filters (Averaging, Gaussian, Median, Bilateral)
- Displaying the blurred images using Matplotlib

### Steps

1. **Loading Image**:
   - Use `cv2.imread()` to load the image in color mode.

2. **Applying Blurring Filters**:
   - **Averaging (Box Filter)**:
     - Use `cv2.blur()` to apply an averaging filter.
   - **Gaussian Blurring**:
     - Use `cv2.GaussianBlur()` to apply a Gaussian blur.
   - **Median Blurring**:
     - Use `cv2.medianBlur()` to apply a median blur.
   - **Bilateral Filtering**:
     - Use `cv2.bilateralFilter()` to apply a bilateral filter.

3. **Convert BGR to RGB**:
   - Use `cv2.cvtColor()` to convert the BGR images to RGB for correct color display with Matplotlib.

4. **Displaying Blurred Images**:
   - Use `plt.imshow()` to display the images in RGB mode.
   - Customize the plot with titles and hide the axis using `plt.title()` and `plt.axis('off')`.
   - Use `plt.show()` to display each image.

### Observations

- Ensure the image file (`scene.jpg`) is in the correct directory or provide the correct path.
- Different blurring techniques serve various purposes:
  - Averaging is simple but may not be as effective in preserving edges.
  - Gaussian blur uses a Gaussian kernel for smoother results.
  - Median blur is effective in removing salt-and-pepper noise.
  - Bilateral filter is useful for edge-preserving smoothing.

### Conclusion

This document demonstrates how to apply different blurring techniques using OpenCV and Matplotlib in Python. Blurring is a common preprocessing step in image processing that helps reduce noise and smooth an image. Each technique has its unique characteristics and use cases.