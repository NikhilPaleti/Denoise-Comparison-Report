import bm3d
import os
import time
import numpy as np
import matplotlib.pyplot as plt

from noise import add_noise
from tests import PSNR, SSIM

def grayscale(img):
    return np.dot(img[...,:3], [0.299, 0.587, 0.114])

images = ["pixel.jpg", "1to1.jpg", "fashion.jpg", "lena.jpg", "nature.jpg"]
times_list = []
ssim_list = []
psnr_list = []

