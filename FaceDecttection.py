import numpy as np
import cv2
import sqlite3
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("Photogeniks.db")
    cmd="SELECT * FROM People Where ID ="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name"+str(Name)+"WHERE ID"+srt(Id)
    else:
        cmd="INSERT INTO People(ID,Name)Values("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()


#filename='FB5.jpg'
cap = cv2.VideoCapture(1)
Id =raw_input("Please enter your ID")
name=raw_input("Please enter your name")


insertOrUpdate(Id,name)
sampleNum=0



while 1:
    ret, img = cap.read()
    #img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
 

        sampleNum=sampleNum+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #saving the captured face in the dataset folder

        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])    

    cv2.imshow('Photogeniks',img)
    k = cv2.waitKey(1)
   
    if sampleNum>20:
        break

cap.release()
cv2.destroyAllWindows()
