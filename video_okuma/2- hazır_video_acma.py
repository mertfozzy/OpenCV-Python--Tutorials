import cv2

cap = cv2.VideoCapture("robot.mp4")    # imread gibi ama video için. webcam için 0, kamera için 1 veya 2, bir video için ise adres
                                       # bir şekilde hata alırsan, 0 yanına şunu ekle : ,cv2.CAP_DSHOW
while True:
    ret, frame = cap.read()                               # okuma iki değer alır. frame okunursa ret true'dur
    if ret == 0:                                          # video bitince ekranı kapa
        break
    cv2.imshow("WRobot", frame)                           # sonsuz while döngüsü döndükçe frameleri göstereceğiz : (pencere adı, değişken)
    if cv2.waitKey(30) & 0xFF == ord("q") :               # videonun kare hızını seçiyoruz, 0 girersek hareket etmez, 1 normal olur
        break                                             # if yapısı ile ve ord'la -> q'ya basınca ekran kapatma fonksiyonu.


cap.release()                                             # while döngüsünü kapatır ve sonucu serbest bırakır
cv2.destroyAllWindows()