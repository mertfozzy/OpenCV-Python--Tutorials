# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:41:53 2021

@author: mertf
"""

"""
BUNLARA DİKKAT ET !!

- YOLO için https://pjreddie.com/darknet/yolo/ adresine git
- yolov3-416 paketinin cfg ve weight dosyalarını indirip proje klasöründe bir dosyaya ekle
- Spyder editörde kütüphaneyi conda aracılığı ile indirmeyi unutma

"""

import cv2
import numpy as np

img = cv2.imread("images/people.jpg")
print(img)

# konsola img.shape yazarak ölçüsünü gördük, ve indisleri koda verdik :
img_width = img.shape[1]
img_height = img.shape[0]

# görüntüyü blob formata çeviriyoruz :
#(değişken, sabit değer, yolo416 blob ölçeği, bgr-rgb değişimi, crop)
img_blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), swapRB=True, crop=False)

# konsola img_blob.shape yazarak blob değerlerimizi görüntülüyoruz.
# bizde (1, 3, 416, 416) çıktı

# modelin tanıyacağı labelları giriyoruz :
# önceden indirdiğimiz yolo algoritmasında 80 model var :
labels = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
         "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
         "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
         "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
         "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
         "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
         "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
         "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
         "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
         "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]

# kutucuk renkleri ayarlıyoruz :
# buradaki kodları teker teker konsola yazınca değer oluşuyor
colors = ["0,255,255","0,0,255","255,0,0","255,255,0","0,255,0"]
colors = [np.array(color.split(",")).astype("int") for color in colors]
colors = np.array(colors) # array haline getirdik
colors = np.tile(colors, (18,1)) # kutuları çoğalttık


# modeli import ediyoruz : algoritma başlangıcı
model = cv2.dnn.readNetFromDarknet("C:/Users/mertf/Desktop/python/YOLO Tutorial/pretrained_model/yolov3.cfg", "C:/Users/mertf/Desktop/python/YOLO Tutorial/pretrained_model/yolov3.weights")
layers = model.getLayerNames()
#çıktı katmanlarını araştırıyoruz
output_layer = [layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]

model.setInput(img_blob)

# çıktı katmanlarını detectiona sokuyoruz
detection_layers = model.forward(output_layer)
# çıktı katmanlarının içindeki değerleri almış olduk.


