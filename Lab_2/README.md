# Image Processing with OpenCV

This document provides an overview of basic image processing tasks using OpenCV in Python. The following steps are covered:
- Loading images from a file
- Displaying images in a window
- Saving images back to the file system

### Steps

1. **Loading Images**:
   - Use `cv2.imread()` to load the image.
   - Ensure the image is loaded successfully by checking if the image object is not `None`.

2. **Displaying Images**:
   - Use `cv2.imshow()` to display the image in a window.
   - Use `cv2.waitKey(0)` to wait indefinitely for a key press before closing the window.
   - Use `cv2.destroyAllWindows()` to close all OpenCV windows.

3. **Saving Images**:
   - Use `cv2.imwrite()` to save the image back to a file.

### Observations

- Make sure the image file (e.g., `Logo.jpg`) is in the same directory as your script, or provide the correct path.
- Implement error handling to ensure the program does not crash silently if the image is not found.

### Conclusion

This example demonstrates basic image processing operations such as loading, displaying, and saving images using OpenCV in Python. These steps form the foundation for more advanced image processing tasks.