import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# yazı yazacağız (değişken, yazı, sol alt köşe koordinat, font, büyüklük, renk, yazı tipi)
cv2.putText(canvas, "OpenCV tutorial", (30,200), font1, 4, (0,0,0), cv2.LINE_AA)
cv2.putText(canvas, "OpenCV tutorial", (30,325), font2, 4, (0,0,0), cv2.LINE_4)
cv2.putText(canvas, "OpenCV tutorial", (30,450), font3, 4, (0,0,0), cv2.LINE_AA)

cv2.imshow("Canvas Deneme", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()