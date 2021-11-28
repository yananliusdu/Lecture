
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = 'E:\\Career\\Lecture\\A.png'
img = cv2.imread(image_path, 0)
height, width = img.shape[:2]
# print(height, width)
# print(img)
img = np.asarray(img)

new_img = np.zeros((28,28))
delt_x = 5
delt_y = 5
T = np.array([[1, 0, delt_x], [0,1,delt_y], [0,0,1]])

for i in range(height):
    for j in range(width):
        p0 = np.array([[i,j,1]]).T
        p = np.dot(T,p0)
        new_x = p[0][0]
        new_y = p[1][0]
        if new_x >= height or new_y >= width:
            continue
        new_img[new_x][new_y] = img[i][j]

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(new_img)
plt.show()

print(new_img)




