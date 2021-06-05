import cv2

eyecascade = cv2.CascadeClassifier('haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Elon1.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eyes = eyecascade.detectMultiScale(gray,1.1,4)
faces = facecascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in eyes :
    cv2.rectangle(img,(x,y),(x+w,y+h),(21,21,237),2)
for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(42,237,42),2)

cv2.imshow('img',img)
cv2.waitKey()
