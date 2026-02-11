import cv2

#image read(file name)
img = cv2.imread('img_42.jpg')
#cv2.imshow('result',img)
#print(img)

#converting the image to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img, (x,y), (w,h), (color), borderWidth
cv2.rectangle(img,(20,20),(100,100),(255,0,0),5)
cv2.imwrite('result.jpg',img)

