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
    plt.ylabel("pixel count")
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
    hist1 = \
        [0 for i in range(64)] + \
        [1/128 for i in range(64,192)] +\
        [0 for i in range(192, 256)]
    hist2 = \
        [1/200 for i in range(100)] +\
        [0 for i in range(100,155)]+\
        [1/200 for i in range(155,256)]
    accumilator1 = [0]
    accumilator2 = [0]
    for i in hist1:
        accumilator1 += [(accumilator1[-1] + i)]
    accumilator1 = accumilator1[1:]
    for i in hist2:
        accumilator2 += [(accumilator2[-1] + i)]
    accumilator2 = accumilator2[1:]
    for i in range(len(accumilator1)):
        accumilator1[i] = [int((127/256)*accumilator1[i])]
    for i in range(len(accumilator2)):
        accumilator2[i] = [int((200/256)*accumilator2[i])]
    print (accumilator2)
    plt.plot(accumilator2)
    plt.show()
    
    return 0

if __name__ == "__main__":
    # question1a()
    question1b()
