# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentsdb.ui'
#
# Created: Thu Nov 30 12:15:40 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Table_view  import table
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

class Ui_Form(object):
    def studentdb(self):
        self.student = QtGui.QMainWindow()
        self.ui = table()
        self.ui.setupUi(self.student)
        self.student.show()

    def studb(self):
        from Table_2 import table
        print(" Sign Up Button Clicked !")
        self.signUpWindow = QtGui.QDialog()
        self.ui = table()





    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(389, 208)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 351, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 120, 351, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", "Students", None))
        self.pushButton_3.setText(_translate("Form", "Students Time", None))
        ########################################################
        self.pushButton_3.clicked.connect(self.studentdb)

        ###################################################

        ########################################################
        self.pushButton_2.clicked.connect(self.studb)

        ###################################################


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

