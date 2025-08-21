from PIL import Image
import numpy as np
#from scipy.ndimage import convolve this prevents looping process
def sharpen_image(img_array):
    img_array=img_array.astype(np.float64)
    rows,columns,channels=img_array.shape
    kernel_size=15
    ax=np.linspace(-(kernel_size-1)/2,(kernel_size-1)/2,kernel_size)
    x,y=np.meshgrid(ax,ax)
    sigma=5
    kernel=np.exp(-(x**2+y**2)/(2*sigma**2))
    kernel=kernel/np.sum(kernel)
    output=np.zeros_like(img_array,dtype=np.float64)
    alpha=2

    for c in range(channels):
        padding=np.pad(img_array[:,:,c],pad_width=kernel_size//2,mode="edge")
        #blurred[:,:,c] = convolve(img_array[:,:,c], kernel, mode='nearest')
        #the above prevents looping process and does it internally instead of manually
        #better for large image size and much faster 
        for i in range(rows):
            for j in range(columns):
                patch=padding[i:i+kernel_size,j:j+kernel_size]
                blur_img=patch*kernel
                output[i,j,c]=np.sum(blur_img)

    sharpen_img=img_array+alpha*(img_array-output)

    sharpen_img=np.clip(sharpen_img,0,255).astype(np.uint8)
    output_img=Image.fromarray(sharpen_img,mode="RGB")
    output_img.show()



    


