from PIL import Image
from load_image import load_img
from Img_cov import img_conversion
from Img_arr import img_2d
from original_image import original_image
from blur_img import blur_image
from sharpen_img import sharpen_image
from edge_detection import edge_detection
from Rotate_img import rotate_img
def main_menu():
    while True:

        a=int(input("""Enter the operation you want to perfor,m on the image:-
                        1.View original image
                        2.black and white image/Gray scale Image
                        3.Blur Image
                        4.Sharpen Image
                        5.Edge detection
                        6.Rotate Image
                        7.exit:-"""))
        if a==1:
            original_image()
                       
        elif a==2:

            img=load_img()
            img_array=img_2d(img)
            img_conversion(img_array)

        elif a==3:
            img=load_img()
            img_array=img_2d(img)
            #gray_scale=img_converter(img_array)
            # remove the above comment if want to pass gray scale and repalace it with img_array below
            blur_image(img_array)
        elif a==4:
            img=load_img()
            img_array=img_2d(img)
            sharpen_image(img_array)
        elif a==5:
            img=load_img()
            img_array=img_2d(img)
            edge_detection(img_array)


        elif a==6:
            img=load_img()
            img_array=img_2d(img)
            rotate_img(img_array)
        elif a==7:
            return print(f'Exited Successfully')
        else:
            print("Invalid Input")
run=main_menu()
