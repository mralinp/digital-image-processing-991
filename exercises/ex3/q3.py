import numpy as np
import cv2 as cv

def idealFilter(size, center):
    P = size[0]
    Q = size[1]
    filter = np.zeros(size, np.uint8)
    for i in range(P//2):
        for j in range(Q//2):
            if((i-center[0])**2 + (j-center[1])**2 <= size[0]/2):
                filter[i,j] = 1
    return filter

def multiplier2D(img, filter):
    img = np.float32(img)
    dct = cv.dct(img)
    ret = dct*filter
    ret = cv.idct(ret)
    return ret
    
if __name__ == "__main__":
    img = cv.imread("./2.jpg", cv.IMREAD_GRAYSCALE)
    cv.imshow("input", img)
    filter = idealFilter(img.shape,(0,0))
    cv.imwrite("./filter.jpg", filter*255)
    res = multiplier2D(img, filter)
    res = np.uint8(res)
    cv.imshow("result", res)
    cv.imwrite("./res.png", res)
    cv.waitKey()
    cv.destroyAllWindows()
    