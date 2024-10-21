# Image Processing with OpenCV

This document provides an overview of basic image processing tasks using OpenCV in Python. The following steps are covered:
- Loading and converting images
- Resizing, cropping, and rotating images
- Drawing shapes and text on images

### Steps

1. **Loading and Converting Images**:
   - Use `cv2.imread()` to load the image.
   - Convert the loaded image to grayscale and HSV color space using `cv2.cvtColor()`.

2. **Resizing Image**:
   - Use `cv2.resize()` to resize the image to specified dimensions.

3. **Cropping Image**:
   - Crop the image using array slicing.

4. **Rotating Image**:
   - Use `cv2.rotate()` to rotate the image by 90 degrees clockwise.

5. **Drawing Shapes and Text**:
   - Draw a rectangle using `cv2.rectangle()`.
   - Draw a circle using `cv2.circle()`.
   - Put text on the image using `cv2.putText()`.
   - Draw a line using `cv2.line()`.

6. **Displaying Image**:
   - Use `cv2.imshow()` to display the image.
   - Use `cv2.waitKey(0)` to wait indefinitely for a key press before closing the window.
   - Use `cv2.destroyAllWindows()` to close all OpenCV windows.

### Observations

- Make sure the image file (e.g., `Logo.jpg`) is in the same directory as your script, or provide the correct path.
- Conversion to different color spaces allows for various image processing techniques.
- Resizing, cropping, and rotating images are basic operations that can be customized as needed.
- Drawing functions can be used to annotate and highlight parts of an image.

### Conclusion

This example demonstrates more advanced image processing operations including loading, converting, resizing, cropping, rotating, and drawing on images using OpenCV in Python. These steps enable a wide range of image manipulation and annotation tasks.