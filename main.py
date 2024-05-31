import generate_blur_and_noisy_img as gen_img
import matplotlib.pyplot as plt
import cv2  
import recovering as rcv
import plotting
import MSE_and_psnr as Map
import time

image_path = 'HQ.jpg'  #input your image's path here

original_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
temp_image =cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)

print("Input the sigma:")
sigma = float(input())



print("Generating noisy image with sigma = {0}".format(sigma))
temp_time = time.time()


#noisy_image = gen_img.add_gaussian_noise(original_image, sigma)
noisy_image = gen_img.add_salt_and_pepper_noise(temp_image)




psnr_of_noised_img = Map.psnr(original_image, noisy_image)
print("Took {0:.2f} seconds.\n".format(time.time() - temp_time))

print("Processing box blur method---")
temp_time = time.time()
box_blur_recovered_image = rcv.box_blur(noisy_image,10)
print("Took {0:.2f} seconds.\n".format(time.time() - temp_time))

temp_time = time.time()
print("Processing median method---")
median_recovered_image = rcv.median_filter(noisy_image, 5)
print("Took {0:.2f} seconds.\n".format(time.time() - temp_time))

temp_time = time.time()
print("Processing gaussian filter method---")
gaussian_recovered_image = rcv.gaussian_filter(noisy_image, 5, 1.5)
print("Took {0:.2f} seconds.\n".format(time.time() - temp_time))


print("""
    With sigma = {0:.4f}, we have 
              MSE = {1:.2f} and psnr = {2:.1f}
      
    MSE value between the original image and image recovered by:
    1. Blur box filter method: {3:.2f}
    2. Median filter method: {4:.2f}
    3. Gaussian filter method: {5:.2f}

      """.format(sigma, Map.mse(original_image, noisy_image), psnr_of_noised_img,
                 Map.mse(original_image, box_blur_recovered_image), Map.mse(original_image, median_recovered_image),
                 Map.mse(original_image, gaussian_recovered_image)
                 ))

plotting.plotting(original_image, noisy_image, box_blur_recovered_image, median_recovered_image, gaussian_recovered_image)
