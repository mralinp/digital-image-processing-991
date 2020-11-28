import cv2 as cv
import numpy as np

img = cv.imread('./1.bmp', cv.IMREAD_GRAYSCALE)
h, w = img.shape
vis0 = np.zeros((h,w), np.float32)
vis0[:h, :w] = img
vis1 = cv.dct(vis0)
vis2 = cv.dft(vis0)
print (vis1)
print (vis0)
print (vis2)

if __name__ == "__main__":
    print ("yes its", __name__)