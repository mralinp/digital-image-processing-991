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
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = ((img[i][j] - f_min)/(f_max-f_min))*255
    return img

def clip_hist(img):
    histogram = [0 for i in range(256)]
    height, width = img.shape
    for i in range(height):
        for j in range(width):
            histogram[img[i, j]] += 1
    n = img.shape[0]*img.shape[1]
    accumilator = 0
    f_min , f_max = 0, 0
    for i in range(256):
        accumilator += histogram[i]
        if(accumilator >= n*0.01):
            f_min = i
            break
    accumilator = 0
    for i in reversed(range(255)):
        accumilator += histogram[i]
        if(accumilator >= 0.01*n):
            f_max = i
            break
    for i in range(width):
        for j in range(height):
            img[j, i] = ((img[j, i] - f_min)/(f_max - f_min))*255
    return img

def normalize_hist(img):
    histogram = [0 for i in range(256)]
    height, width = img.shape
    for i in range(height):
        for j in range(width):
            histogram[img[i, j]] += 1
    accumilator = [histogram[0]]
    for i in range(1,256):
        accumilator += [accumilator[i-1] + histogram[i]]
    size = img.shape[0]*img.shape[1]
    for i in range(len(accumilator)):
        accumilator[i] = int(accumilator[i]*(255/size))
    mat = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            mat[i,j] = accumilator[img[i,j]]
    return mat

if __name__ == "__main__":
    images = []
    images += [(cv.imread(const.path.MAP, cv.IMREAD_GRAYSCALE), "Map")]
    images += [(cv.imread(const.path.TSUKUBA, cv.IMREAD_GRAYSCALE), "Tsukuba")]
    images += [(cv.imread(const.path.HAWKES_BAY,
                          cv.IMREAD_GRAYSCALE), "Hawkes_Bay")]
    plot_histogram("original images", images)
    images1 = []
    for i in range(len(images)):
        images1 += [(streach_hist(images[i][0]), images[i][1])]
    plot_histogram("after using streached histogram method", images1)
    images2 = []
    for i in images:
        images2 += [(clip_hist(i[0]), i[1])]
    plot_histogram("after using chip histogram method", images2)
    images3 = []
    for i in images:
        images3 += [(normalize_hist(i[0]), i[1])]
    plot_histogram("after using normalized histogram method", images3)