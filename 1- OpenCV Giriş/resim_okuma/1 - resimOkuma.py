import cv2                                                  # kütüphaneyi dahil ettik ve klasörümüze "klon.jpg" dosyasını ekledik

img = cv2.imread("klon.jpg")                                # resimlerin matematiksel değerini okur, içinde directory belirttik
                                                            # (dosya adı,cv2.IMREAD_GRAYSCALE) veya 0 yazmak resmi geri yapar

print(img)                                                  # okuduğu matrisi konsola yazar : (imaj değişkeni)

cv2.namedWindow("image",cv2.WINDOW_NORMAL)                  # pencere boyutunu ayarlanabilir yapar : (pencere adı, parametre)
cv2.imshow("image",img)                                     # yeni pencere açar : (pencere adı, değişken)
cv2.imwrite("klonyeni.jpg", img)                            # resmi kaydeder : (yeni dosya adı, değişken)
cv2.waitKey(0)                                              # penecerenin hemen kapanmasını önler
cv2.destroyAllWindows()                                     # bütün pencereleri kapar, her kodun sonuna yazılmalıdır


# masaüstündeki dosyayı kullanmak istiyorsak :
        #   img = cv2.imread("C:\Users\mertf\Desktop\mert.jpg")
        #   cv2.imwrite("klonMert.jpg", img)