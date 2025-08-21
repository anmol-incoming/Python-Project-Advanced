from PIL import Image
import numpy as np
def blur_image(img_array):#pass gray scale instead of img-arry if you want grayscale blur 
    # This code was for gray_scale image but i consider it to be better,
    #if i applied it directly on RBG image instead of Grayscale image.
    """"
    kernal_size=15
    rows=gray_scale.shape[0]
    columns=gray_scale.shape[1]
    
    kernel=np.ones((15,15))/225
    pad=kernal_size//2
    padding=np.pad(gray_scale,((pad,pad),(pad,pad)),mode='edge')
    output=np.zeros_like(gray_scale,dtype=np.float64)
    #gray_scale.astype(np.float64)

    for i in range(rows):
        for j in range(columns):
            patch=padding[i:i+15,j:j+15]
            blur_img=patch*kernel
            output[i,j]=np.sum(blur_img)
    output=np.clip(output,0,255).astype(np.uint8)
    output_img=Image.fromarray(output,mode="L")
    output_img.show()
    """
    kernel_size=15
    #print(img_array.shape)
    ax=np.linspace(-(kernel_size-1)/2,(kernel_size-1)/2,kernel_size)
    x,y=np.meshgrid(ax,ax)
    sigma=6
    kernel=np.exp(-(x**2+y**2)/(2*sigma**2))
    kernel=kernel/np.sum(kernel)

    img_array=img_array.astype(np.float64)
    rows,columns,channels=img_array.shape
    #kernel=np.ones((kernel_size,kernel_size))/(kernel_size*kernel_size)
    output=np.zeros_like(img_array,dtype=np.float64)
    #print(output.shape)

    for c in range(channels):
        padding=np.pad(img_array[:,:,c],pad_width=kernel_size//2,mode="edge")
        for i in range(rows):
            for j in range(columns):
                patch=padding[i:i+kernel_size,j:j+kernel_size]
                blur_img=patch*kernel
                output[i,j,c]=np.sum(blur_img)

    output=np.clip(output,0,255).astype(np.uint8)
    output_img=Image.fromarray(output,mode="RGB")
    output_img.show()
    





    


