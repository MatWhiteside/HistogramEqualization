from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

"""
Script that applies histogram equalization to a greyscale image.
Specify an input image and name for the output image below.
When script is ran two histograms will be displayed:
 - The colour distribution of the original image
 - The colour distribution of the new image

Accompanying blog post: https://ukdevguy.com/...
"""

# Only two constants that need setting before running
IN_FILE = "5_input.png"
OUT_FILE = "5_output.png"

def make_histogram(img):
    """ Take an image and create a historgram from it """
    histogram = np.zeros(256, dtype=int)
    for row in range(img.shape[0]):
        for column in range(img[row].shape[0]):
            histogram[img[row][column][0]] += 1
            histogram[img[row][column][1]] += 1
            histogram[img[row][column][2]] += 1
    return histogram / 3

def make_cumsum(histogram):
    """ Create an array that represents the cumulative sum of the histogram """
    cumsum = np.zeros(256, dtype=int)
    cumsum[0] = histogram[0]
    for i in range(1, histogram.size):
        cumsum[i] = cumsum[i-1] + histogram[i]
    return cumsum

def make_mapping(histogram, cumsum):
    """ Create a mapping s.t. each old colour value is mapped to a new
        one between 0 and 255. Mapping is created using:
         - M(i) = max(0, round((grey_levels*cumsum(i))/(h*w))-1)
        where g_levels is the number of grey levels in the image """
    mapping = np.zeros(256, dtype=int)
    grey_levels = 256
    for i in range(histogram.size):
        mapping[i] = max(0, round((grey_levels*cumsum[i])/(IMG_H*IMG_W))-1)
    return mapping

def apply_mapping(img, mapping):
    """ Apply the mapping to our image """
    new_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=int)
    for row in range(img.shape[0]):
        for column in range(img[row].shape[0]):
            new_image[row][column][0] = mapping[img[row][column][0]] # R
            new_image[row][column][1] = mapping[img[row][column][1]] # G
            new_image[row][column][2] = mapping[img[row][column][2]] # B
    return new_image

# Load image, store width and height into constants
pillow_img = Image.open(IN_FILE)
IMG_W, IMG_H = pillow_img.size

# Read in and flatten our greyscale image, calculate the histogram,
# cumulative sum, mapping and then apply the mapping to create a new image
img = np.array(pillow_img)
#print(img)
histogram = make_histogram(img)
cumsum = make_cumsum(histogram)
mapping = make_mapping(histogram, cumsum)
new_image = apply_mapping(img, mapping)

print(new_image)

# Save the image
output_image = Image.fromarray(np.uint8(new_image))
output_image.save(OUT_FILE)

# Display the old (blue) and new (orange) histograms next to eachother
x_axis = np.arange(256)
fig = plt.figure()
fig.add_subplot(1, 2, 1)
plt.bar(x_axis, histogram)
fig.add_subplot(1, 2, 2)
plt.bar(x_axis, make_histogram(new_image), color="orange")
plt.show()
