from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

"""
Script that applies histogram equalization to a colour image.
Specify an input image and name for the output image below (must be jpg).
When script is ran two histograms will be displayed:
 - The luma distribution of the original image (YCbCr)
 - The luma distribution of the new image (YCbCr)

Accompanying blog post: https://ukdevguy.com/...
"""

# Only two constants that need setting before running
IN_FILE = "4_input.jpg"
OUT_FILE = "4_output.jpg"

def make_histogram(img):
    """ Take an image and create a historgram from it's luma values """
    y_vals = img[:,:,0].flatten()
    histogram = np.zeros(256, dtype=int)
    for y_index in range(y_vals.size):
        histogram[y_vals[y_index]] += 1
    return histogram

def make_cumsum(histogram):
    """ Create an array that represents the cumulative sum of the histogram """
    cumsum = np.zeros(256, dtype=int)
    cumsum[0] = histogram[0]
    for i in range(1, histogram.size):
        cumsum[i] = cumsum[i-1] + histogram[i]
    return cumsum

def make_mapping(histogram, cumsum):
    """ Create a mapping s.t. each old luma value is mapped to a new
        one between 0 and 255. Mapping is created using:
         - M(i) = max(0, round((luma_levels*cumsum(i))/(h*w))-1)
        where luma_levels is the number of luma levels in the image """
    mapping = np.zeros(256, dtype=int)
    luma_levels = 256
    for i in range(histogram.size):
        mapping[i] = max(0, round((luma_levels*cumsum[i])/(IMG_H*IMG_W))-1)
    return mapping

def apply_mapping(img, mapping):
    """ Apply the mapping to our image """
    new_image = img.copy()
    new_image[:,:,0] = list(map(lambda a : mapping[a], img[:,:,0]))
    return new_image

# Load image, convert it to YCbCr format ten store width and height into constants
pillow_img = Image.open(IN_FILE).convert('YCbCr')
IMG_W, IMG_H = pillow_img.size

# Convert our image to numpy array, calculate the histogram, cumulative sum,
# mapping and then apply the mapping to create a new image
img = np.array(pillow_img)
histogram = make_histogram(img)
cumsum = make_cumsum(histogram)
mapping = make_mapping(histogram, cumsum)
new_image = apply_mapping(img, mapping)

# Save the image
output_image = Image.fromarray(np.uint8(new_image), "YCbCr")
output_image.save(OUT_FILE)

# Display the old (blue) and new (orange) histograms next to eachother
x_axis = np.arange(256)
fig = plt.figure()
fig.add_subplot(1, 2, 1)
plt.bar(x_axis, histogram)
fig.add_subplot(1, 2, 2)
plt.bar(x_axis, make_histogram(new_image), color="orange")
plt.show()
