import numpy as np
import cv2
from scipy.signal import convolve2d


def box_blur(image, kernel_size):
    kernel_value = np.ones((kernel_size, kernel_size))
    kernel_value_normalized = kernel_value/ np.sum(kernel_value)
    blurred_image = convolve2d(image, kernel_value_normalized, mode='same', boundary='symm')
    
    return blurred_image



def median_filter(image, window_size):
    def median_value(data):
        data.sort()
        return data[len(data) // 2] 
    
    if window_size % 2 == 0:
      print("Window size must be an odd number")
      quit()

    filtered_image = np.zeros_like(image)  

    pad_width = window_size // 2 
    padded_image = cv2.copyMakeBorder(image, pad_width, pad_width, pad_width, pad_width, cv2.BORDER_REPLICATE)  

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_image[i:i + window_size, j:j + window_size] 
            median_val = median_value(window.flatten())  
            filtered_image[i, j] = median_val

    return filtered_image


def gaussian_filter(image, kernel_size, sigma):
    mean = 0
    kernel = np.fromfunction(
    # Gaussian formula
        lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(-((x - (kernel_size - mean) / 2) ** 2 + (y - (kernel_size - mean) / 2) ** 2) / (2 * sigma ** 2)),
        (kernel_size, kernel_size)
    )
    gaussian_kernel_value  =  kernel / np.sum(kernel)

    filtered_image =  convolve2d(image, gaussian_kernel_value,
                                  mode='same', boundary="symm")
    return filtered_image
