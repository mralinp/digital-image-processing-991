import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from scipy.fftpack import dctn, idctn

quantize_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                            [12, 12, 14, 19, 26, 58, 60, 55],
                            [14, 13, 16, 24, 40, 57, 69, 56],
                            [14, 17, 22, 29, 51, 87, 80, 62],
                            [18, 22, 37, 56, 68, 109, 103, 77],
                            [24, 35, 55, 64, 81, 104, 113, 92],
                            [49, 64, 78, 87, 103, 121, 120, 101],
                            [72, 92, 95, 98, 112, 100, 130, 99]])

sequence = [-40.0, 8.0, 7.0, 1.0, 5.0, 1.0, -
            1.0, 1.0, 1.0, -1.0, 0.0, -0.0, 1.0, 'EOB']


def sequence_to_block(sequence):

    width = 8
    height = 8
    decodedSequence = np.array([[0 for i in range(width)]
                                for j in range(height)])
    currentPos = (0, 0)
    direction = (-1, 1)
    for i in range(len(sequence)-1):
        decodedSequence[currentPos[0], currentPos[1]] = sequence[i]
        newPos = tuple(map(lambda x, y: x+y, currentPos, direction))
        if(newPos[0] < 0 or newPos[1] < 0 or newPos[0] > height or newPos[1] > width):
            if(direction == (-1, 1)):
                newPos = tuple(map(lambda x, y: x+y, (0, 1), currentPos))
                if(newPos[1] > width):
                    newPos = tuple(map(lambda x, y: x+y, (+1, 0), currentPos))
            elif(direction == (1, -1)):
                newPos = tuple(map(lambda x, y: x+y, (+1, 0), currentPos))
                if(newPos[0] > height):
                    newPos = tuple(map(lambda x, y: x+y, (0, +1), currentPos))
            direction = tuple(map(lambda x, y: x*y, (-1, -1), direction))
        currentPos = newPos
    return decodedSequence


def inverse_transform(block):
    width = 8
    height = 8
    block = block*quantize_matrix
    block = np.float32(block)
    block = cv.idct(block)
    block = np.uint8(block)
    block = block + 128
    cv.imwrite("Q2.bmp", block)


if __name__ == "__main__":
    inverse_transform(sequence_to_block(sequence))
