import cv2
from random import randrange
#importing frontalface
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image
#img=cv2.imread('dr.png')
#img=cv2.imread('two.png')

#for capturing video from webcam
webcam=cv2.VideoCapture(0)

while True:
    #read the current frame
    successful_frame_read,frame=webcam.read()
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect face
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

    for x,y,w,h in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)

    cv2.imshow('FIrst Face detector',frame)
    key=cv2.waitKey(1)
    #ascii for q and Q to quit
    if key==81 or key==113:
        break
webcam.release()


"""
#convert to gray scale for working
#grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#detect face
face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

#displaying rectangle img coordinates
print(face_coordinates)
#draw rectangle               coord x,y   x+w   y+h             color   thickness
for x,y,w,h in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)


#show img
cv2.imshow('FIrst Face detector',img)
#image waits to view it
cv2.waitKey()
print("Working")"""