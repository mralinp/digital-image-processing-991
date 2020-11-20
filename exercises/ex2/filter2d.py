import cv2 as cv
import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
res = cv.filter2D(mat, -1, kernel)
print(mat)
print(kernel)
print(res)
