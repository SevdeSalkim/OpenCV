import os 
import cv2
# read image
image_path = os.path.join('.','ikon-but-you-mv-teaser-flashback.jpeg')
img = cv2.imread(image_path)


# write image
cv2.imwrite(os.path.join('.','data','ikon-but-you-out.jpeg'),img)
# visualize image 
cv2.imshow('image', img)
cv2.waitKey(0) # bekleme anahtarı ; yani 0 yerine 5000 yazsaydık image açıldıktan 5 sn sonra kendiliğinden kapanacktı.
#cv2.waitKey(5000)

#İmage Resize
resize_img = cv2.resize(img , (540,350))
print(img.shape)
print(resize_img.shape)
cv2.imshow('img', img)
cv2.imshow('resize_img',resize_img)
cv2.waitKey(0)


# İmage Cropped
cropped_img = img[320:640 , 950:1250] # ilk kısım yükseklik boyutu için , ikinci kısım genişlik boyutu için girilir
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)








