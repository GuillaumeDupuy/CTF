import numpy as np
import cv2

df = cv2.imread('final.png')

df = np.mod(df[:, :, 2], 2)
with open('half.png', 'wb') as f:
    f.write(bytes(np.packbits(df)))

df = cv2.imread('half.png')
df = np.mod(df[:, :, 2], 2)
print(bytes(np.packbits(df)))