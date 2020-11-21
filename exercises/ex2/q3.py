import cv2 as cv
import numpy as np
import constants as const

img = cv.imread(const.path.TSUKUBA, cv.IMREAD_GRAYSCALE)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imwrite('./images/clahe_2.jpg', cl1)
cv.imshow('clhe_tsukuba', cl1)
cv.waitKey()
cv.destroyAllWindows()