import cv2 as cv
import numpy as np
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
    histogram1 = \
        [0 for i in range(64)] +\
        [1/128 for i in range(128)] +\
        [0 for i in range(64)]
    histogram2 = \
        [1/200 for i in range(100)] +\
        [0 for i in range(55)] +\
        [1/200 for i in range(101)]
    print(histogram2[155], histogram2[154])
    for i in range(1, 256):
        histogram1[i] = histogram1[i] + histogram1[i-1]
        histogram2[i] = histogram2[i] + histogram2[i-1]
    for i in range(256):
        histogram1[i] *= 255
        histogram2[i] *= 255
    print(histogram1)
    plt.figure("question2")
    plt.subplot(1, 2, 1)
    plt.plot(histogram1)
    plt.xlim(0, 255)
    plt.subplot(1, 2, 2)
    plt.plot(histogram2)
    plt.show()


def question1c():
    pic = [5, 3, 3, 5, 1, 6, 4, 3, 3, 9, 7, 7, 9]
    kernel = [-1, -2, 5, -1, -1]
    res = [0 for i in range(9)]
    for i in range(2, 10):
        for j in range(5):
            res[i-2] += pic[i+j-2]*kernel[j]
        if (res[i-2] < 0):
            res[i-2] = 0
    print(res)


if __name__ == "__main__":
    # question1a()
    # question1b()
    question1c()
