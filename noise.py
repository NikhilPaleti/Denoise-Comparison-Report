import numpy as np

# def add_noise(image, sigma=20): #Gaussian noise
#     return image + np.random.normal(0, sigma, image.shape)

def add_noise(image, sigma=0.1): #Salt-and-Pepper noise
    # noisy = image.copy()
    image[np.random.rand(*image.shape) < sigma] = 0
    image[np.random.rand(*image.shape) < sigma] = 255
    return add_blur(image)

def add_blur(image, kernel_size=3): 
    kernel = np.ones((kernel_size, kernel_size))/(kernel_size**2)
    return np.convolve(image, kernel, mode='same')
