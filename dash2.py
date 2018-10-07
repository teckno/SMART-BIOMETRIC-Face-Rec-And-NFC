# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created: Thu Nov 23 18:19:21 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
#from Datastore import  database
from face_capture import Ui_Dialog
#from ViewC import view_Camera
#from Users import students
#from Sdb import Ui_Form
#from features2 import Ui_MainWindow

import sqlite3


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

class Ui_MainWindow(object):

    def signUpShow(self):
        self.signUpWindow = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        
    def extrafeatures(self):
        from features2 import Ui_MainWindow
        self.signUpWindow = QtGui.QDialog()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        
    def database(self):
        self.signUpWindow = QtGui.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

    def signUpCheck(self):
        print(" Sign Up Button Clicked !")
        self.signUpShow()

    def datastore_show(self):
        from facer12 import facelive
        self.signUpWindow = QtGui.QDialog()
        self.ui = facelive()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

    def dastastoreCheck(self):
        print(" Sign Up Button Clicked !")
        self.datastore_show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(389, 520)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(40, 100, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        self.toolButton.clicked.connect(self.signUpCheck)





        self.toolButton.setFont(font)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))


        
        self.toolButton_2 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(40, 160, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)

        
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(40, 320, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_3.clicked.connect(self.database)

        
        self.toolButton_5 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(40, 440, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(13)


        ########################################################
        self.toolButton_2.clicked.connect(self.dastastoreCheck)

        ###################################################






        self.toolButton_5.setFont(font)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        

        
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, -20, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton_4 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(40, 240, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_4.setFont(font)
        
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_6 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(40, 380, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_6.setFont(font)
        
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.toolButton_6.clicked.connect(self.extrafeatures)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Photogeniks", "PhotoGeniks", None))
        self.toolButton.setText(_translate("MainWindow", "Face Registration", None))
        self.toolButton_2.setText(_translate("MainWindow", "Face Real Time Recognition", None))
        self.toolButton_3.setText(_translate("MainWindow", "Databases", None))
        self.toolButton_5.setText(_translate("MainWindow", "logout", None))
        self.label_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0055ff; vertical-align:sub;\">Photogeniks</span></p></body></html>", None))
        self.toolButton_4.setText(_translate("MainWindow", "NFC Recognition", None))
        self.toolButton_6.setText(_translate("MainWindow", "Extra Features", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

