# Adversarial Image Generation and GAN Training

This document provides an overview of adversarial image generation techniques and GAN training using PyTorch and OpenCV in Python. The following tasks are covered:
- Creating adversarial images by adding noise.
- Defining and training a Generative Adversarial Network (GAN).
- Gradually adding Gaussian noise to images and denoising them.

## Adversarial Image Generation

### Steps

1. **Adversarial Image Creation**:
   - Load the original image using `cv2.imread('flower.png', cv2.IMREAD_GRAYSCALE)`.
   - Create noise using `np.random.normal(0, 25, image.shape)`.
   - Add noise to create the adversarial image using `cv2.addWeighted()`.
   - Display the adversarial image using `cv2.imshow()`.

## GAN Training

### Steps

1. **GAN Definition**:
   - Define the **Generator**:
     - Map input noise to 128 features using a fully connected layer.
     - Introduce non-linearity using `ReLU` activation functions.
     - Expand feature space to 256 dimensions.
     - Map features to a 28x28 image using another fully connected layer.
     - Scale output pixel values to the range `[-1, 1]` using `Tanh`.
   - Define the **Discriminator**:
     - Take a flattened 28x28 image as input.
     - Reduce features to 128 dimensions using linear layers.
     - Introduce non-linearity using `LeakyReLU`.
     - Output a single value (real/fake score) using a `Sigmoid` function.

2. **GAN Training Loop**:
   - Define loss function as `BCELoss()`.
   - Set up optimizers using `optim.Adam()`.
   - Train the Discriminator:
     - Generate fake images from random noise.
     - Calculate loss for real and fake images.
     - Perform backpropagation to update Discriminator parameters.
   - Train the Generator:
     - Get Discriminator's predictions for the fake images.
     - Calculate the Generator's loss.
     - Perform backpropagation to update Generator parameters.

## Noise Addition and Denoising

### Steps

1. **Load and Preprocess the Image**:
   - Load the image using `cv2.imread('flower.png', cv2.IMREAD_GRAYSCALE)`.
   - Resize and normalize the image.

2. **Add Gaussian Noise in Steps**:
   - Add Gaussian noise to the image in incremental steps.
   - Display each noisy image using `cv2.imshow()`.
   - Denoise the image using `cv2.GaussianBlur()`.
   - Display the denoised image.

## Observations

- **Adversarial Image Generation**:
  - Creates adversarial images by adding random noise, demonstrating potential vulnerabilities.

- **GAN (Generative Adversarial Network)**:
  - Consists of a Generator that creates fake images and a Discriminator that differentiates between real and fake images.
  - Trains through a competition, improving the quality of generated images over time.

- **Noise Addition and Denoising**:
  - Incrementally adds Gaussian noise to images and applies Gaussian blur for denoising.
  - Helps in understanding the effects of noise and the denoising process.

## Conclusion

This document demonstrates how to generate adversarial images, define and train a GAN, and add and denoise Gaussian noise using PyTorch and OpenCV in Python. These techniques are crucial for understanding the vulnerabilities of image-processing systems and the process of image generation and denoising.