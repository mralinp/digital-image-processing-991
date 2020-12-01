import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from scipy.fftpack import dctn, idctn

quantize_matrix = np.array([[16,11,10,16,24,40,51,61],
                            [12,12,14,19,26,58,60,55],
                            [14,13,16,24,40,57,69,56],
                            [14,17,22,29,51,87,80,62],
                            [18,22,37,56,68,109,103,77],
                            [24,35,55,64,81,104,113,92],
                            [49,64,78,87,103,121,120,101],
                            [72,92,95,98,112,100,130,99]])

sequence = [-40.0, 8.0, 7.0, 1.0, 5.0, 1.0, -1.0, 1.0, 1.0, -1.0, 0.0, -0.0, 1.0, 'EOB']


def sequence_to_block(sequence):
    ### Implement this!!

def inverse_transform(block):
    ### Implement this!!

### Decode the sequence and generate a 8x8 image and save it as a BMP file

