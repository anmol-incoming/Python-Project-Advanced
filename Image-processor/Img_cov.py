import numpy as np
from PIL import Image
def img_conversion(img_array):
    if img_array.ndim==3:
        gray_scale=(
            0.299*img_array[:,:,0]+
            0.587*img_array[:,:,1]+
            0.114*img_array[:,:,2]
        ).astype(np.uint8)
        gray_img=Image.fromarray(gray_scale,mode="L")
        gray_img.show()
    

    

    return gray_scale
