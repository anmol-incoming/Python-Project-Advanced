import numpy as np
from PIL import Image
def rotate_img(img_array):
    c=int(input("""Do you want to rotate image to:-
                    1.90 degree
                    2.180 degree:-"""))
    if c==1:
        rot_90=np.rot90(img_array,k=-1)
        rot_90=np.clip(rot_90,0,255).astype(np.uint8)
        rot_img=Image.fromarray(rot_90,mode="RGB")
        rot_img.show()
    elif c==2:
        rot_180=np.rot90(img_array,k=2)
        rot_180=np.clip(rot_180,0,255).astype(np.uint8)
        rot_img=Image.fromarray(rot_180,mode="RGB")
        rot_img.show()

    else:
        print("Invalid Input")