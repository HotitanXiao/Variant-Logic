# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created: Sun Jan 25 17:50:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 432)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 621, 381))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setAutoFillBackground(True)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabsMovable(False)
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuNIST = QtGui.QMenu(self.menubar)
        self.menuNIST.setObjectName("menuNIST")
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStt = QtGui.QAction(MainWindow)
        self.actionStt.setObjectName("actionStt")
        self.actionSouq = QtGui.QAction(MainWindow)
        self.actionSouq.setObjectName("actionSouq")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionStt)
        self.menu_2.addAction(self.actionSouq)
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuNIST.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "变值逻辑-powerd by H.Y.", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "等待", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "文件", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("MainWindow", "杨辉三角 ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNIST.setTitle(QtGui.QApplication.translate("MainWindow", "NIST测量 ", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_3.setTitle(QtGui.QApplication.translate("MainWindow", "关于", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStt.setText(QtGui.QApplication.translate("MainWindow", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSouq.setText(QtGui.QApplication.translate("MainWindow", "杨辉三角", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

