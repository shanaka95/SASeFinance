# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        MainWindow.setWindowTitle("Login to Luckview Credit & Investment")
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet(_fromUtf8(""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainframe = QtGui.QFrame(self.centralWidget)
        self.mainframe.setGeometry(QtCore.QRect(390, 260, 541, 231))
        self.mainframe.setStyleSheet(_fromUtf8("\n"
"#mainframe {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}"))
        self.mainframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtGui.QFrame.Raised)
        self.mainframe.setObjectName(_fromUtf8("mainframe"))
        self.lineEdit = QtGui.QLineEdit(self.mainframe)
        self.lineEdit.setGeometry(QtCore.QRect(190, 60, 191, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.mainframe)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 191, 20))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self.mainframe)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 47, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.mainframe)
        self.label_4.setGeometry(QtCore.QRect(130, 100, 51, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.mainframe)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 62, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.mainframe)
        self.label_5.setGeometry(QtCore.QRect(130, 185, 281, 31))
        self.label_5.setStyleSheet(_fromUtf8("color:red;"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 1381, 781))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("background.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(-20, 40, 1361, 221))
        self.frame.setStyleSheet(_fromUtf8("\n"
"     \n"
"    QLabel  {\n"
"color: #564242;\n"
"        font-family: \"Adobe Caslon Pro\", \"Hoefler Text\", Georgia, Garamond, Times, serif;\n"
" letter-spacing:0.1em;\n"
" text-align:center;\n"
" margin: 40px auto;\n"
" text-transform: lowercase;\n"
" line-height: 145%;\n"
" font-size: 50pt;\n"
" font-variant: small-caps;\n"
"        }"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 1401, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Cool Text - Luckview Investment Private Limited 213393981539896.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label.raise_()
        self.mainframe.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Username", None))
        self.label_4.setText(_translate("MainWindow", "Password", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))

