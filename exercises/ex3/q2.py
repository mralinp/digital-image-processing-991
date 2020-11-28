import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct

def getDct(img):
    imf = np.float32(img)
    dct = cv.dct(imf)
    # dshift = np.fft.fftshift(dct)
    magnitude_spectrum = 20*np.log(np.abs(dct))
    plt.title("DCT")
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    return dct


def getDft(img):
    dft = np.fft.fft2(img)
    fshift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    plt.title("DFT")
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum (shifted)'), plt.xticks([]), plt.yticks([])
    plt.show()
    return (dft)

def sortCofs(mat):
    mat = np.ravel(abs(mat))
    mat = list(mat)
    mat.sort(reverse=True)
    return np.array(mat)
    
if __name__ == "__main__":
    img = cv.imread("./1.bmp", cv.IMREAD_GRAYSCALE)
    dct = getDct(img)
    dft = getDft(img)
    sorted_dct = sortCofs(dct)
    sorted_dft = sortCofs(dft)
    for i in range(sorted_dft.shape[0]):
        sorted_dft[i] = sorted_dft[i]**2
    for i in range(sorted_dct.shape[0]):
        sorted_dct[i] = sorted_dct[i]**2
    cumsum_dft = np.cumsum(sorted_dft)
    cumsum_dct = np.cumsum(sorted_dct)
    plt.figure("cumsum 2")
    plt.subplot(1,2,1)
    plt.title("cumsum_dct")
    plt.plot(cumsum_dct)
    plt.subplot(1,2,2)
    plt.title("cumsum_dft")
    plt.plot(cumsum_dft)
    plt.show()
    