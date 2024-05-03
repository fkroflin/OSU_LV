import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")
img = img[:,:,0].copy()

plt.imshow(img, cmap = "gray")
plt.figure()

#a
plt.imshow(img, alpha=0.5, cmap="gray")
plt.figure()

#b
b = np.hsplit(img.copy(), 4)[1]
plt.imshow(b, cmap = "gray")
plt.figure()

#c
c = np.rot90(np.rot90(np.rot90(img.copy())))
plt.imshow(c, cmap = "gray")
plt.figure()

#d
d = np.flip(img.copy(), axis = 1)
plt.imshow(d, cmap = "gray")
plt.show()
