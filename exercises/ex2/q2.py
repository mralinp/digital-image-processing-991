import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import constants as const


def plot_histogram(title, images):
    plt.figure(title)
    number_of_images = len(images)
    for i in range(number_of_images):
        plt.subplot(number_of_images, 2, 2*i + 1)
        plt.title(images[i][1])
        plt.imshow(images[i][0], 'gray')
        plt.subplot(number_of_images, 2, 2*i + 2)
        plt.hist(images[i][0].ravel(), bins=256, range=(0, 255))
    print("close the window to continue!")
    plt.show()


def streach_hist(img):
    f_max = np.amax(img)
    f_min = np.amin(img)
    print(f_max, f_min)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = ((img[i][j] - f_min)/(f_max-f_min))*255
    return img


if __name__ == "__main__":
    images = []
    images += [(cv.imread(const.path.MAP, cv.IMREAD_GRAYSCALE), "Map")]
    images += [(cv.imread(const.path.TSUKUBA, cv.IMREAD_GRAYSCALE), "Tsukuba")]
    images += [(cv.imread(const.path.HAWKES_BAY,
                          cv.IMREAD_GRAYSCALE), "Hawkes_Bay")]
    plot_histogram("original images", images)
    for i in range(len(images)):
        images[i] = (streach_hist(images[i][0]), images[i][1])
    plot_histogram("after using streached histogram method", images)
