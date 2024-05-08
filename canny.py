# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:11:41 2024

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import feature
import cv2

# Generate noisy image of a square
# image = np.zeros((128, 128), dtype=float)
# image[32:-32, 32:-32] = 1
# image = ndi.rotate(image, 15, mode='constant')
# image = ndi.gaussian_filter(image, 4)
# image = random_noise(image, mode='speckle', mean=0.1)

image = cv2.imread("D:/my/Pic/Incredible_Mixed_Wallpapers_Set_181/10.jpg")
image = ndi.gaussian_filter(image, 4)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Compute the Canny filter for two values of sigma
edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=3)

# display results
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('noisy image', fontsize=20)

ax[1].imshow(edges1, cmap='gray')
ax[1].set_title(r'Canny filter, $\sigma=1$', fontsize=20)

ax[2].imshow(edges2, cmap='gray')
ax[2].set_title(r'Canny filter, $\sigma=3$', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()