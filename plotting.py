import matplotlib.pyplot as plt

def plotting(original_image, noisy_image, box_blur_recovered_image, median_recovered_image, gaussian_recovered_image):
    plt.figure(figsize=(16, 8))

    plt.subplot(2,3, 1)
    plt.imshow(original_image, cmap="gray")
    plt.title('Original image')
    plt.axis('off')
    plt.subplot(2,3, 2)
  
    plt.imshow(noisy_image, cmap="gray")
    plt.title('Noisy image' )
    plt.axis('off')
   
    plt.subplot(2,3, 3) 
    plt.imshow(box_blur_recovered_image, cmap="gray")
    plt.title('Box blur filter recovered Image' )
    plt.axis('off') 
    plt.subplot(2,3, 4)
    
    plt.imshow(median_recovered_image, cmap="gray")
    plt.title('Median filter recovered Image' )
    plt.axis('off')
    
    plt.subplot(2,3, 5)
    plt.imshow(gaussian_recovered_image, cmap="gray")
    plt.title('Gaussian filter recovered Image' )
    plt.axis('off')
    

    
    plt.show()