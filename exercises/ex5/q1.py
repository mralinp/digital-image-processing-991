import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, ifft2, ifftshift
# %matplotlib inline

### 
# Hint: Dont forget to scale [0-1] and normalize psf
#       PSF image should be shifted before taking dft (H = fft2( ifftshif(psf) )
#       > Regards
###

def showImages(img):
    for i in range(len(img)):
        plt.subplot(1,len(img),i+1)
        plt.imshow(img[i], cmap='gray', vmin=0, vmax=255)
    plt.tight_layout()
    plt.show()

khayyam = cv.imread('./Khayyam.jpg', cv.IMREAD_GRAYSCALE)
psf1 = cv.imread('./psf1.bmp', cv.IMREAD_GRAYSCALE)
showImages([khayyam, psf1])


def normalize(mat):
    mat.astype(np.float32)
    return mat/mat.sum()

def weiner(img, psf, k=0):
    psf = normalize(psf)
    psf = ifftshift(psf)
    H = fft2(psf)
    H_2 = (np.abs(H) * np.abs(H))
    F = fft2(img)
    F = np.divide(H_2,(H_2 + k))*F
    F = np.divide(F,H)
    f = ifft2(F)
    f = np.abs(f)
    return f

showImages([weiner(khayyam, psf1, 10e-4)])

car = cv.imread("car.jpg", cv.IMREAD_GRAYSCALE)
showImages([car])

from math import cos, sin, pi, degrees
def line(r, teta):
    x = r*cos(teta)
    y = r*sin(teta)
    return (int(x),int(y))

h, w = car.shape
for i in range(-90, 90, 2):
    psf = np.zeros(car.shape)
    x, y = line(2, i*(pi/180))
    cv.line(psf, (h//2-x, w//2+y), (h//2+x, w//2-y), 255, 1)
    plate = weiner(car, psf, 0.001)
    plate = np.abs(plate)
    cv.imwrite("./plate"+str(i)+".bmp", plate)