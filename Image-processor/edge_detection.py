from PIL import Image
import numpy as np
from scipy.ndimage import convolve
def edge_detection(img_array):
    img_array=img_array.astype(np.float64)
    row,column,channels=img_array.shape
    kernel_size=15
    ax=np.linspace(-(kernel_size-1)/2,(kernel_size-1)/2,kernel_size)
    x,y=np.meshgrid(ax,ax)
    sigma=6
    kernel=np.exp(-(x**2+y**2)/(2*sigma**2)) 
    kernel=kernel/np.sum(kernel)
    blured_output=np.zeros_like(img_array,dtype=np.float64)
    sobel_x_output=np.zeros_like(blured_output,dtype=np.float64)
    sobel_y_output=np.zeros_like(blured_output,dtype=np.float64)

    for c in range(channels):
        blured_output[:,:,c]=convolve(img_array[:,:,c],kernel,mode='nearest')
    blured_output=np.clip(blured_output,0,255)
    
    

    sobel_x=np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]])
    
    sobel_y=np.array([[-1,-2,-1],
                      [0,0,0],
                      [1,2,1]])
    
    for c in range(channels):
        sobel_x_output[:,:,c]=convolve(blured_output[:,:,c],sobel_x,mode='nearest')
        sobel_y_output[:,:,c]=convolve(blured_output[:,:,c],sobel_y,mode="nearest")
    edge_output=np.hypot(sobel_x_output,sobel_y_output)
    edge_output=np.clip(edge_output,0,255).astype(np.uint8)
    edge_img=Image.fromarray(edge_output,mode="RGB")
    edge_img.show()



    

