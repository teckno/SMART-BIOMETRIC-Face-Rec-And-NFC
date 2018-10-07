import cv2
import numpy as np
import sqlite3
import datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class facelive(object):
	
	
		recognizer = cv2.createLBPHFaceRecognizer()
		recognizer.load('recognizer/trainingData.yml')
		cascadePath = "haarcascade_frontalface_default.xml"
		faceCascade = cv2.CascadeClassifier(cascadePath);
		path='dataset'

		de=datetime.datetime.now()


		def getProfile(id):
			conn=sqlite3.connect("Photogeniks.db")
			cmd="SELECT * FROM People WHERE ID="+str(id)
			cursor=conn.execute(cmd)
			profile=None
			for row in cursor:
				profile=row
			conn.close()
			return profile



		cam = cv2.VideoCapture(0)


		font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
		while True:
			ret, im =cam.read()
			#im = cv2.imread(filename)
			gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
			faces=faceCascade.detectMultiScale(gray, 1.2,5)
			for(x,y,w,h) in faces:
				cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
				id, conf = recognizer.predict(gray[y:y+h,x:x+w])
				profile = getProfile(id)
				if(profile!=None):
					#cv2.cv.PutText(cv2.cv.fromarray(im),str(id),(x+y+h),font,255)
					
					
					a=id
					b=datetime.datetime.now()
					c='in'

					cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[1]),(x,y+h+30),font,255)
					cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[2]),(x,y+h+60),font,255)
					cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[3]),(x,y+h+90),font,255)
					cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[4]),(x,y+h+120),font,255)

					conn = sqlite3.connect('timer.db')

					conn.execute("INSERT INTO Attend (Id,date,time,status) VALUES (?,?,?,?)",(a,b,de,c));
					conn.commit()
					
					print "Records created successfully";
					#showdialog();
				   
					conn.close()
					break


					


					

					#draw text
				   # cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[2]),(x+y+h+60),font,255)#draw text
					#cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[3]),(x+y+h+90),font,255)#draw text
					#cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[4]),(x+y+h+120),font,255)#draw text
			 
				
			cv2.imshow('PhotoGeniks',im) 
			if cv2.waitKey(10) & 0xFF==ord('q'):
				break
		cam.release()
		cv2.destroyAllWindows()




