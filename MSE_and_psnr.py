import numpy as np

def mse(imgage_1, imgage_2):
    return np.mean(np.square(np.subtract(imgage_1.astype(np.int32),
                                         imgage_2.astype(np.int32))))


def psnr(image_1, image_2):
    MSE = mse(image_1, image_2)
    if MSE == 0:
        return np.Inf
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX) - 10 * np.log10(MSE)