from PIL import Image, ImageOps
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import random
import math

img= Image.open('cspace.png')
img =ImageOps.grayscale(img)

np_img = np.array(img)
np_img = ~np_img
np_img[np_img > 0] = 1
plt.set_cmap('binary')
plt.imshow(np_img)
np.save('cspace.npy', np_img)
# grid =np.load('cspace.npy')
# plt.imsave(grid)
# plt.show()