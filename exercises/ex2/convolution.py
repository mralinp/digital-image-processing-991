from math import exp
import numpy as np


def c(f, w):
    res = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            for s in range(-1, 2, 1):
                for t in range(-1, 2, 1):
                    x = 0
                    if(i+s >= 0 and j+t >= 0 and i+s < 3 and j+t < 3):
                        x = f[int(i+s)][int(j+t)]
                    res[i][j] += x*w[1+s][1+t]
    return res


f = [[1 for i in range(3)] for j in range(3)]
kernel = [[exp(-1), exp(-0.5), exp(-1)], [exp(-0.5), 1,
                                          exp(-0.5)], [exp(-1), exp(-0.5), exp(-1)]]
k = 0
for i in range(3):
    for j in range(3):
        k += kernel[i][j]

k = 1/k
k = k**3
print(k)
res = c(kernel, c(kernel, kernel))
for i in res:
    print(i)
