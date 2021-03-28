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

img = cv2.imread("C:/Users/mertf/Desktop/python/YOLO Tutorial/yolo pretained image/images/people.jpg")
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



#%% non-maximum supression : operation 1
# hatalı kutuları ve oranları yok etmek için kullanılan bir yöntemdir :
 
ids_list = []
boxes_list = []
confidences_list = []


#%% non-maximum supression : operation 1 end

# deteksiyona başlıyoruz. for içinde for yaparak değerler oluşturduk
for detection_layer in detection_layers:
    for object_detection in detection_layer:
        
        scores = object_detection[5:] # puan tutuyoruz, 5 değer aldık
        predicted_id = np.argmax(scores) # en yüksek değerli indeksi çekiyoruz
        confidence = scores[predicted_id] # en güvenilir skoru alıyoruyz ve tutuyoruz
        
        if confidence > 0.35: # güvenilir skor yüzde 30dan iyiyse bounding box çizeceğiz
            
            # kutuyu çizerken sol alt köşeden başlayıp sağ üst köşeye gideceğiz
            label = labels[predicted_id] # id leri çektik ve aşağıda kutu çiziyoruz.
            bounding_box = object_detection[0:4] * np.array([img_width,img_height,img_width,img_height]) # boyut ayarladık
            (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
            
            # x ve y noktalarının özel koordinatı
            start_x = int (box_center_x - (box_width/2))
            start_y = int (box_center_y - (box_height/2))
            
            
#%% non-maximum supression : operation 2
# döngü içindeki değerleri listeliyoruz ve alta iletiyoruz
# for içinde yukarda oluşturulan kutuları dolduruyoruz :
    
            ids_list.append(predicted_id)
            confidences_list.append(float (confidence))
            boxes_list.append([start_x, start_y, int(box_width), int(box_height)])


#%% non-maximum supression : operation 2 end




#%% non-maximum supression : operation 3
# (yukardan gelen değerlerle) max_ids içerisinde en güvenilir kutuları saklıyorum

# cv2.dnn.NMSBoxes() maximum confidenceları liste yapar
# 0.5 ve 0.4 trashold değerleri yani standart

max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)

for max_id in max_ids: # liste içindeki değeri çekeceğiz
        max_class_id = max_id[0] # max_class_id aslında nesnenin tutulduğu id olacak
        box = boxes_list[max_class_id] # box en iyi değeri tutacak
                
        start_x = box[0] # box'un başlangıç noktası indis değeri
        start_y = box[1]
        box_width = box[2]
        box_height = box[3] # box eni ve boyu
                    
        predicted_id = ids_list[max_class_id] # label yazmak için max_classı kullandık
        label = labels[predicted_id] # ilgili labelı yukardan uygun şekilde çektik
        confidence = confidences_list[max_class_id] # confidence oranı sağlam olanı aldık
                



#%% non-maximum supression : operation 3 end
            
        end_x = start_x + box_width
        end_y = start_y + box_height
            
        # renk verelim
        box_color = colors[predicted_id]
        box_color = [int(each) for each in box_color]
        
        # formatlama yaptık, daha güzel görünecek
        label = "{}: {:.2f}%".format(label, confidence * 100)
        print ("predicted object {}".format(label))
            
            
        # kutuyla ilgili tüm parametreler hazır. çizim başlıyor :
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), box_color, 1)
        cv2.putText(img, label, (start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color,1)


#%%

cv2.imshow("Detection Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
non-maximum supression ile yüzde 30 gibi kötü değerleri yok ettik. 
yani bu kodlar öncekine göre daha sağlam.

"""





