import os
import time
import numpy as np
import matplotlib.pyplot as plt

from noise import add_noise
from tests import PSNR, SSIM

def grayscale(img):
	return np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])

def median_filter(data, kernel_size):
    temp = []
    indexer = kernel_size // 2
    data_final = []
    data_final = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            for k in range(kernel_size):
                if i + k - indexer < 0 or i + k - indexer > len(data) - 1:
                    for c in range(kernel_size):
                        temp.append(0)
                else:
                    if j + k - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for x in range(kernel_size):
                            temp.append(data[i + k - indexer][j +  x - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

images = ["dataset/pixel.jpg", "dataset/1to1.jpg", "dataset/fashion.jpg", "dataset/lena.jpg", "dataset/nature.jpg"]
times_list = []
ssim_list = []
psnr_list = []

