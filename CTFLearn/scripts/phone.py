from pyzbar import pyzbar
import numpy as np
import cv2


arr = "0000000100110110010000000011111010001100101011111001000101010001011101000100100010100110011110100010010001011110101101010001001111101011100010101111100000000101010101010000000111111111010011101111111100110001111101110110100001100001100001010010100110101010010110110011100011100000011110101000011010011000010001000111000111000000100100110101010010000011101000110000101111000111111111010011111101001010000011001001101000000101011111111000001100111001100000000111100000010101011011111010100110101110101101000101011111110000010010100010110100001000011100010001011100100100101100101111101000111100101010010000000101111110100000000"
list = []
for i in arr:
    if int(i)==1:
        list.append(255)
    else:
        list.append(int(i))
img = np.array(list)
img = img.reshape(25,25).astype('float32') 
resized = cv2.resize(img, (36*10,37*10), interpolation = cv2.INTER_AREA)
cv2.imwrite('Result.png',resized)

img = cv2.imread("Result.png")
barcodes = pyzbar.decode(img)
print(barcodes)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))
