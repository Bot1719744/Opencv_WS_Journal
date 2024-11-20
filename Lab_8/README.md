# Edge Detection Techniques with OpenCV

This document provides an overview of different edge detection techniques using OpenCV in Python. The following tasks are covered:
- Applying Canny edge detection
- Applying Sobel edge detection
- Displaying the edge-detected images

### Steps

1. **Loading Image**:
   - Use `cv2.imread()` to load the image in grayscale mode.

2. **Applying Edge Detection Techniques**:
   - **Canny Edge Detection**:
     - Use `cv2.Canny()` to apply Canny edge detection.
   - **Sobel Edge Detection**:
     - Use `cv2.Sobel()` to detect horizontal edges.
     - Use `cv2.Sobel()` to detect vertical edges.
     - Combine the results using the Euclidean distance formula.

3. **Displaying Edge-Detected Images**:
   - Use `cv2.imshow()` to display the images.
   - Use `cv2.waitKey(0)` to hold the display window.
   - Use `cv2.destroyAllWindows()` to close the display window.


### Observations

- Ensure the image file (`flower.png`) is in the correct directory or provide the correct path.
- Different edge detection techniques serve various purposes:
  - **Canny Edge Detection**: Provides clear and thin edges, suitable for detecting fine details.
  - **Sobel Edge Detection**: Detects horizontal and vertical edges separately and allows for more control over edge thickness with the kernel size.
  - Combining Sobel X and Y results provides a comprehensive edge map of the image.

### Conclusion

This document demonstrates how to apply different edge detection techniques using OpenCV in Python. Edge detection is crucial in image processing for identifying object boundaries and features. Each technique has its unique advantages and use cases:
- Canny edge detection is excellent for fine detail detection.
- Sobel edge detection is advantageous when requiring control over edge direction and thickness.