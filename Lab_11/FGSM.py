import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# ------------------- Adversarial Image Generation -------------------
# Load original image
image = cv2.imread('flower.png', cv2.IMREAD_GRAYSCALE)

# Create noise
noise = np.random.normal(0, 25, image.shape).astype('uint8')

# Add noise to create adversarial image
adversarial_image = cv2.addWeighted(image, 1.0, noise, 0.1, 0)

# Show the adversarial image
cv2.imshow('Adversarial Image', adversarial_image)
cv2.waitKey(0)

# ------------------- GAN Definition -------------------
latent_dim = 100  # Dimension of latent noise vector

# Generator
generator = nn.Sequential(
    nn.Linear(latent_dim, 128),  # Fully connected layer: maps input noise to 128 features
    nn.ReLU(),  # Activation function: introduces non-linearity
    nn.Linear(128, 256),  # Expands the feature space to 256 dimensions
    nn.ReLU(),  # Another activation function to make learning non-linear
    nn.Linear(256, 28 * 28),  # Output layer: maps features to 784 pixels (28x28 image)
    nn.Tanh()  # Scales output pixel values to the range [-1, 1]
)

# Discriminator
discriminator = nn.Sequential(
    nn.Linear(28 * 28, 256),  # Input layer: takes flattened 28x28 image (784 pixels)
    nn.LeakyReLU(0.2),  # Activation: allows small gradients for negative inputs (slope = 0.2)
    nn.Linear(256, 128),  # Hidden layer: reduces features to 128 dimensions
    nn.LeakyReLU(0.2),  # Another activation for non-linearity
    nn.Linear(128, 1),  # Output layer: maps features to a single value (real/fake score)
    nn.Sigmoid()  # Activation: outputs probability [0, 1] (real = 1, fake = 0)
)

# ------------------- GAN Training -------------------
# Loss function
criterion = nn.BCELoss()

# Optimizers
optimizer_G = optim.Adam(generator.parameters(), lr=0.0002)
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002)

# Training Loop
real_imgs = torch.randn(64, 28 * 28)  # Example real images (flattened)
fake_labels = torch.zeros(64, 1)  # Fake label (0)
real_labels = torch.ones(64, 1)  # Real label (1)

# 1. Train the Discriminator
# Generate fake images from random noise
z = torch.randn(64, latent_dim)  # Random noise
fake_imgs = generator(z)  # Fake images

# Calculate loss for real images
real_loss = criterion(discriminator(real_imgs), real_labels)

# Calculate loss for fake images
fake_loss = criterion(discriminator(fake_imgs.detach()), fake_labels)

# Total loss for the Discriminator
d_loss = real_loss + fake_loss

# Backpropagation to compute gradients
d_loss.backward()
optimizer_D.step()  # Update Discriminator parameters

# 2. Train the Generator
# Get the discriminator's predictions for the fake images
fake_preds = discriminator(fake_imgs)

# Calculate the Generator's loss
g_loss = criterion(fake_preds, real_labels)

# Backpropagation to compute gradients for the Generator
g_loss.backward()
optimizer_G.step()  # Update Generator parameters
