from PIL import Image
im = Image.open("original_images/img-num-1.jpg")
new_im = im.resize((640,480))
new_im.save("modified_images/modif_img1.jpg")
