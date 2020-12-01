import numpy as np
import cv2 as cv
from scipy.fftpack import fft2, ifft2
import matplotlib.pyplot as plt


### Load input image and sensor image -> g(x, y) & h(x, y)

### Rescale (0 - 255 -> 0 - 1) & Normalize sensor image

### 2D-FFT of input image -> G(u, v)

### 2D-FFT of sensor image -> H(u, v)

### Inverse filtering -> F_hat(u, v)

### 2D-iFFT of the filtering result -> f_hat(x, y)

### Save to file & plot if you want!