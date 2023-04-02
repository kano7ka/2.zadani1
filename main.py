from PIL import Image

def rotate_image(file):
    with Image.open(file) as im:
        im_rotated=im.transpose(method=Image.ROTATE_90)
    im_rotated.save("rotated-" + file,im.format)
    im_rotated.show()