# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup2.ui'
#
# Created: Wed Oct 11 15:48:02 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def insertData(self):
        username = self.uname_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        connection = sqlite3.connect("login.db")

        cmd = "INSERT INTO USERS(USERNAME,EMAIL,PASSWORD)VALUES(" + str(username) + "," + str(email) + "," + str(
            password) + ")"
        connection.execute(cmd)
        connection.commit()
        connection.close()


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(328, 403)
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(30, 139, 271, 31))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(30, 190, 271, 31))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(30, 239, 271, 41))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(30, 300, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 90, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.signup_btn.setText(_translate("Dialog", "Sign Up", None))
        self.label_4.setText(_translate("Dialog", "Create Account", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0055ff;\">Photogeniks</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

