import cv2 as cv
import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
import math
import matplotlib.pyplot as plt


def question1a():
    hist = [0, 2, 4, 6, 3, 1, 0, 0, 0, 0]
    colors = [str(i) for i in range(10)]
    n = 16  # 4*4 image
    plt.figure(1)
    plt.subplot(121)
    plt.title("Original Histogram")
    plt.xlabel("color value")
    plt.ylabel("color count")
    plt.bar(colors, hist, width=0.4)
    accumilator = [0]
    for i in hist:
        accumilator += [accumilator[-1] + i]
    accumilator = accumilator[1:]
    color_map = [0]
    for i in accumilator:
        color_map += [int(9*(i/n))]
    normalized_hist = [0 for i in range(10)]
    for i in range(10):
        normalized_hist[color_map[i]] = normalized_hist[color_map[i]] + hist[i]
    print(hist)
    print(color_map)
    print(normalized_hist)
    plt.subplot(122)
    plt.bar(colors, normalized_hist, width=0.4)
    plt.xlabel("color value")
    plt.ylabel("pixel count")
    plt.title("Normalized Histogram")
    print("Close the figure to continue!")
    plt.show()
    print("Done!")


def question1b():
    return 0

>>>>>>> 45f4b38f3452c65adaae514826f97463810d14e8

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
<<<<<<< HEAD
    solve1()
=======
    question1a()
    question1b()
>>>>>>> 45f4b38f3452c65adaae514826f97463810d14e8
