# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created: Mon Oct 23 19:59:57 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from signup4 import  Ui_signUp
from dash2 import Ui_MainWindow
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

class Ui_Dialog(object):
    def showMessageBox(self, title, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def welcomeWindowShow(self):
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    def signUpShow(self):
        self.signUpWindow = QtGui.QDialog()
        self.ui = Ui_signUp()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()


    def loginCheck(self):
        conn = sqlite3.connect('stande.db')

        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()

        b=str(username)
        e=str(password)
        #a="mwape"
        #c="freedom247"

        cursor =conn.execute("SELECT * FROM admin WHERE fname =? AND password = ?",(b,e))
        if (len(cursor.fetchall()) > 0):
            print("User Found ! ")
            self.welcomeWindowShow()
        else:
            print("User Not Found !")
            self.showMessageBox('Warning', 'Invalid Username And Password')
        conne.close()

    def signUpCheck(self):
        print(" Sign Up Button Clicked !")
        self.signUpShow()


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(301, 374)
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(10, 110, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.uname_lineEdit.setFont(font)
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setPlaceholderText('Username')
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))

        self.pass_lineEdit = QtGui.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(10, 150, 271, 31))
        self.pass_lineEdit.setText(_fromUtf8(""))
        self.pass_lineEdit.setEchoMode(QtGui.QLineEdit.Password)

        self.pass_lineEdit.setPlaceholderText('Password')
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(10, 200, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_btn.setFont(font)
        #########################################################

        self.login_btn.clicked.connect(self.loginCheck)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.signup_btn = QtGui.QPushButton(Dialog)



        self.signup_btn.setGeometry(QtCore.QRect(10, 250, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        ####################################################
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.signup_btn.clicked.connect(self.signUpCheck)


        ################################################333


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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PHOTOI", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))
        self.signup_btn.setText(_translate("Dialog", "Sign Up", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0055ff;\">PhotoGeniks</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", " created by techno", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

