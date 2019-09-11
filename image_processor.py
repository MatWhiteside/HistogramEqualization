from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

"""
Script to allow simple modifications to images that better allows the histogram
equalization algorithm to be demonstrated.
"""

# Size for new image (img / SHRINK_AMT) none = 1, 1/2 = 2, 1/4 = 4, etc
SHRINK_AMT = 4
# Amount to compress the historgram: 0 (weak) to 1 (strong)
STRENGTH = 0.5
# Input image and name for the output image
IN_FILE = "input.jpg"
OUT_FILE = "modified.png"

def make_greyscale(img):
    """ Convert an image to greyscale """
    return img.convert("L")

def resize(img, width, height):
    """ Resize an image to a new width, height """
    return img.resize((width, height))

def save(img, output_str):
    """ Save an image to the disk """
    img.save(output_str)

def compress_histogram(img, strength):
    """ Reduce the number of greys in an image by compressing it's histogram
        towards the centre values """
    modified = np.zeros(img.size, dtype=int)
    for i in range(img.size):
        diff = 127 - img[i]
        modified[i] = img[i] + int(diff * STRENGTH)
    return modified

def img_to_array(img):
    """ Convert a Pillow image into a NumPy array """
    return np.array(img).flatten()

def array_to_img(arr, width, height):
    """ Convert a NumPy array into a Pillow image """
    arr = arr.reshape((height, width))
    return Image.fromarray(np.uint8(arr))

# Carry out the image processing
img = Image.open(IN_FILE)
w, h = img.size
new_w = int(w/SHRINK_AMT)
new_h = int(h/SHRINK_AMT)
img = make_greyscale(img)
img = resize(img, new_w, new_h)
img = array_to_img(compress_histogram(img_to_array(img), STRENGTH), new_w, new_h)
save(img, OUT_FILE)
