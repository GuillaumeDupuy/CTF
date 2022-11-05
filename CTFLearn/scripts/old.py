from PIL import Image

i1 = Image.open("1.png")
i2 = Image.open("2.png")

pixels = 512

pix1 = i1.load()
pix2 = i2.load()

for i in range(pixels):
	for j in range(pixels):
		if pix1[i,j] == pix2[i,j]:
			pix1[i,j] = 0
		else:
			pix1[i,j] = 255
		
i1.save("flag.png")