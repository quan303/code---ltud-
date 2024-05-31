import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
#def add_gaussian_noise(img, psnr):
#    mean = 0
#    sigma = 255 * 10 ** (-psnr / 20.0)
#    gaussian_noise = np.random.normal(mean, sigma, img.shape)
#    noisy_image = img + gaussian_noise
#    noisy_image = np.clip(noisy_image, 0, 255)
#    return noisy_image

def add_gaussian_noise(img, sigma):
    mean = 0
    w = np.random.normal(mean, float(sigma), img.shape)

    noisy_image = img + w
    noisy_image = np.clip(noisy_image, 0, 255).astype(img.dtype)
    return noisy_image

def add_salt_and_pepper_noise(image, salt_prob = .075, pepper_prob = .075):
    salt_mask = np.random.rand(image.shape[0], image.shape[1]) < salt_prob
    image[salt_mask] = 255 # White

    pepper_mask = np.random.rand(image.shape[0], image.shape[1]) < pepper_prob
    image[pepper_mask] = 0 # black
    return image