# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'In_Progress.ui'
#
# Created: Sat Oct 28 10:02:28 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import numpy as np
import cv2
import sqlite3
import os
from trainer2 import dataset

from PIL import Image
import subprocess

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

class Progress_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(261, 66)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(-20, -20, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_6.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#0055ff;\">In Progress</span></p></body></html>", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Progress_Form()
    ui.setupUi(Form)

    Form.show()
    from trainer2 import dataset

    sys.exit(app.exec_())

