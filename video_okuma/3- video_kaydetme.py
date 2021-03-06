import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# frameleri tek tek kaydedeceğiz sırayı takip et !

fileName = "E:\webcam.avi"                                                      # 6 - Dosya adı oluşturuyoruz : orjinali : fileName = "webcam.avi"

codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')                              # 3 - Codec bileşeni standart 4 adet değer alır, internette var
frameRate = 30                                                                  # 4 - Frame Rate girdik, video hızı belirliyor.
resolution = (640,480)                                                          # 5 - Çözünürlük girdik.
videoFileOutput =  cv2.VideoWriter(fileName, codec, frameRate, resolution)      # 2 - Frameler geldi, parametreleri yazıyoruz.

# 7- Kaydedeceğimiz dosyaya sağ tıklayıp, Copy Path --> Absolute Path diyoruz, ve fileName = "webcam.avi" içerisine ekliyoruz

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    videoFileOutput.write(frame)                                                # 1 - Tek tek frameleri yukarı yolladık

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord ("q") :
        break

videoFileOutput.release()
cv2.release()
cv2.destroyAllWindows()