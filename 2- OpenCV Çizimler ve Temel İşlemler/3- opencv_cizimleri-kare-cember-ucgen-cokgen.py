import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255

#tuval üstüne çizgi çiziyoruz. (değişken, başlangıç noktası, bitiş noktası, rengi, kalınlık)
cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)            # mavi çizgi
cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=7)           # kırmızı çizgi


# dikdörtgen çizelim. (değişken, sol üst köşe başlangıç, sağ alt köşe bitiş, rengi, kalınlık)
# thickness -1 olursa içi dolu olur
cv2.rectangle(canvas, (20,20), (50,50), (0,255,0), thickness=2)         # yeşil dikdörtgen
cv2.rectangle(canvas, (50,50), (150,150), (0,255,255), thickness=2)     # sarı dikdörtgen


# çember çizelim (değişken, merkezi, yarıçap değeri, rengi, kalınlığı)
cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=5)              # kırmızı çember


# üçgen çizelim, özel fonksiyon yok. kendimiz çizeceğiz : 3 tane çizgi gibi
# öncelikle koordinat yazıyoruzi ardından köşegenler birleşecek şekilde çizgiler
p1 = (100,200)
p2 = (50,50)
p3 = (300,100)
cv2.line(canvas, p1, p2, (0,0,0), 4)
cv2.line(canvas, p2, p3, (0,0,0), 4)
cv2.line(canvas, p1, p3, (0,0,0), 4)


# düzgün olmayan dörtgen-beşgen çizelim. numpy özel koordinatı yapalım
# ardından polylines : (değişken, koordinatlarımız, açık-kapalı şekil, renk, kalınlık) -true kapalı şekil, false açık
points = np.array([[[110,200], [330,200], [290,220], [100,100]]], np.int32) # numpy özel koordinatı
cv2.polylines(canvas, [points], True, (0,0,100), 5)


#elips çizelim (değişken, en-boyu, yatay eksenle yapacağı açı, başlangıç açı, bitiş açı, renk, kalınlık)
# başlangıç ve bitiş açıları değişirse elipsi döndürebiliriz
cv2.ellipse(canvas, (300,300), (100,50), 0, 0, 360 , (255,255,0), 2)


cv2.imshow("Canvas Deneme", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()