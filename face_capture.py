# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture_face.ui'
#
# Created: Fri Oct 27 17:14:13 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

from PyQt4 import QtCore, QtGui
import numpy as np
import cv2
import sqlite3
import os

from PIL import Image
import subprocess

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path='dataset'


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def insertOrUpdate(self):
        Id = self.uname_lineEdit.text()
        Name = self.uname_lineEdit_2.text()

        b = str(Id)
        e = str(Name)

        conn = sqlite3.connect("Photogeniks.db")
    
        conn.execute("INSERT INTO People(ID,Name) \
        VALUES (?,?)",(b,e));
        
    
        conn.commit()
        print ("Records created successfully")
        
        conn.close()
        sampleNum = 0

        cap = cv2.VideoCapture(0)

        while 1:
            ret, img = cap.read()
            # img = cv2.imread(filename)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]

                sampleNum = sampleNum + 1
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # saving the captured face in the dataset folder

                cv2.imwrite("dataSet/Student." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('Photogeniks', img)
            k = cv2.waitKey(1)

            if sampleNum > 20:
                break

        cap.release()
        cv2.destroyAllWindows()
    def signUpShow(self):
        from progress import Progress_Form
        self.signUpWindow = QtGui.QDialog()
        self.ui = Progress_Form()

        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        
    def traindata(self):
        print(" Sign Up Button Clicked !")
        self.signUpShow()
        
        
        





    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(296, 333)
        font = QtGui.QFont()
        font.setPointSize(5)
        Dialog.setFont(font)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(80, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.uname_lineEdit.setFont(font)
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(10, 200, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        #self.login_btn.clicked.connect(self.loginCheck)

        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(10, 250, 271, 41))
        font = QtGui.QFont()

        ######################Button click########################
        self.login_btn.clicked.connect(self.insertOrUpdate)






        ###################### Button click2######################
        self.signup_btn.clicked.connect(self.traindata)





        font.setPointSize(9)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 340, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 51, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 51, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.uname_lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit_2.setGeometry(QtCore.QRect(80, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.uname_lineEdit_2.setFont(font)
        self.uname_lineEdit_2.setText(_fromUtf8(""))
        self.uname_lineEdit_2.setObjectName(_fromUtf8("uname_lineEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PHOTOI", None))
        self.login_btn.setText(_translate("Dialog", "Capture Dataset", None))
        self.signup_btn.setText(_translate("Dialog", "Train Dataset", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0055ff;\">PhotoGeniks</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", " created by techno", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">ID</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Name</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

