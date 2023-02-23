from PIL import Image as ig
import numpy as np

img1 = ig.open('old_image.png')

img = img1.copy()
np_img = np.array(img) # np_img[0][0:256] ~ np_img[255][0:256] -> [r,g,b], 65536개

pixel=img.load() # pixel[x,y] = (r,g,b)

for x in range(0,256) :
	  for y in range(0,256) :
		    pixel[np_img[x][y][1], np_img[x][y][0]] = (x,y,0) # 컬럼의 순서 변경

img.save('new_image.png')