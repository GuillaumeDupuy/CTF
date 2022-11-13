from pyzbar import pyzbar
import cv2

img_path = 'Untitled.png'

img = cv2.imread(img_path)

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