import numpy as np
from math import log2

def calEntropy(mat):
    l = [0 for i in range(256)]
    height, width = mat.shape
    for i in range(height):
        for j in range(width):
            l[mat[i,j]] = l[mat[i,j]] + 1
    ret = 0
    for i in range(256):
        if(l[i]!=0):
            ret = ret + (l[i]/(width*height))*(log2(l[i]/(width*height)))
    return -ret

if __name__ == '__main__':
    mat = np.array([[2,1,254,2,254,255],
                    [2,2,255,2,252,253],
                    [3,0,253,3,255,251],
                    [2,1,255,1,254,253]], np.uint8)
    print(calEntropy(mat))
    