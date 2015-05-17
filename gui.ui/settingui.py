# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingui.ui'
#
# Created: Thu Mar 05 20:38:18 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 284)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 291, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit_rootPath = QtGui.QLineEdit(Dialog)
        self.lineEdit_rootPath.setGeometry(QtCore.QRect(60, 50, 291, 21))
        self.lineEdit_rootPath.setObjectName("lineEdit_rootPath")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 72, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Null = QtGui.QLineEdit(Dialog)
        self.lineEdit_Null.setGeometry(QtCore.QRect(60, 160, 291, 21))
        self.lineEdit_Null.setObjectName("lineEdit_Null")
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 110, 379, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "注：默认路径为安装路径下的result文件夹", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "生成图像保存路径", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Null", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Null.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Null is not a error", None, QtGui.QApplication.UnicodeUTF8))

