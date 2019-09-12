# HistogramEqualization
Script that applies histogram equalization to a greyscale image.

Accompanying blog post: https://ukdevguy.com/...

Image credit: https://www.instagram.com/lorrainewhiteside/

## Examples
### 1: Image with colour range reduced for demonstration purposes
![Input image (left) vs output image (right)](https://i.imgur.com/2S1tEIe.png)


### 2: Old photo with no moficiations apart from histogram equalization
![Input image (left) vs output image (right)](https://i.imgur.com/c7BT7k4.png)


### 3: Colour version of cow, no other modifications
![Input image (left) vs output image (right)](https://i.imgur.com/HkxQGP6.png)


### 4: Colour version of dog, no other modifications
![Input image (left) vs output image (right)](https://i.imgur.com/jRldRTk.png)

## Usage Guide - Greyscale
The `image_processor.py` class can be used to convert a colour image to greyscale, reduce the size of an image and reduce the colour range of an image. There are four constants you need to worry about:

| Constant   | Description                                 | Example                                                                               |
|------------|---------------------------------------------|---------------------------------------------------------------------------------------|
| SHRINK_AMT | Amount to shrink the image by               | If we had an image with width = 1000 and SHRINK_AMT = 4 the new width would be 250    |
| STRENGTH   | Denotes how much to shrink the histogram by | 0 = don't shrink, 1 = shrink completely. Leave at 0 unless for demonstration purposes |
| IN_FILE    | Path where the input file is located        | "input.png"                                                                           |
| OUT_FILE   | Path where the output file should be saved  | "output.png"                                                                          |

Once our image is processed into greyscale, we can use the `equalizer_greyscale.py` class to apply histogram equalization. This class has only two constants to set:

| Constant | Description                                                     | Example        |
|----------|-----------------------------------------------------------------|----------------|
| IN_FILE  | Path where the input file is located (must be greyscale image!) | "modified.png" |
| OUT_FILE | Path where the output file should be saved                      | "output.png"   |

## Usage Guide - Colour
The colour version of the script, `equalizer_colour.py`, converts the input image into the YCbCr colour format. It then applies histogram equalization onto the Y channel. To use this script simply set the input and output variables in exactly the same way as the greyscale version.

**Note: the output file type must be jpg.**

Any questions feel free to leave a comment over at the [blog post](https://ukdevguy.com/).
