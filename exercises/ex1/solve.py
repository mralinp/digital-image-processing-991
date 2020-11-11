import cv2 as cv
import numpy as np
import math


def show(name, img):
    cv.namedWindow(name)
    cv.imshow(name, img)
    print("press any key to continue...")
    cv.waitKey(0)
    cv.destroyAllWindows()


def firstStep():
    einsteinImg = cv.imread("./einstein.jpg", cv.IMREAD_GRAYSCALE)
    pepersImg = cv.imread("peppers.jpg", cv.IMREAD_GRAYSCALE)
    show("einstein", einsteinImg)
    show("peppers", pepersImg)
    return einsteinImg, pepersImg


def secondStep(img1, img2):
    height, width = img2.shape
    newImgMat = np.zeros((height, width), np.uint8)
    for i in range(width):
        for j in range(height):
            newImgMat[j][i] = img2[j][i] if (i < 127) else img1[j][i]
    show("peptein", newImgMat)
    cv.imwrite("./peptein.jpg", newImgMat)
    return newImgMat


def thiredStep(J):
    J_neg = 255 - J
    show("J-neg", J_neg)
    cv.imwrite("negative_einstein.jpg", J_neg)


def forthStep():
    coloredPeppers = cv.imread("peppers_color.png")
    height, width, channels = coloredPeppers.shape
    blue_peppers = coloredPeppers[:, :, 0]
    green_peppers = coloredPeppers[:, :, 1]
    red_peppers = coloredPeppers[:, :, 2]
    show("blue-channel", blue_peppers)
    show("green-channel", green_peppers)
    show("red-channel", red_peppers)


if __name__ == "__main__":
    enistein, peppers = firstStep()
    J = secondStep(enistein, peppers)
    thiredStep(J)
    forthStep()
    print("Done!")
