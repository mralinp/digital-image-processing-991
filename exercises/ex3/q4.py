import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

import pywt
import pywt.data


if __name__ == "__main__":
    img = cv.imread("./3.bmp", cv.IMREAD_GRAYSCALE)
    src = cv.imread("./4.bmp", cv.IMREAD_GRAYSCALE)
    print(cv.PSNR(img, src))

    titles = ['Approximation', ' Horizontal detail',
            'Vertical detail', 'Diagonal detail']
    coeffs2 = pywt.dwt2(img, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2
    # LH = HL = HH = np.zeros(LH.shape)
    
    fig = plt.figure(figsize=(12, 3))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    fig.tight_layout()
    plt.show()
    
    LH = HL = HH = np.zeros(LH.shape)
    res = pywt.idwt2((LL, (LH, HL,HH)), "Haar")
    res = np.uint8(res)
    cv.imshow("result", res)
    cv.imwrite("q4_res.jpg", res)
    cv.imshow("src", src)
    print(res[2:258,2:258].shape)
    print(cv.PSNR(res[2:258,2:258], src))
    cv.waitKey()
    cv.destroyAllWindows()
    