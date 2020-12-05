import numpy as np
import cv2 as cv
from scipy.fftpack import fft2, ifft2
import matplotlib.pyplot as plt
from math import sqrt
import statistics as stat

## Load input image and sensor image -> g(x, y) & h(x, y)

### Rescale (0 - 255 -> 0 - 1) & Normalize sensor image

### 2D-FFT of input image -> G(u, v)

### 2D-FFT of sensor image -> H(u, v)

### Inverse filtering -> F_hat(u, v)

### 2D-iFFT of the filtering result -> f_hat(x, y)

### Save to file & plot if you want!

def normalize(mat):
    height, width = mat.shape
    norm = 0
    for i in range(height):
        for j in range(width):
            norm += mat[i,j]*mat[i,j]
    norm = sqrt(norm)
    mat /= norm
    return mat

def partOne():
    g = cv.imread("./cam_1.bmp", cv.IMREAD_GRAYSCALE)
    h = cv.imread("./sensor.bmp", cv.IMREAD_GRAYSCALE)
    g = np.float32(g)
    h = np.float32(h)/255 # scale
    h = normalize(h) # normalize
    g = fft2(g)
    h = fft2(h)
    f = g/h
    f = ifft2(f)
    f = np.uint8(f)
    cv.imwrite("Q4_1.bmp", f)
    return f

def partTwo():
    g = cv.imread("./cam_2.bmp", cv.IMREAD_GRAYSCALE)
    h = cv.imread("./sensor.bmp", cv.IMREAD_GRAYSCALE)
    g = np.float32(g)
    h = np.float32(h)/255 # scale
    h = normalize(h) # normalize
    g = fft2(g)
    h = fft2(h)
    f = g/h
    f = ifft2(f)
    f = np.uint8(f)
    cv.imwrite("Q4_2.bmp", f)
    return f

def partThree():
    img = cv.imread("./cam_2.bmp", cv.IMREAD_GRAYSCALE)
    subImg = img[40:60, 40:60]
    plt.figure("histogram")
    plt.subplot(1,2,1)
    plt.title("sub-image")
    plt.imshow(subImg, cmap='gray', vmin=0, vmax=255)
    plt.subplot(1,2,2)
    plt.title("Histogram")
    plt.hist(subImg.ravel(), bins=256, range=(0, 255))
    # print (list(subImg.ravel()))
    l = list(subImg.ravel())
    l = [float(i) for i in l]
    print ("Deviation : %f" % stat.pstdev(l))
    print("Mean : %f" % stat.mean(l))
    plt.show()

    
if __name__ == '__main__':
    res1 = partOne()
    plt.figure("Results")
    plt.subplot(1,2,1)
    plt.title("Noise Free")
    plt.imshow(res1, cmap='gray', vmin=0, vmax=255)
    res2 = partTwo()       
    plt.subplot(1,2,2)
    plt.title("Noisy picture")
    plt.imshow(res2, cmap='gray', vmin=0, vmax=255)
    plt.show()
    partThree()