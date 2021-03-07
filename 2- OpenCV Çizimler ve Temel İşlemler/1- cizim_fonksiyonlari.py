import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255    # belli alana siyah tuval oluşturur, 255 eklediğimizde beyaz oluşur, 3 kanal veri var
print(canvas)                                           # matrisi gösterir

cv2.imshow("Canvas Deneme", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()