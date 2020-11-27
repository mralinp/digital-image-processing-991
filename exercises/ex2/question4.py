import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from math import exp

# implement a function that returns a gaussian kernel

def gaussian(s,t, std=1):
    x = (s*s + t*t)/(2*std*std)
    return exp(-x)
def make_gaussian(size=3, std=1):
    kernel = np.zeros((size, size), np.float32)
    k = 0
    if(size%2 != 0):
        for s in range(-int(size/2), int(size/2) + 1, 1):
            for t in range(-int(size/2), int(size/2) + 1, 1):
                kernel[int(size/2) + s, int(size/2) + t] = gaussian(s,t,std)
                k += kernel[int(size/2) + s, int(size/2) + t]
        kernel = kernel/k
    return kernel

# implement a 2D convolution
def convolve2d(image, kernel):
    # You do not need to modify these, but feel free to implement your own
    kernel       = np.flipud(np.fliplr(kernel))  # Flip the kernel, if it's symmetric it does not matter
    kernel_width = kernel.shape[0]
    kernel_height= kernel.shape[1]
    padding      = (kernel_width - 1)
    offset       = padding // 2
    output       = np.zeros_like(image)
    # Add zero padding to the input image
    image_padded = np.zeros((image.shape[0] + padding, image.shape[1] + padding))   
    image_padded[offset:-offset, offset:-offset] = image
    # implement the convolution inside the inner for loop
    size = kernel.shape[0]//2
    percent = 0
    tmp = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            r = 0
            for s in range(-size, size+1, 1):
                for t in range(-size, size+1, 1):
                    r += kernel[size+s, size+t]*image_padded[x+s, y+t]
            output[x,y] = int(output[x,y])
    return output

if __name__ == "__main__":
    gray_img = cv.imread("./Azadi.jpg", cv.IMREAD_GRAYSCALE)
    img = 255-gray_img
    # bllured = convolve2d(img, make_gaussian(19,3))
    bllured = cv.filter2D(img, -1, make_gaussian(19,3))
    cv.imwrite("./azadi_blured.jpg", bllured)
    res = cv.divide(gray_img, 255-bllured, scale=256)
    cv.imwrite("./azadi_pencil_sketch.jpg", res)