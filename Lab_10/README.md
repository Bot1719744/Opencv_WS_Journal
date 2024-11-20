# Optical Flow Detection with OpenCV

This document provides an overview of optical flow detection techniques using OpenCV in Python. The following tasks are covered:
- Setting up a camera for video capture.
- Applying Shi-Tomasi Corner Detection.
- Calculating Sparse Optical Flow using the Lucas-Kanade method.
- Calculating Dense Optical Flow using the Farneback method.
- Displaying the optical flow results.

### Steps

1. **Setting Up Camera**:
   - Use `cv2.VideoCapture(0)` to capture video from the primary camera (webcam).

2. **Shi-Tomasi Corner Detection**:
   - Define parameters and use `cv2.goodFeaturesToTrack()` to find points to track.
   
3. **Lucas-Kanade Optical Flow (Sparse)**:
   - Define parameters and use `cv2.calcOpticalFlowPyrLK()` to calculate the optical flow for sparse feature points.

4. **Dense Optical Flow**:
   - Use `cv2.calcOpticalFlowFarneback()` to calculate dense optical flow.
   
5. **Displaying Optical Flow Results**:
   - Display the results using `cv2.imshow()`.
   - Overlay the Lucas-Kanade tracks on the original frame.
   - Visualize the dense optical flow in HSV color space.

### Observations

- **Shi-Tomasi Corner Detection**:
  - Detects good features (corners) in the first frame to track over subsequent frames.
- **Lucas-Kanade Optical Flow (Sparse)**:
  - Tracks the movement of detected feature points over time.
  - Suitable for tracking fewer points and provides a clear visual of point movement.
- **Dense Optical Flow (Farneback)**:
  - Calculates dense optical flow, providing motion information for every pixel.
  - Visualized in HSV color space where hue represents direction and value represents magnitude.

### Conclusion

This document demonstrates how to perform optical flow detection using OpenCV in Python. Optical flow detection is crucial in tracking the motion of objects or points across frames in a video sequence. The Lucas-Kanade method provides sparse optical flow, ideal for tracking specific points, while the Farneback method provides dense optical flow, useful for a holistic view of motion across the entire frame.