import numpy as np
import cv2

"""""
img = np.zeros((10,10,3), np.uint8)           # küçük bi görüntü yaptık

# burada da pikselleri teker teker boyuyoruz
img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,150)
img[0,3] = (255,255,15)
"""""
# burada da pikselleri teker teker boyuyoruz, ama siyah beyaz yapacağız :
img = np.zeros((10, 10), np.uint8)  # 3 kanal verisi olmayınca siyah beyaz oluyor
img[0,0] = 255
img[0,1] = 200
img[0,2] = 100
img[0,3] = 15

img = cv2.resize(img, (1000,1000), interpolation=cv2.INTER_AREA) # pikselleri yüz katı büyüttük

cv2.imshow("Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()