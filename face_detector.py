# pip install opencv-python
# haarcascade_frontalface_default.xml

import cv2

a= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

b = cv2.VideoCapture(0)

while True:
    c_rectangale,d_image = b.read()
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3,6)

    for(x1,y1,w1,h1) in f:
        cv2.rectangle(d_image, (x1,y1), (x1+w1, y1+h1), (255,0,0), 10)

        cv2.imshow('img', d_image)
        h = cv2.waitKey(50) & 0xff
        if h == 50:
            break
b.release()
cv2.destroyAllWindows()