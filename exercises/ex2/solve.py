import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def solve1():
    histogram = [0,2,4,6,3,1,0,0,0,0]
    labels = [str(i) for i in range(10)]
    # plt.bar(labels, histogram, width=0.4)
    # plt.xlabel("color value")
    # plt.ylabel("pixel count")
    # plt.title("image histogram")
    # plt.show()
    newValues = [0]
    for i in range(1, len(histogram)):
        newValues += [histogram[i-1] + histogram[i]]
    for i in range(len(newValues)):
        newValues[i] = int(newValues[i]*(9/16))
    normalizedHistogram = [0 for i in range(10)]
    print(normalizedHistogram)
    for i in range(len(histogram)):
        print(i, newValues[i], histogram[i],normalizedHistogram[i])
        normalizedHistogram[newValues[i]] += histogram[i];
    print (normalizedHistogram)
if __name__ == "__main__":
    solve1()
