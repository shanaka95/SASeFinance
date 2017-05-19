# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        MainWindow.setObjectName(_fromUtf8("SASeFinance"))
        MainWindow.resize(1280, 768)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet(_fromUtf8(""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 1280, 768))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;\n"
"}"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("1593643.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 1261, 611))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;\n"
"}"))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tjj = QtGui.QWidget()
        self.tjj.setObjectName(_fromUtf8("tjj"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tjj)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1261, 581))
        self.tabWidget_2.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;\n"
"}"))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.label_21 = QtGui.QLabel(self.tab_11)
        self.label_21.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.tab_11)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(160, 50, 231, 51))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.label_22 = QtGui.QLabel(self.tab_11)
        self.label_22.setGeometry(QtCore.QRect(30, 110, 91, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_11)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 110, 231, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_23 = QtGui.QLabel(self.tab_11)
        self.label_23.setGeometry(QtCore.QRect(30, 140, 131, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_14 = QtGui.QLineEdit(self.tab_11)
        self.lineEdit_14.setGeometry(QtCore.QRect(160, 140, 231, 20))
        self.lineEdit_14.setText(_fromUtf8(""))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_24 = QtGui.QLabel(self.tab_11)
        self.label_24.setGeometry(QtCore.QRect(30, 170, 121, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.plainTextEdit_5 = QtGui.QPlainTextEdit(self.tab_11)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(160, 170, 231, 51))
        self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))
        self.label_25 = QtGui.QLabel(self.tab_11)
        self.label_25.setGeometry(QtCore.QRect(30, 230, 121, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_11)
        self.lineEdit_17.setGeometry(QtCore.QRect(160, 230, 231, 20))
        self.lineEdit_17.setText(_fromUtf8(""))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_11)
        self.lineEdit_18.setGeometry(QtCore.QRect(160, 260, 231, 20))
        self.lineEdit_18.setText(_fromUtf8(""))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.label_26 = QtGui.QLabel(self.tab_11)
        self.label_26.setGeometry(QtCore.QRect(30, 260, 121, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_11)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 470, 171, 41))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(80, 40, 61, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label_30 = QtGui.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(90, 430, 281, 31))
        self.label_30.setStyleSheet(_fromUtf8("color:red;"))
        self.label_30.setText(_fromUtf8(""))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.lineEdit_98 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_98.setGeometry(QtCore.QRect(150, 340, 231, 20))
        self.lineEdit_98.setText(_fromUtf8(""))
        self.lineEdit_98.setObjectName(_fromUtf8("lineEdit_98"))
        self.label_184 = QtGui.QLabel(self.groupBox_3)
        self.label_184.setGeometry(QtCore.QRect(20, 340, 121, 16))
        self.label_184.setObjectName(_fromUtf8("label_184"))
        self.comboBox_15 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_15.setGeometry(QtCore.QRect(80, 370, 61, 22))
        self.comboBox_15.setObjectName(_fromUtf8("comboBox_15"))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.label_185 = QtGui.QLabel(self.groupBox_3)
        self.label_185.setGeometry(QtCore.QRect(20, 370, 61, 16))
        self.label_185.setObjectName(_fromUtf8("label_185"))
        self.plainTextEdit_18 = QtGui.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_18.setGeometry(QtCore.QRect(150, 370, 231, 51))
        self.plainTextEdit_18.setObjectName(_fromUtf8("plainTextEdit_18"))
        self.pushButton_56 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_56.setGeometry(QtCore.QRect(420, 40, 121, 41))
        self.pushButton_56.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_56.setObjectName(_fromUtf8("pushButton_56"))
        self.label_189 = QtGui.QLabel(self.groupBox_3)
        self.label_189.setGeometry(QtCore.QRect(400, 90, 351, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_189.setFont(font)
        self.label_189.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";\n"
"color:blue;"))
        self.label_189.setText(_fromUtf8(""))
        self.label_189.setObjectName(_fromUtf8("label_189"))
        self.pushButton_57 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_57.setGeometry(QtCore.QRect(210, 470, 171, 41))
        self.pushButton_57.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_57.setObjectName(_fromUtf8("pushButton_57"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_11)
        self.groupBox_4.setGeometry(QtCore.QRect(800, 10, 341, 181))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 70, 231, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.plainTextEdit_17 = QtGui.QPlainTextEdit(self.tab_11)
        self.plainTextEdit_17.setGeometry(QtCore.QRect(160, 290, 231, 51))
        self.plainTextEdit_17.setObjectName(_fromUtf8("plainTextEdit_17"))
        self.label_183 = QtGui.QLabel(self.tab_11)
        self.label_183.setGeometry(QtCore.QRect(30, 290, 121, 16))
        self.label_183.setObjectName(_fromUtf8("label_183"))
        self.groupBox_3.raise_()
        self.label_21.raise_()
        self.plainTextEdit_4.raise_()
        self.label_22.raise_()
        self.lineEdit_3.raise_()
        self.label_23.raise_()
        self.lineEdit_14.raise_()
        self.label_24.raise_()
        self.plainTextEdit_5.raise_()
        self.label_25.raise_()
        self.lineEdit_17.raise_()
        self.lineEdit_18.raise_()
        self.label_26.raise_()
        self.groupBox_4.raise_()
        self.plainTextEdit_17.raise_()
        self.label_183.raise_()
        self.tabWidget_2.addTab(self.tab_11, _fromUtf8(""))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        self.plainTextEdit_19 = QtGui.QPlainTextEdit(self.tab_12)
        self.plainTextEdit_19.setGeometry(QtCore.QRect(160, 290, 231, 51))
        self.plainTextEdit_19.setObjectName(_fromUtf8("plainTextEdit_19"))
        self.label_176 = QtGui.QLabel(self.tab_12)
        self.label_176.setGeometry(QtCore.QRect(30, 260, 121, 16))
        self.label_176.setObjectName(_fromUtf8("label_176"))
        self.lineEdit_94 = QtGui.QLineEdit(self.tab_12)
        self.lineEdit_94.setGeometry(QtCore.QRect(160, 230, 231, 20))
        self.lineEdit_94.setText(_fromUtf8(""))
        self.lineEdit_94.setObjectName(_fromUtf8("lineEdit_94"))
        self.plainTextEdit_9 = QtGui.QPlainTextEdit(self.tab_12)
        self.plainTextEdit_9.setEnabled(True)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(160, 50, 231, 51))
        self.plainTextEdit_9.setPlainText(_fromUtf8(""))
        self.plainTextEdit_9.setObjectName(_fromUtf8("plainTextEdit_9"))
        self.groupBox_53 = QtGui.QGroupBox(self.tab_12)
        self.groupBox_53.setGeometry(QtCore.QRect(10, 10, 851, 521))
        self.groupBox_53.setObjectName(_fromUtf8("groupBox_53"))
        self.pushButton_54 = QtGui.QPushButton(self.groupBox_53)
        self.pushButton_54.setGeometry(QtCore.QRect(20, 470, 171, 41))
        self.pushButton_54.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_54.setObjectName(_fromUtf8("pushButton_54"))
        self.comboBox_14 = QtGui.QComboBox(self.groupBox_53)
        self.comboBox_14.setGeometry(QtCore.QRect(80, 40, 61, 22))
        self.comboBox_14.setObjectName(_fromUtf8("comboBox_14"))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.label_177 = QtGui.QLabel(self.groupBox_53)
        self.label_177.setGeometry(QtCore.QRect(90, 280, 281, 31))
        self.label_177.setStyleSheet(_fromUtf8("color:red;"))
        self.label_177.setText(_fromUtf8(""))
        self.label_177.setObjectName(_fromUtf8("label_177"))
        self.lineEdit_99 = QtGui.QLineEdit(self.groupBox_53)
        self.lineEdit_99.setGeometry(QtCore.QRect(150, 340, 231, 20))
        self.lineEdit_99.setText(_fromUtf8(""))
        self.lineEdit_99.setObjectName(_fromUtf8("lineEdit_99"))
        self.label_186 = QtGui.QLabel(self.groupBox_53)
        self.label_186.setGeometry(QtCore.QRect(20, 340, 121, 16))
        self.label_186.setObjectName(_fromUtf8("label_186"))
        self.comboBox_16 = QtGui.QComboBox(self.groupBox_53)
        self.comboBox_16.setGeometry(QtCore.QRect(80, 370, 61, 22))
        self.comboBox_16.setObjectName(_fromUtf8("comboBox_16"))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.label_187 = QtGui.QLabel(self.groupBox_53)
        self.label_187.setGeometry(QtCore.QRect(20, 370, 61, 16))
        self.label_187.setObjectName(_fromUtf8("label_187"))
        self.plainTextEdit_20 = QtGui.QPlainTextEdit(self.groupBox_53)
        self.plainTextEdit_20.setGeometry(QtCore.QRect(150, 370, 231, 51))
        self.plainTextEdit_20.setObjectName(_fromUtf8("plainTextEdit_20"))
        self.label_190 = QtGui.QLabel(self.groupBox_53)
        self.label_190.setGeometry(QtCore.QRect(110, 430, 281, 31))
        self.label_190.setStyleSheet(_fromUtf8("color:red;"))
        self.label_190.setText(_fromUtf8(""))
        self.label_190.setObjectName(_fromUtf8("label_190"))
        self.lineEdit_100 = QtGui.QLineEdit(self.groupBox_53)
        self.lineEdit_100.setGeometry(QtCore.QRect(580, 60, 231, 20))
        self.lineEdit_100.setObjectName(_fromUtf8("lineEdit_100"))
        self.label_191 = QtGui.QLabel(self.groupBox_53)
        self.label_191.setGeometry(QtCore.QRect(450, 60, 121, 16))
        self.label_191.setObjectName(_fromUtf8("label_191"))
        self.comboBox_22 = QtGui.QComboBox(self.groupBox_53)
        self.comboBox_22.setGeometry(QtCore.QRect(580, 30, 101, 22))
        self.comboBox_22.setObjectName(_fromUtf8("comboBox_22"))
        self.comboBox_22.addItem(_fromUtf8(""))
        self.comboBox_22.addItem(_fromUtf8(""))
        self.comboBox_22.addItem(_fromUtf8(""))
        self.pushButton_55 = QtGui.QPushButton(self.groupBox_53)
        self.pushButton_55.setGeometry(QtCore.QRect(210, 470, 171, 41))
        self.pushButton_55.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_55.setObjectName(_fromUtf8("pushButton_55"))
        self.lineEdit_95 = QtGui.QLineEdit(self.tab_12)
        self.lineEdit_95.setGeometry(QtCore.QRect(160, 140, 231, 20))
        self.lineEdit_95.setText(_fromUtf8(""))
        self.lineEdit_95.setObjectName(_fromUtf8("lineEdit_95"))
        self.lineEdit_96 = QtGui.QLineEdit(self.tab_12)
        self.lineEdit_96.setGeometry(QtCore.QRect(160, 110, 231, 20))
        self.lineEdit_96.setText(_fromUtf8(""))
        self.lineEdit_96.setObjectName(_fromUtf8("lineEdit_96"))
        self.label_178 = QtGui.QLabel(self.tab_12)
        self.label_178.setGeometry(QtCore.QRect(30, 230, 121, 16))
        self.label_178.setObjectName(_fromUtf8("label_178"))
        self.label_188 = QtGui.QLabel(self.tab_12)
        self.label_188.setGeometry(QtCore.QRect(30, 290, 121, 16))
        self.label_188.setObjectName(_fromUtf8("label_188"))
        self.lineEdit_97 = QtGui.QLineEdit(self.tab_12)
        self.lineEdit_97.setGeometry(QtCore.QRect(160, 260, 231, 20))
        self.lineEdit_97.setText(_fromUtf8(""))
        self.lineEdit_97.setObjectName(_fromUtf8("lineEdit_97"))
        self.label_179 = QtGui.QLabel(self.tab_12)
        self.label_179.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.label_179.setObjectName(_fromUtf8("label_179"))
        self.label_180 = QtGui.QLabel(self.tab_12)
        self.label_180.setGeometry(QtCore.QRect(30, 170, 121, 16))
        self.label_180.setObjectName(_fromUtf8("label_180"))
        self.label_181 = QtGui.QLabel(self.tab_12)
        self.label_181.setGeometry(QtCore.QRect(30, 110, 91, 16))
        self.label_181.setObjectName(_fromUtf8("label_181"))
        self.plainTextEdit_16 = QtGui.QPlainTextEdit(self.tab_12)
        self.plainTextEdit_16.setGeometry(QtCore.QRect(160, 170, 231, 51))
        self.plainTextEdit_16.setObjectName(_fromUtf8("plainTextEdit_16"))
        self.label_182 = QtGui.QLabel(self.tab_12)
        self.label_182.setGeometry(QtCore.QRect(30, 140, 131, 16))
        self.label_182.setObjectName(_fromUtf8("label_182"))
        self.groupBox_53.raise_()
        self.plainTextEdit_19.raise_()
        self.label_176.raise_()
        self.lineEdit_94.raise_()
        self.plainTextEdit_9.raise_()
        self.lineEdit_95.raise_()
        self.lineEdit_96.raise_()
        self.label_178.raise_()
        self.label_188.raise_()
        self.lineEdit_97.raise_()
        self.label_179.raise_()
        self.label_180.raise_()
        self.label_181.raise_()
        self.plainTextEdit_16.raise_()
        self.label_182.raise_()
        self.tabWidget_2.addTab(self.tab_12, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_10)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 871, 511))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_39 = QtGui.QLabel(self.groupBox_5)
        self.label_39.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.lineEdit_27 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_27.setGeometry(QtCore.QRect(120, 40, 191, 20))
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.label_40 = QtGui.QLabel(self.groupBox_5)
        self.label_40.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.lineEdit_32 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_32.setEnabled(False)
        self.lineEdit_32.setGeometry(QtCore.QRect(120, 180, 151, 20))
        self.lineEdit_32.setText(_fromUtf8(""))
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.lineEdit_33 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_33.setGeometry(QtCore.QRect(120, 210, 151, 20))
        self.lineEdit_33.setText(_fromUtf8(""))
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.label_49 = QtGui.QLabel(self.groupBox_5)
        self.label_49.setGeometry(QtCore.QRect(420, 40, 61, 16))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.plainTextEdit_10 = QtGui.QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_10.setEnabled(False)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(120, 100, 191, 71))
        self.plainTextEdit_10.setPlainText(_fromUtf8(""))
        self.plainTextEdit_10.setObjectName(_fromUtf8("plainTextEdit_10"))
        self.lineEdit_38 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_38.setEnabled(False)
        self.lineEdit_38.setGeometry(QtCore.QRect(490, 40, 191, 20))
        self.lineEdit_38.setText(_fromUtf8(""))
        self.lineEdit_38.setObjectName(_fromUtf8("lineEdit_38"))
        self.lineEdit_39 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_39.setEnabled(False)
        self.lineEdit_39.setGeometry(QtCore.QRect(120, 70, 191, 20))
        self.lineEdit_39.setText(_fromUtf8(""))
        self.lineEdit_39.setObjectName(_fromUtf8("lineEdit_39"))
        self.label_53 = QtGui.QLabel(self.groupBox_5)
        self.label_53.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_54 = QtGui.QLabel(self.groupBox_5)
        self.label_54.setGeometry(QtCore.QRect(10, 210, 91, 16))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.label_55 = QtGui.QLabel(self.groupBox_5)
        self.label_55.setGeometry(QtCore.QRect(10, 180, 91, 16))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.label_56 = QtGui.QLabel(self.groupBox_5)
        self.label_56.setGeometry(QtCore.QRect(10, 240, 91, 16))
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.lineEdit_34 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_34.setEnabled(False)
        self.lineEdit_34.setGeometry(QtCore.QRect(120, 240, 151, 20))
        self.lineEdit_34.setText(_fromUtf8(""))
        self.lineEdit_34.setObjectName(_fromUtf8("lineEdit_34"))
        self.lineEdit_35 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_35.setEnabled(False)
        self.lineEdit_35.setGeometry(QtCore.QRect(120, 270, 151, 20))
        self.lineEdit_35.setText(_fromUtf8(""))
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.label_57 = QtGui.QLabel(self.groupBox_5)
        self.label_57.setGeometry(QtCore.QRect(10, 270, 91, 16))
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.label_41 = QtGui.QLabel(self.groupBox_5)
        self.label_41.setGeometry(QtCore.QRect(10, 340, 81, 16))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.lineEdit_28 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_28.setGeometry(QtCore.QRect(120, 370, 231, 20))
        self.lineEdit_28.setText(_fromUtf8(""))
        self.lineEdit_28.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.lineEdit_29 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_29.setGeometry(QtCore.QRect(120, 340, 231, 20))
        self.lineEdit_29.setText(_fromUtf8(""))
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.label_42 = QtGui.QLabel(self.groupBox_5)
        self.label_42.setGeometry(QtCore.QRect(10, 370, 81, 16))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 440, 171, 41))
        self.pushButton_9.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_31 = QtGui.QLabel(self.groupBox_5)
        self.label_31.setGeometry(QtCore.QRect(60, 400, 281, 31))
        self.label_31.setStyleSheet(_fromUtf8("color:red;"))
        self.label_31.setText(_fromUtf8(""))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_116 = QtGui.QLabel(self.groupBox_5)
        self.label_116.setGeometry(QtCore.QRect(70, 400, 321, 31))
        self.label_116.setStyleSheet(_fromUtf8("color:red;"))
        self.label_116.setText(_fromUtf8(""))
        self.label_116.setObjectName(_fromUtf8("label_116"))
        self.comboBox_23 = QtGui.QComboBox(self.groupBox_5)
        self.comboBox_23.setGeometry(QtCore.QRect(320, 40, 81, 22))
        self.comboBox_23.setObjectName(_fromUtf8("comboBox_23"))
        self.comboBox_23.addItem(_fromUtf8(""))
        self.comboBox_23.addItem(_fromUtf8(""))
        self.comboBox_23.addItem(_fromUtf8(""))
        self.tabWidget_2.addTab(self.tab_10, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.groupBox_40 = QtGui.QGroupBox(self.tab_7)
        self.groupBox_40.setEnabled(True)
        self.groupBox_40.setGeometry(QtCore.QRect(10, 10, 411, 221))
        self.groupBox_40.setObjectName(_fromUtf8("groupBox_40"))
        self.lineEdit_30 = QtGui.QLineEdit(self.groupBox_40)
        self.lineEdit_30.setGeometry(QtCore.QRect(130, 30, 231, 20))
        self.lineEdit_30.setText(_fromUtf8(""))
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.label_117 = QtGui.QLabel(self.groupBox_40)
        self.label_117.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label_117.setObjectName(_fromUtf8("label_117"))
        self.lineEdit_31 = QtGui.QLineEdit(self.groupBox_40)
        self.lineEdit_31.setGeometry(QtCore.QRect(130, 90, 231, 20))
        self.lineEdit_31.setText(_fromUtf8(""))
        self.lineEdit_31.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.label_118 = QtGui.QLabel(self.groupBox_40)
        self.label_118.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_118.setObjectName(_fromUtf8("label_118"))
        self.lineEdit_51 = QtGui.QLineEdit(self.groupBox_40)
        self.lineEdit_51.setGeometry(QtCore.QRect(130, 60, 231, 20))
        self.lineEdit_51.setText(_fromUtf8(""))
        self.lineEdit_51.setObjectName(_fromUtf8("lineEdit_51"))
        self.label_119 = QtGui.QLabel(self.groupBox_40)
        self.label_119.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_119.setObjectName(_fromUtf8("label_119"))
        self.pushButton_43 = QtGui.QPushButton(self.groupBox_40)
        self.pushButton_43.setGeometry(QtCore.QRect(130, 160, 171, 41))
        self.pushButton_43.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_43.setObjectName(_fromUtf8("pushButton_43"))
        self.label_120 = QtGui.QLabel(self.groupBox_40)
        self.label_120.setGeometry(QtCore.QRect(60, 120, 321, 31))
        self.label_120.setStyleSheet(_fromUtf8("color:red;"))
        self.label_120.setText(_fromUtf8(""))
        self.label_120.setObjectName(_fromUtf8("label_120"))
        self.tabWidget_2.addTab(self.tab_7, _fromUtf8(""))
        self.tabWidget.addTab(self.tjj, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.frame = QtGui.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 581))
        self.frame.setStyleSheet(_fromUtf8("\n"
"\n"
"\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 611, 551))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(390, 20, 191, 20))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 20, 191, 20))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 190, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(420, 190, 191, 51))
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 190, 151, 20))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 280, 101, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 91, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 181, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 340, 91, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 460, 91, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 430, 91, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 400, 91, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 250, 151, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 370, 151, 20))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 340, 151, 20))
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 310, 151, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 280, 151, 20))
        self.lineEdit_9.setText(_fromUtf8(""))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 490, 151, 20))
        self.lineEdit_10.setText(_fromUtf8(""))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 460, 151, 20))
        self.lineEdit_11.setText(_fromUtf8(""))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 430, 151, 20))
        self.lineEdit_12.setText(_fromUtf8(""))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 400, 151, 20))
        self.lineEdit_13.setText(_fromUtf8(""))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(310, 160, 101, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 220, 91, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(10, 490, 91, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 520, 91, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_15.setEnabled(False)
        self.lineEdit_15.setGeometry(QtCore.QRect(120, 520, 151, 20))
        self.lineEdit_15.setText(_fromUtf8(""))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(390, 500, 171, 41))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(310, 20, 61, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(80, 50, 191, 51))
        self.plainTextEdit_2.setPlainText(_fromUtf8(""))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 130, 81, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_5 = QtGui.QComboBox(self.groupBox)
        self.comboBox_5.setGeometry(QtCore.QRect(420, 160, 51, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.lineEdit_19 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_19.setEnabled(False)
        self.lineEdit_19.setGeometry(QtCore.QRect(120, 220, 151, 20))
        self.lineEdit_19.setText(_fromUtf8(""))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.label_32 = QtGui.QLabel(self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(270, 340, 91, 21))
        self.label_32.setStyleSheet(_fromUtf8("color:blue;"))
        self.label_32.setText(_fromUtf8(""))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(30, 100, 281, 21))
        self.label_33.setStyleSheet(_fromUtf8("color:red;"))
        self.label_33.setText(_fromUtf8(""))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(350, 410, 251, 31))
        self.label_34.setStyleSheet(_fromUtf8("color:red;"))
        self.label_34.setText(_fromUtf8(""))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.comboBox_6 = QtGui.QComboBox(self.groupBox)
        self.comboBox_6.setGeometry(QtCore.QRect(120, 160, 81, 22))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.pushButton_58 = QtGui.QPushButton(self.groupBox)
        self.pushButton_58.setGeometry(QtCore.QRect(390, 450, 171, 41))
        self.pushButton_58.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_58.setObjectName(_fromUtf8("pushButton_58"))
        self.label_155 = QtGui.QLabel(self.groupBox)
        self.label_155.setGeometry(QtCore.QRect(310, 250, 91, 16))
        self.label_155.setObjectName(_fromUtf8("label_155"))
        self.lineEdit_26 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_26.setGeometry(QtCore.QRect(420, 250, 151, 20))
        self.lineEdit_26.setText(_fromUtf8(""))
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(720, 20, 461, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 70, 231, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab)
        self.tabWidget_3.setGeometry(QtCore.QRect(-4, -1, 1271, 591))
        self.tabWidget_3.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"    QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        self.groupBox_13 = QtGui.QGroupBox(self.tab_20)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 10, 821, 531))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.label_64 = QtGui.QLabel(self.groupBox_13)
        self.label_64.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.label_65 = QtGui.QLabel(self.groupBox_13)
        self.label_65.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.label_66 = QtGui.QLabel(self.groupBox_13)
        self.label_66.setGeometry(QtCore.QRect(10, 180, 81, 16))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.label_67 = QtGui.QLabel(self.groupBox_13)
        self.label_67.setGeometry(QtCore.QRect(10, 250, 81, 16))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.lineEdit_54 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_54.setEnabled(True)
        self.lineEdit_54.setGeometry(QtCore.QRect(130, 250, 231, 20))
        self.lineEdit_54.setText(_fromUtf8(""))
        self.lineEdit_54.setObjectName(_fromUtf8("lineEdit_54"))
        self.label_68 = QtGui.QLabel(self.groupBox_13)
        self.label_68.setGeometry(QtCore.QRect(10, 280, 81, 16))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.lineEdit_55 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_55.setEnabled(False)
        self.lineEdit_55.setGeometry(QtCore.QRect(130, 280, 231, 20))
        self.lineEdit_55.setText(_fromUtf8(""))
        self.lineEdit_55.setObjectName(_fromUtf8("lineEdit_55"))
        self.label_69 = QtGui.QLabel(self.groupBox_13)
        self.label_69.setGeometry(QtCore.QRect(10, 310, 111, 16))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.lineEdit_56 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_56.setGeometry(QtCore.QRect(130, 310, 231, 20))
        self.lineEdit_56.setText(_fromUtf8(""))
        self.lineEdit_56.setObjectName(_fromUtf8("lineEdit_56"))
        self.label_70 = QtGui.QLabel(self.groupBox_13)
        self.label_70.setGeometry(QtCore.QRect(10, 340, 101, 16))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.lineEdit_57 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_57.setGeometry(QtCore.QRect(130, 340, 231, 20))
        self.lineEdit_57.setText(_fromUtf8(""))
        self.lineEdit_57.setObjectName(_fromUtf8("lineEdit_57"))
        self.label_71 = QtGui.QLabel(self.groupBox_13)
        self.label_71.setGeometry(QtCore.QRect(10, 400, 81, 16))
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.lineEdit_58 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_58.setGeometry(QtCore.QRect(130, 400, 231, 20))
        self.lineEdit_58.setText(_fromUtf8(""))
        self.lineEdit_58.setObjectName(_fromUtf8("lineEdit_58"))
        self.label_72 = QtGui.QLabel(self.groupBox_13)
        self.label_72.setGeometry(QtCore.QRect(10, 430, 81, 16))
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.lineEdit_59 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_59.setGeometry(QtCore.QRect(130, 430, 231, 20))
        self.lineEdit_59.setText(_fromUtf8(""))
        self.lineEdit_59.setObjectName(_fromUtf8("lineEdit_59"))
        self.label_73 = QtGui.QLabel(self.groupBox_13)
        self.label_73.setGeometry(QtCore.QRect(10, 490, 101, 16))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.lineEdit_60 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_60.setEnabled(False)
        self.lineEdit_60.setGeometry(QtCore.QRect(130, 490, 231, 20))
        self.lineEdit_60.setText(_fromUtf8(""))
        self.lineEdit_60.setObjectName(_fromUtf8("lineEdit_60"))
        self.label_74 = QtGui.QLabel(self.groupBox_13)
        self.label_74.setGeometry(QtCore.QRect(10, 460, 81, 16))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.lineEdit_61 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_61.setGeometry(QtCore.QRect(130, 460, 231, 20))
        self.lineEdit_61.setText(_fromUtf8(""))
        self.lineEdit_61.setObjectName(_fromUtf8("lineEdit_61"))
        self.label_75 = QtGui.QLabel(self.groupBox_13)
        self.label_75.setGeometry(QtCore.QRect(420, 50, 81, 16))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.lineEdit_62 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_62.setGeometry(QtCore.QRect(540, 50, 231, 20))
        self.lineEdit_62.setText(_fromUtf8(""))
        self.lineEdit_62.setObjectName(_fromUtf8("lineEdit_62"))
        self.label_76 = QtGui.QLabel(self.groupBox_13)
        self.label_76.setGeometry(QtCore.QRect(420, 20, 81, 16))
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.lineEdit_63 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_63.setEnabled(False)
        self.lineEdit_63.setGeometry(QtCore.QRect(540, 20, 231, 20))
        self.lineEdit_63.setText(_fromUtf8(""))
        self.lineEdit_63.setObjectName(_fromUtf8("lineEdit_63"))
        self.label_77 = QtGui.QLabel(self.groupBox_13)
        self.label_77.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.lineEdit_64 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_64.setGeometry(QtCore.QRect(130, 50, 231, 20))
        self.lineEdit_64.setObjectName(_fromUtf8("lineEdit_64"))
        self.plainTextEdit_12 = QtGui.QPlainTextEdit(self.groupBox_13)
        self.plainTextEdit_12.setEnabled(False)
        self.plainTextEdit_12.setGeometry(QtCore.QRect(130, 110, 231, 61))
        self.plainTextEdit_12.setPlainText(_fromUtf8(""))
        self.plainTextEdit_12.setObjectName(_fromUtf8("plainTextEdit_12"))
        self.plainTextEdit_13 = QtGui.QPlainTextEdit(self.groupBox_13)
        self.plainTextEdit_13.setEnabled(False)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(130, 180, 231, 61))
        self.plainTextEdit_13.setPlainText(_fromUtf8(""))
        self.plainTextEdit_13.setObjectName(_fromUtf8("plainTextEdit_13"))
        self.label_78 = QtGui.QLabel(self.groupBox_13)
        self.label_78.setGeometry(QtCore.QRect(420, 80, 81, 16))
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.lineEdit_65 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_65.setEnabled(False)
        self.lineEdit_65.setGeometry(QtCore.QRect(540, 80, 231, 20))
        self.lineEdit_65.setText(_fromUtf8(""))
        self.lineEdit_65.setObjectName(_fromUtf8("lineEdit_65"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_13)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 470, 171, 41))
        self.pushButton_11.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.dateEdit_19 = QtGui.QDateEdit(self.groupBox_13)
        self.dateEdit_19.setGeometry(QtCore.QRect(130, 20, 110, 22))
        self.dateEdit_19.setObjectName(_fromUtf8("dateEdit_19"))
        self.pushButton_39 = QtGui.QPushButton(self.groupBox_13)
        self.pushButton_39.setGeometry(QtCore.QRect(580, 420, 171, 41))
        self.pushButton_39.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.label_35 = QtGui.QLabel(self.groupBox_13)
        self.label_35.setGeometry(QtCore.QRect(530, 320, 271, 31))
        self.label_35.setStyleSheet(_fromUtf8("color:red;"))
        self.label_35.setText(_fromUtf8(""))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.groupBox_13)
        self.label_36.setGeometry(QtCore.QRect(110, 80, 271, 21))
        self.label_36.setStyleSheet(_fromUtf8("color:red;"))
        self.label_36.setText(_fromUtf8(""))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.comboBox_17 = QtGui.QComboBox(self.groupBox_13)
        self.comboBox_17.setGeometry(QtCore.QRect(250, 20, 111, 22))
        self.comboBox_17.setObjectName(_fromUtf8("comboBox_17"))
        self.comboBox_17.addItem(_fromUtf8(""))
        self.comboBox_17.addItem(_fromUtf8(""))
        self.comboBox_17.addItem(_fromUtf8(""))
        self.pushButton_61 = QtGui.QPushButton(self.groupBox_13)
        self.pushButton_61.setGeometry(QtCore.QRect(580, 370, 171, 41))
        self.pushButton_61.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_61.setObjectName(_fromUtf8("pushButton_61"))
        self.label_96 = QtGui.QLabel(self.groupBox_13)
        self.label_96.setGeometry(QtCore.QRect(80, 490, 271, 31))
        self.label_96.setStyleSheet(_fromUtf8("color:red;"))
        self.label_96.setText(_fromUtf8(""))
        self.label_96.setObjectName(_fromUtf8("label_96"))
        self.label_150 = QtGui.QLabel(self.groupBox_13)
        self.label_150.setGeometry(QtCore.QRect(10, 370, 101, 16))
        self.label_150.setObjectName(_fromUtf8("label_150"))
        self.lineEdit_75 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_75.setGeometry(QtCore.QRect(130, 370, 231, 20))
        self.lineEdit_75.setText(_fromUtf8(""))
        self.lineEdit_75.setObjectName(_fromUtf8("lineEdit_75"))
        self.label_152 = QtGui.QLabel(self.groupBox_13)
        self.label_152.setGeometry(QtCore.QRect(420, 240, 111, 20))
        self.label_152.setStyleSheet(_fromUtf8("color:Blue"))
        self.label_152.setObjectName(_fromUtf8("label_152"))
        self.listWidget = QtGui.QListWidget(self.groupBox_13)
        self.listWidget.setGeometry(QtCore.QRect(540, 110, 231, 121))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_156 = QtGui.QLabel(self.groupBox_13)
        self.label_156.setGeometry(QtCore.QRect(420, 110, 81, 16))
        self.label_156.setStyleSheet(_fromUtf8("color :blue"))
        self.label_156.setObjectName(_fromUtf8("label_156"))
        self.label_157 = QtGui.QLabel(self.groupBox_13)
        self.label_157.setGeometry(QtCore.QRect(420, 270, 111, 20))
        self.label_157.setStyleSheet(_fromUtf8("color:Blue"))
        self.label_157.setObjectName(_fromUtf8("label_157"))
        self.label_158 = QtGui.QLabel(self.groupBox_13)
        self.label_158.setGeometry(QtCore.QRect(540, 270, 231, 21))
        self.label_158.setStyleSheet(_fromUtf8("color:red"))
        self.label_158.setText(_fromUtf8(""))
        self.label_158.setObjectName(_fromUtf8("label_158"))
        self.lineEdit_80 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_80.setEnabled(False)
        self.lineEdit_80.setGeometry(QtCore.QRect(540, 240, 231, 20))
        self.lineEdit_80.setText(_fromUtf8(""))
        self.lineEdit_80.setObjectName(_fromUtf8("lineEdit_80"))
        self.lineEdit_81 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_81.setEnabled(False)
        self.lineEdit_81.setGeometry(QtCore.QRect(540, 270, 231, 20))
        self.lineEdit_81.setText(_fromUtf8(""))
        self.lineEdit_81.setObjectName(_fromUtf8("lineEdit_81"))
        self.tabWidget_3.addTab(self.tab_20, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 10, 1041, 521))
        self.groupBox_12.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit {    \n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.label_43 = QtGui.QLabel(self.groupBox_12)
        self.label_43.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_44 = QtGui.QLabel(self.groupBox_12)
        self.label_44.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.lineEdit_36 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_36.setEnabled(False)
        self.lineEdit_36.setGeometry(QtCore.QRect(130, 220, 231, 20))
        self.lineEdit_36.setText(_fromUtf8(""))
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.label_45 = QtGui.QLabel(self.groupBox_12)
        self.label_45.setGeometry(QtCore.QRect(10, 190, 81, 16))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_46 = QtGui.QLabel(self.groupBox_12)
        self.label_46.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.lineEdit_40 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_40.setEnabled(False)
        self.lineEdit_40.setGeometry(QtCore.QRect(130, 190, 231, 20))
        self.lineEdit_40.setText(_fromUtf8(""))
        self.lineEdit_40.setObjectName(_fromUtf8("lineEdit_40"))
        self.label_47 = QtGui.QLabel(self.groupBox_12)
        self.label_47.setGeometry(QtCore.QRect(10, 280, 81, 16))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.lineEdit_41 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_41.setEnabled(False)
        self.lineEdit_41.setGeometry(QtCore.QRect(130, 280, 231, 20))
        self.lineEdit_41.setText(_fromUtf8(""))
        self.lineEdit_41.setObjectName(_fromUtf8("lineEdit_41"))
        self.label_48 = QtGui.QLabel(self.groupBox_12)
        self.label_48.setGeometry(QtCore.QRect(10, 250, 81, 16))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.lineEdit_42 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_42.setGeometry(QtCore.QRect(130, 250, 231, 20))
        self.lineEdit_42.setText(_fromUtf8(""))
        self.lineEdit_42.setObjectName(_fromUtf8("lineEdit_42"))
        self.label_50 = QtGui.QLabel(self.groupBox_12)
        self.label_50.setGeometry(QtCore.QRect(10, 220, 81, 16))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.lineEdit_43 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_43.setGeometry(QtCore.QRect(130, 20, 151, 20))
        self.lineEdit_43.setObjectName(_fromUtf8("lineEdit_43"))
        self.label_51 = QtGui.QLabel(self.groupBox_12)
        self.label_51.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.plainTextEdit_11 = QtGui.QPlainTextEdit(self.groupBox_12)
        self.plainTextEdit_11.setEnabled(False)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(130, 140, 231, 41))
        self.plainTextEdit_11.setObjectName(_fromUtf8("plainTextEdit_11"))
        self.lineEdit_44 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_44.setEnabled(False)
        self.lineEdit_44.setGeometry(QtCore.QRect(130, 310, 231, 20))
        self.lineEdit_44.setText(_fromUtf8(""))
        self.lineEdit_44.setObjectName(_fromUtf8("lineEdit_44"))
        self.label_52 = QtGui.QLabel(self.groupBox_12)
        self.label_52.setGeometry(QtCore.QRect(10, 310, 81, 16))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.lineEdit_45 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_45.setEnabled(False)
        self.lineEdit_45.setGeometry(QtCore.QRect(130, 340, 231, 20))
        self.lineEdit_45.setText(_fromUtf8(""))
        self.lineEdit_45.setObjectName(_fromUtf8("lineEdit_45"))
        self.label_58 = QtGui.QLabel(self.groupBox_12)
        self.label_58.setGeometry(QtCore.QRect(10, 400, 91, 16))
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.lineEdit_46 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_46.setEnabled(False)
        self.lineEdit_46.setGeometry(QtCore.QRect(130, 460, 231, 20))
        self.lineEdit_46.setText(_fromUtf8(""))
        self.lineEdit_46.setObjectName(_fromUtf8("lineEdit_46"))
        self.label_59 = QtGui.QLabel(self.groupBox_12)
        self.label_59.setGeometry(QtCore.QRect(10, 460, 81, 16))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.lineEdit_47 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_47.setEnabled(False)
        self.lineEdit_47.setGeometry(QtCore.QRect(130, 430, 231, 20))
        self.lineEdit_47.setText(_fromUtf8(""))
        self.lineEdit_47.setObjectName(_fromUtf8("lineEdit_47"))
        self.label_60 = QtGui.QLabel(self.groupBox_12)
        self.label_60.setGeometry(QtCore.QRect(10, 430, 101, 16))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.lineEdit_48 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_48.setEnabled(False)
        self.lineEdit_48.setGeometry(QtCore.QRect(130, 400, 231, 20))
        self.lineEdit_48.setText(_fromUtf8(""))
        self.lineEdit_48.setObjectName(_fromUtf8("lineEdit_48"))
        self.label_61 = QtGui.QLabel(self.groupBox_12)
        self.label_61.setGeometry(QtCore.QRect(10, 370, 81, 16))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.lineEdit_49 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_49.setEnabled(False)
        self.lineEdit_49.setGeometry(QtCore.QRect(130, 370, 231, 20))
        self.lineEdit_49.setText(_fromUtf8(""))
        self.lineEdit_49.setObjectName(_fromUtf8("lineEdit_49"))
        self.label_62 = QtGui.QLabel(self.groupBox_12)
        self.label_62.setGeometry(QtCore.QRect(10, 340, 81, 16))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.label_63 = QtGui.QLabel(self.groupBox_12)
        self.label_63.setGeometry(QtCore.QRect(10, 490, 81, 16))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.lineEdit_50 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_50.setEnabled(False)
        self.lineEdit_50.setGeometry(QtCore.QRect(130, 490, 231, 20))
        self.lineEdit_50.setText(_fromUtf8(""))
        self.lineEdit_50.setObjectName(_fromUtf8("lineEdit_50"))
        self.tableWidget_2 = QtGui.QTableWidget(self.groupBox_12)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(400, 20, 561, 351))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_10.setGeometry(QtCore.QRect(400, 410, 171, 41))
        self.pushButton_10.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.dateEdit_20 = QtGui.QDateEdit(self.groupBox_12)
        self.dateEdit_20.setEnabled(True)
        self.dateEdit_20.setGeometry(QtCore.QRect(130, 70, 110, 22))
        self.dateEdit_20.setObjectName(_fromUtf8("dateEdit_20"))
        self.label_37 = QtGui.QLabel(self.groupBox_12)
        self.label_37.setGeometry(QtCore.QRect(100, 40, 271, 21))
        self.label_37.setStyleSheet(_fromUtf8("color:red;"))
        self.label_37.setText(_fromUtf8(""))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.plainTextEdit_14 = QtGui.QPlainTextEdit(self.groupBox_12)
        self.plainTextEdit_14.setEnabled(False)
        self.plainTextEdit_14.setGeometry(QtCore.QRect(130, 100, 231, 31))
        self.plainTextEdit_14.setObjectName(_fromUtf8("plainTextEdit_14"))
        self.comboBox_18 = QtGui.QComboBox(self.groupBox_12)
        self.comboBox_18.setGeometry(QtCore.QRect(290, 20, 71, 22))
        self.comboBox_18.setObjectName(_fromUtf8("comboBox_18"))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.tabWidget_3.addTab(self.tab_3, _fromUtf8(""))
        self.tab_17 = QtGui.QWidget()
        self.tab_17.setObjectName(_fromUtf8("tab_17"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_17)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 10, 1241, 531))
        self.groupBox_11.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit {    \n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.comboBox_7 = QtGui.QComboBox(self.groupBox_11)
        self.comboBox_7.setGeometry(QtCore.QRect(90, 40, 171, 22))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.label_94 = QtGui.QLabel(self.groupBox_11)
        self.label_94.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_94.setObjectName(_fromUtf8("label_94"))
        self.lineEdit_20 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_20.setGeometry(QtCore.QRect(280, 40, 351, 20))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.pushButton_40 = QtGui.QPushButton(self.groupBox_11)
        self.pushButton_40.setGeometry(QtCore.QRect(670, 20, 161, 41))
        self.pushButton_40.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_40.setObjectName(_fromUtf8("pushButton_40"))
        self.tableWidget_17 = QtGui.QTableWidget(self.groupBox_11)
        self.tableWidget_17.setGeometry(QtCore.QRect(20, 100, 831, 201))
        self.tableWidget_17.setObjectName(_fromUtf8("tableWidget_17"))
        self.tableWidget_17.setColumnCount(8)
        self.tableWidget_17.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(7, item)
        self.tableWidget_19 = QtGui.QTableWidget(self.groupBox_11)
        self.tableWidget_19.setGeometry(QtCore.QRect(20, 330, 1211, 191))
        self.tableWidget_19.setObjectName(_fromUtf8("tableWidget_19"))
        self.tableWidget_19.setColumnCount(11)
        self.tableWidget_19.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(10, item)
        self.label_95 = QtGui.QLabel(self.groupBox_11)
        self.label_95.setGeometry(QtCore.QRect(280, 70, 491, 21))
        self.label_95.setStyleSheet(_fromUtf8("color:red;"))
        self.label_95.setText(_fromUtf8(""))
        self.label_95.setObjectName(_fromUtf8("label_95"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.groupBox_11)
        self.commandLinkButton_2.setEnabled(False)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(1041, 270, 181, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.tabWidget_3.addTab(self.tab_17, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_14 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 10, 701, 501))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.tableWidget_3 = QtGui.QTableWidget(self.groupBox_14)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 30, 661, 451))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.groupBox_15 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_15.setGeometry(QtCore.QRect(740, 10, 431, 201))
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_15)
        self.pushButton_12.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_12.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.tabWidget_3.addTab(self.tab_4, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        self.groupBox_16 = QtGui.QGroupBox(self.tab_19)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 10, 551, 521))
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.dateEdit = QtGui.QDateEdit(self.groupBox_16)
        self.dateEdit.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_79 = QtGui.QLabel(self.groupBox_16)
        self.label_79.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.label_80 = QtGui.QLabel(self.groupBox_16)
        self.label_80.setGeometry(QtCore.QRect(220, 30, 31, 16))
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.dateEdit_2 = QtGui.QDateEdit(self.groupBox_16)
        self.dateEdit_2.setGeometry(QtCore.QRect(250, 30, 110, 22))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.pushButton_13 = QtGui.QPushButton(self.groupBox_16)
        self.pushButton_13.setGeometry(QtCore.QRect(200, 70, 161, 41))
        self.pushButton_13.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.tableWidget_4 = QtGui.QTableWidget(self.groupBox_16)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 130, 521, 371))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.comboBox_8 = QtGui.QComboBox(self.groupBox_16)
        self.comboBox_8.setGeometry(QtCore.QRect(70, 80, 111, 22))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.groupBox_17 = QtGui.QGroupBox(self.tab_19)
        self.groupBox_17.setGeometry(QtCore.QRect(580, 10, 431, 201))
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.pushButton_14 = QtGui.QPushButton(self.groupBox_17)
        self.pushButton_14.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_14.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.tabWidget_3.addTab(self.tab_19, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.groupBox_18 = QtGui.QGroupBox(self.tab_9)
        self.groupBox_18.setGeometry(QtCore.QRect(10, 10, 551, 521))
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.dateEdit_3 = QtGui.QDateEdit(self.groupBox_18)
        self.dateEdit_3.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setObjectName(_fromUtf8("dateEdit_3"))
        self.label_81 = QtGui.QLabel(self.groupBox_18)
        self.label_81.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.label_82 = QtGui.QLabel(self.groupBox_18)
        self.label_82.setGeometry(QtCore.QRect(220, 30, 31, 16))
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.dateEdit_4 = QtGui.QDateEdit(self.groupBox_18)
        self.dateEdit_4.setGeometry(QtCore.QRect(250, 30, 110, 22))
        self.dateEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_4.setObjectName(_fromUtf8("dateEdit_4"))
        self.pushButton_15 = QtGui.QPushButton(self.groupBox_18)
        self.pushButton_15.setGeometry(QtCore.QRect(200, 70, 161, 41))
        self.pushButton_15.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.tableWidget_5 = QtGui.QTableWidget(self.groupBox_18)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 130, 511, 371))
        self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        self.comboBox_9 = QtGui.QComboBox(self.groupBox_18)
        self.comboBox_9.setGeometry(QtCore.QRect(70, 80, 111, 22))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.groupBox_19 = QtGui.QGroupBox(self.tab_9)
        self.groupBox_19.setGeometry(QtCore.QRect(580, 10, 431, 201))
        self.groupBox_19.setObjectName(_fromUtf8("groupBox_19"))
        self.pushButton_16 = QtGui.QPushButton(self.groupBox_19)
        self.pushButton_16.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_16.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.tabWidget_3.addTab(self.tab_9, _fromUtf8(""))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        self.groupBox_20 = QtGui.QGroupBox(self.tab_21)
        self.groupBox_20.setGeometry(QtCore.QRect(10, 10, 681, 521))
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.dateEdit_5 = QtGui.QDateEdit(self.groupBox_20)
        self.dateEdit_5.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_5.setObjectName(_fromUtf8("dateEdit_5"))
        self.label_83 = QtGui.QLabel(self.groupBox_20)
        self.label_83.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_83.setObjectName(_fromUtf8("label_83"))
        self.label_84 = QtGui.QLabel(self.groupBox_20)
        self.label_84.setGeometry(QtCore.QRect(220, 30, 31, 16))
        self.label_84.setObjectName(_fromUtf8("label_84"))
        self.dateEdit_6 = QtGui.QDateEdit(self.groupBox_20)
        self.dateEdit_6.setGeometry(QtCore.QRect(250, 30, 110, 22))
        self.dateEdit_6.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_6.setObjectName(_fromUtf8("dateEdit_6"))
        self.pushButton_17 = QtGui.QPushButton(self.groupBox_20)
        self.pushButton_17.setGeometry(QtCore.QRect(200, 70, 161, 41))
        self.pushButton_17.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.tableWidget_6 = QtGui.QTableWidget(self.groupBox_20)
        self.tableWidget_6.setGeometry(QtCore.QRect(10, 130, 641, 371))
        self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_6"))
        self.tableWidget_6.setColumnCount(6)
        self.tableWidget_6.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        self.comboBox_10 = QtGui.QComboBox(self.groupBox_20)
        self.comboBox_10.setGeometry(QtCore.QRect(70, 80, 111, 22))
        self.comboBox_10.setObjectName(_fromUtf8("comboBox_10"))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.groupBox_21 = QtGui.QGroupBox(self.tab_21)
        self.groupBox_21.setGeometry(QtCore.QRect(710, 10, 431, 201))
        self.groupBox_21.setObjectName(_fromUtf8("groupBox_21"))
        self.pushButton_18 = QtGui.QPushButton(self.groupBox_21)
        self.pushButton_18.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_18.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.tabWidget_3.addTab(self.tab_21, _fromUtf8(""))
        self.tab_22 = QtGui.QWidget()
        self.tab_22.setObjectName(_fromUtf8("tab_22"))
        self.groupBox_22 = QtGui.QGroupBox(self.tab_22)
        self.groupBox_22.setGeometry(QtCore.QRect(10, 10, 551, 521))
        self.groupBox_22.setObjectName(_fromUtf8("groupBox_22"))
        self.dateEdit_7 = QtGui.QDateEdit(self.groupBox_22)
        self.dateEdit_7.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_7.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_7.setObjectName(_fromUtf8("dateEdit_7"))
        self.label_85 = QtGui.QLabel(self.groupBox_22)
        self.label_85.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_85.setObjectName(_fromUtf8("label_85"))
        self.label_86 = QtGui.QLabel(self.groupBox_22)
        self.label_86.setGeometry(QtCore.QRect(220, 30, 31, 16))
        self.label_86.setObjectName(_fromUtf8("label_86"))
        self.dateEdit_8 = QtGui.QDateEdit(self.groupBox_22)
        self.dateEdit_8.setGeometry(QtCore.QRect(250, 30, 110, 22))
        self.dateEdit_8.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_8.setObjectName(_fromUtf8("dateEdit_8"))
        self.pushButton_19 = QtGui.QPushButton(self.groupBox_22)
        self.pushButton_19.setGeometry(QtCore.QRect(200, 70, 161, 41))
        self.pushButton_19.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.tableWidget_7 = QtGui.QTableWidget(self.groupBox_22)
        self.tableWidget_7.setGeometry(QtCore.QRect(10, 130, 521, 371))
        self.tableWidget_7.setObjectName(_fromUtf8("tableWidget_7"))
        self.tableWidget_7.setColumnCount(5)
        self.tableWidget_7.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        self.comboBox_11 = QtGui.QComboBox(self.groupBox_22)
        self.comboBox_11.setGeometry(QtCore.QRect(70, 80, 111, 22))
        self.comboBox_11.setObjectName(_fromUtf8("comboBox_11"))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.groupBox_23 = QtGui.QGroupBox(self.tab_22)
        self.groupBox_23.setGeometry(QtCore.QRect(580, 10, 431, 201))
        self.groupBox_23.setObjectName(_fromUtf8("groupBox_23"))
        self.pushButton_20 = QtGui.QPushButton(self.groupBox_23)
        self.pushButton_20.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_20.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.tabWidget_3.addTab(self.tab_22, _fromUtf8(""))
        self.tab_30 = QtGui.QWidget()
        self.tab_30.setObjectName(_fromUtf8("tab_30"))
        self.groupBox_49 = QtGui.QGroupBox(self.tab_30)
        self.groupBox_49.setEnabled(True)
        self.groupBox_49.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.groupBox_49.setObjectName(_fromUtf8("groupBox_49"))
        self.lineEdit_91 = QtGui.QLineEdit(self.groupBox_49)
        self.lineEdit_91.setEnabled(True)
        self.lineEdit_91.setGeometry(QtCore.QRect(140, 30, 231, 20))
        self.lineEdit_91.setText(_fromUtf8(""))
        self.lineEdit_91.setObjectName(_fromUtf8("lineEdit_91"))
        self.label_175 = QtGui.QLabel(self.groupBox_49)
        self.label_175.setEnabled(True)
        self.label_175.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.label_175.setObjectName(_fromUtf8("label_175"))
        self.lineEdit_92 = QtGui.QLineEdit(self.groupBox_49)
        self.lineEdit_92.setGeometry(QtCore.QRect(140, 180, 231, 20))
        self.lineEdit_92.setText(_fromUtf8(""))
        self.lineEdit_92.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_92.setObjectName(_fromUtf8("lineEdit_92"))
        self.label_194 = QtGui.QLabel(self.groupBox_49)
        self.label_194.setGeometry(QtCore.QRect(20, 180, 81, 16))
        self.label_194.setObjectName(_fromUtf8("label_194"))
        self.lineEdit_93 = QtGui.QLineEdit(self.groupBox_49)
        self.lineEdit_93.setEnabled(True)
        self.lineEdit_93.setGeometry(QtCore.QRect(140, 150, 231, 20))
        self.lineEdit_93.setText(_fromUtf8(""))
        self.lineEdit_93.setObjectName(_fromUtf8("lineEdit_93"))
        self.label_195 = QtGui.QLabel(self.groupBox_49)
        self.label_195.setGeometry(QtCore.QRect(20, 150, 81, 16))
        self.label_195.setObjectName(_fromUtf8("label_195"))
        self.pushButton_52 = QtGui.QPushButton(self.groupBox_49)
        self.pushButton_52.setGeometry(QtCore.QRect(130, 250, 171, 41))
        self.pushButton_52.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_52.setObjectName(_fromUtf8("pushButton_52"))
        self.label_196 = QtGui.QLabel(self.groupBox_49)
        self.label_196.setGeometry(QtCore.QRect(60, 210, 321, 31))
        self.label_196.setStyleSheet(_fromUtf8("color:red;"))
        self.label_196.setText(_fromUtf8(""))
        self.label_196.setObjectName(_fromUtf8("label_196"))
        self.label_197 = QtGui.QLabel(self.groupBox_49)
        self.label_197.setEnabled(True)
        self.label_197.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.label_197.setObjectName(_fromUtf8("label_197"))
        self.lineEdit_101 = QtGui.QLineEdit(self.groupBox_49)
        self.lineEdit_101.setEnabled(False)
        self.lineEdit_101.setGeometry(QtCore.QRect(140, 60, 231, 20))
        self.lineEdit_101.setText(_fromUtf8(""))
        self.lineEdit_101.setObjectName(_fromUtf8("lineEdit_101"))
        self.lineEdit_102 = QtGui.QLineEdit(self.groupBox_49)
        self.lineEdit_102.setEnabled(False)
        self.lineEdit_102.setGeometry(QtCore.QRect(140, 90, 231, 20))
        self.lineEdit_102.setText(_fromUtf8(""))
        self.lineEdit_102.setObjectName(_fromUtf8("lineEdit_102"))
        self.label_198 = QtGui.QLabel(self.groupBox_49)
        self.label_198.setEnabled(True)
        self.label_198.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.label_198.setObjectName(_fromUtf8("label_198"))
        self.lineEdit_103 = QtGui.QLineEdit(self.groupBox_49)
        self.lineEdit_103.setEnabled(False)
        self.lineEdit_103.setGeometry(QtCore.QRect(140, 120, 231, 20))
        self.lineEdit_103.setText(_fromUtf8(""))
        self.lineEdit_103.setObjectName(_fromUtf8("lineEdit_103"))
        self.label_199 = QtGui.QLabel(self.groupBox_49)
        self.label_199.setEnabled(True)
        self.label_199.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.label_199.setObjectName(_fromUtf8("label_199"))
        self.tabWidget_3.addTab(self.tab_30, _fromUtf8(""))
        self.tab_31 = QtGui.QWidget()
        self.tab_31.setObjectName(_fromUtf8("tab_31"))
        self.groupBox_50 = QtGui.QGroupBox(self.tab_31)
        self.groupBox_50.setGeometry(QtCore.QRect(740, 20, 431, 201))
        self.groupBox_50.setObjectName(_fromUtf8("groupBox_50"))
        self.pushButton_53 = QtGui.QPushButton(self.groupBox_50)
        self.pushButton_53.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_53.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_53.setObjectName(_fromUtf8("pushButton_53"))
        self.groupBox_51 = QtGui.QGroupBox(self.tab_31)
        self.groupBox_51.setGeometry(QtCore.QRect(10, 20, 701, 501))
        self.groupBox_51.setObjectName(_fromUtf8("groupBox_51"))
        self.tableWidget_22 = QtGui.QTableWidget(self.groupBox_51)
        self.tableWidget_22.setGeometry(QtCore.QRect(10, 120, 661, 361))
        self.tableWidget_22.setObjectName(_fromUtf8("tableWidget_22"))
        self.tableWidget_22.setColumnCount(6)
        self.tableWidget_22.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(5, item)
        self.label_109 = QtGui.QLabel(self.groupBox_51)
        self.label_109.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_109.setObjectName(_fromUtf8("label_109"))
        self.pushButton_62 = QtGui.QPushButton(self.groupBox_51)
        self.pushButton_62.setGeometry(QtCore.QRect(20, 60, 161, 41))
        self.pushButton_62.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_62.setObjectName(_fromUtf8("pushButton_62"))
        self.label_114 = QtGui.QLabel(self.groupBox_51)
        self.label_114.setGeometry(QtCore.QRect(200, 20, 31, 16))
        self.label_114.setObjectName(_fromUtf8("label_114"))
        self.dateEdit_21 = QtGui.QDateEdit(self.groupBox_51)
        self.dateEdit_21.setGeometry(QtCore.QRect(50, 20, 110, 22))
        self.dateEdit_21.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_21.setObjectName(_fromUtf8("dateEdit_21"))
        self.dateEdit_27 = QtGui.QDateEdit(self.groupBox_51)
        self.dateEdit_27.setGeometry(QtCore.QRect(230, 20, 110, 22))
        self.dateEdit_27.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_27.setObjectName(_fromUtf8("dateEdit_27"))
        self.tabWidget_3.addTab(self.tab_31, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        self.groupBox_24 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_24.setGeometry(QtCore.QRect(10, 10, 691, 521))
        self.groupBox_24.setObjectName(_fromUtf8("groupBox_24"))
        self.dateEdit_9 = QtGui.QDateEdit(self.groupBox_24)
        self.dateEdit_9.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_9.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_9.setObjectName(_fromUtf8("dateEdit_9"))
        self.label_87 = QtGui.QLabel(self.groupBox_24)
        self.label_87.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_87.setObjectName(_fromUtf8("label_87"))
        self.label_88 = QtGui.QLabel(self.groupBox_24)
        self.label_88.setGeometry(QtCore.QRect(220, 30, 31, 16))
        self.label_88.setObjectName(_fromUtf8("label_88"))
        self.dateEdit_10 = QtGui.QDateEdit(self.groupBox_24)
        self.dateEdit_10.setGeometry(QtCore.QRect(250, 30, 110, 22))
        self.dateEdit_10.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_10.setObjectName(_fromUtf8("dateEdit_10"))
        self.pushButton_21 = QtGui.QPushButton(self.groupBox_24)
        self.pushButton_21.setGeometry(QtCore.QRect(30, 70, 161, 41))
        self.pushButton_21.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.tableWidget_8 = QtGui.QTableWidget(self.groupBox_24)
        self.tableWidget_8.setGeometry(QtCore.QRect(10, 130, 661, 371))
        self.tableWidget_8.setObjectName(_fromUtf8("tableWidget_8"))
        self.tableWidget_8.setColumnCount(5)
        self.tableWidget_8.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        self.groupBox_25 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_25.setGeometry(QtCore.QRect(720, 10, 431, 201))
        self.groupBox_25.setObjectName(_fromUtf8("groupBox_25"))
        self.pushButton_22 = QtGui.QPushButton(self.groupBox_25)
        self.pushButton_22.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_22.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.tabWidget_3.addTab(self.tab_23, _fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8("Receipt and Debtors card"))
        self.vbnbv = QtGui.QWidget()
        self.vbnbv.setObjectName(_fromUtf8("vbnbv"))
        self.tabWidget_5 = QtGui.QTabWidget(self.vbnbv)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 1261, 591))
        self.tabWidget_5.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.tabWidget_5.setObjectName(_fromUtf8("tabWidget_5"))
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName(_fromUtf8("tab_15"))
        self.groupBox_41 = QtGui.QGroupBox(self.tab_15)
        self.groupBox_41.setGeometry(QtCore.QRect(350, 9, 251, 411))
        self.groupBox_41.setObjectName(_fromUtf8("groupBox_41"))
        self.label_121 = QtGui.QLabel(self.groupBox_41)
        self.label_121.setGeometry(QtCore.QRect(10, 30, 191, 20))
        self.label_121.setObjectName(_fromUtf8("label_121"))
        self.label_122 = QtGui.QLabel(self.groupBox_41)
        self.label_122.setGeometry(QtCore.QRect(10, 60, 191, 20))
        self.label_122.setObjectName(_fromUtf8("label_122"))
        self.label_123 = QtGui.QLabel(self.groupBox_41)
        self.label_123.setGeometry(QtCore.QRect(10, 90, 191, 20))
        self.label_123.setObjectName(_fromUtf8("label_123"))
        self.label_124 = QtGui.QLabel(self.groupBox_41)
        self.label_124.setGeometry(QtCore.QRect(10, 120, 191, 20))
        self.label_124.setObjectName(_fromUtf8("label_124"))
        self.label_125 = QtGui.QLabel(self.groupBox_41)
        self.label_125.setGeometry(QtCore.QRect(10, 150, 191, 20))
        self.label_125.setObjectName(_fromUtf8("label_125"))
        self.label_126 = QtGui.QLabel(self.groupBox_41)
        self.label_126.setGeometry(QtCore.QRect(10, 180, 191, 20))
        self.label_126.setObjectName(_fromUtf8("label_126"))
        self.label_127 = QtGui.QLabel(self.groupBox_41)
        self.label_127.setGeometry(QtCore.QRect(10, 210, 191, 20))
        self.label_127.setObjectName(_fromUtf8("label_127"))
        self.label_128 = QtGui.QLabel(self.groupBox_41)
        self.label_128.setGeometry(QtCore.QRect(10, 270, 191, 20))
        self.label_128.setObjectName(_fromUtf8("label_128"))
        self.label_129 = QtGui.QLabel(self.groupBox_41)
        self.label_129.setGeometry(QtCore.QRect(10, 240, 191, 20))
        self.label_129.setObjectName(_fromUtf8("label_129"))
        self.label_192 = QtGui.QLabel(self.groupBox_41)
        self.label_192.setGeometry(QtCore.QRect(10, 300, 191, 20))
        self.label_192.setObjectName(_fromUtf8("label_192"))
        self.groupBox_42 = QtGui.QGroupBox(self.tab_15)
        self.groupBox_42.setGeometry(QtCore.QRect(10, 10, 331, 411))
        self.groupBox_42.setObjectName(_fromUtf8("groupBox_42"))
        self.label_130 = QtGui.QLabel(self.groupBox_42)
        self.label_130.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_130.setObjectName(_fromUtf8("label_130"))
        self.lineEdit_21 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_21.setGeometry(QtCore.QRect(100, 70, 191, 20))
        self.lineEdit_21.setText(_fromUtf8(""))
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.label_131 = QtGui.QLabel(self.groupBox_42)
        self.label_131.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_131.setObjectName(_fromUtf8("label_131"))
        self.dateEdit_11 = QtGui.QDateEdit(self.groupBox_42)
        self.dateEdit_11.setGeometry(QtCore.QRect(100, 30, 110, 22))
        self.dateEdit_11.setObjectName(_fromUtf8("dateEdit_11"))
        self.lineEdit_22 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_22.setGeometry(QtCore.QRect(100, 100, 191, 20))
        self.lineEdit_22.setText(_fromUtf8(""))
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.label_132 = QtGui.QLabel(self.groupBox_42)
        self.label_132.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_132.setObjectName(_fromUtf8("label_132"))
        self.label_133 = QtGui.QLabel(self.groupBox_42)
        self.label_133.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_133.setObjectName(_fromUtf8("label_133"))
        self.label_134 = QtGui.QLabel(self.groupBox_42)
        self.label_134.setGeometry(QtCore.QRect(10, 200, 81, 16))
        self.label_134.setObjectName(_fromUtf8("label_134"))
        self.lineEdit_24 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_24.setGeometry(QtCore.QRect(100, 200, 191, 20))
        self.lineEdit_24.setText(_fromUtf8(""))
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.label_135 = QtGui.QLabel(self.groupBox_42)
        self.label_135.setGeometry(QtCore.QRect(10, 230, 71, 16))
        self.label_135.setObjectName(_fromUtf8("label_135"))
        self.lineEdit_25 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_25.setGeometry(QtCore.QRect(100, 230, 191, 20))
        self.lineEdit_25.setText(_fromUtf8(""))
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.pushButton_44 = QtGui.QPushButton(self.groupBox_42)
        self.pushButton_44.setGeometry(QtCore.QRect(100, 300, 171, 41))
        self.pushButton_44.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_44.setObjectName(_fromUtf8("pushButton_44"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.groupBox_42)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(100, 130, 191, 61))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.label_136 = QtGui.QLabel(self.groupBox_42)
        self.label_136.setGeometry(QtCore.QRect(50, 260, 271, 31))
        self.label_136.setStyleSheet(_fromUtf8("color:red;"))
        self.label_136.setText(_fromUtf8(""))
        self.label_136.setObjectName(_fromUtf8("label_136"))
        self.pushButton_60 = QtGui.QPushButton(self.groupBox_42)
        self.pushButton_60.setGeometry(QtCore.QRect(100, 350, 171, 41))
        self.pushButton_60.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_60.setObjectName(_fromUtf8("pushButton_60"))
        self.tabWidget_5.addTab(self.tab_15, _fromUtf8(""))
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName(_fromUtf8("tab_16"))
        self.groupBox_43 = QtGui.QGroupBox(self.tab_16)
        self.groupBox_43.setGeometry(QtCore.QRect(10, 10, 681, 521))
        self.groupBox_43.setObjectName(_fromUtf8("groupBox_43"))
        self.dateEdit_17 = QtGui.QDateEdit(self.groupBox_43)
        self.dateEdit_17.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_17.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_17.setObjectName(_fromUtf8("dateEdit_17"))
        self.label_137 = QtGui.QLabel(self.groupBox_43)
        self.label_137.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_137.setObjectName(_fromUtf8("label_137"))
        self.label_138 = QtGui.QLabel(self.groupBox_43)
        self.label_138.setGeometry(QtCore.QRect(220, 30, 31, 16))
        self.label_138.setObjectName(_fromUtf8("label_138"))
        self.dateEdit_22 = QtGui.QDateEdit(self.groupBox_43)
        self.dateEdit_22.setGeometry(QtCore.QRect(250, 30, 110, 22))
        self.dateEdit_22.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_22.setObjectName(_fromUtf8("dateEdit_22"))
        self.pushButton_45 = QtGui.QPushButton(self.groupBox_43)
        self.pushButton_45.setGeometry(QtCore.QRect(30, 70, 161, 41))
        self.pushButton_45.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_45.setObjectName(_fromUtf8("pushButton_45"))
        self.tableWidget_20 = QtGui.QTableWidget(self.groupBox_43)
        self.tableWidget_20.setGeometry(QtCore.QRect(10, 130, 651, 371))
        self.tableWidget_20.setObjectName(_fromUtf8("tableWidget_20"))
        self.tableWidget_20.setColumnCount(6)
        self.tableWidget_20.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(5, item)
        self.groupBox_44 = QtGui.QGroupBox(self.tab_16)
        self.groupBox_44.setGeometry(QtCore.QRect(710, 10, 431, 201))
        self.groupBox_44.setObjectName(_fromUtf8("groupBox_44"))
        self.pushButton_46 = QtGui.QPushButton(self.groupBox_44)
        self.pushButton_46.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_46.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_46.setObjectName(_fromUtf8("pushButton_46"))
        self.tabWidget_5.addTab(self.tab_16, _fromUtf8(""))
        self.tabWidget.addTab(self.vbnbv, _fromUtf8(""))
        self.ghjghj = QtGui.QWidget()
        self.ghjghj.setObjectName(_fromUtf8("ghjghj"))
        self.tabWidget_4 = QtGui.QTabWidget(self.ghjghj)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 1261, 581))
        self.tabWidget_4.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        self.groupBox_26 = QtGui.QGroupBox(self.tab_24)
        self.groupBox_26.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.groupBox_26.setObjectName(_fromUtf8("groupBox_26"))
        self.label_89 = QtGui.QLabel(self.groupBox_26)
        self.label_89.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.label_89.setObjectName(_fromUtf8("label_89"))
        self.pushButton_23 = QtGui.QPushButton(self.groupBox_26)
        self.pushButton_23.setGeometry(QtCore.QRect(140, 70, 161, 41))
        self.pushButton_23.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.tableWidget_9 = QtGui.QTableWidget(self.groupBox_26)
        self.tableWidget_9.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_9.setObjectName(_fromUtf8("tableWidget_9"))
        self.tableWidget_9.setColumnCount(7)
        self.tableWidget_9.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(6, item)
        self.dateEdit_12 = QtGui.QDateEdit(self.groupBox_26)
        self.dateEdit_12.setGeometry(QtCore.QRect(120, 30, 110, 22))
        self.dateEdit_12.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_12.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_12.setObjectName(_fromUtf8("dateEdit_12"))
        self.comboBox_19 = QtGui.QComboBox(self.groupBox_26)
        self.comboBox_19.setGeometry(QtCore.QRect(20, 70, 101, 22))
        self.comboBox_19.setObjectName(_fromUtf8("comboBox_19"))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.groupBox_27 = QtGui.QGroupBox(self.tab_24)
        self.groupBox_27.setGeometry(QtCore.QRect(800, 10, 441, 201))
        self.groupBox_27.setObjectName(_fromUtf8("groupBox_27"))
        self.pushButton_24 = QtGui.QPushButton(self.groupBox_27)
        self.pushButton_24.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_24.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.tabWidget_4.addTab(self.tab_24, _fromUtf8(""))
        self.tab_26 = QtGui.QWidget()
        self.tab_26.setObjectName(_fromUtf8("tab_26"))
        self.groupBox_28 = QtGui.QGroupBox(self.tab_26)
        self.groupBox_28.setGeometry(QtCore.QRect(10, 10, 1061, 521))
        self.groupBox_28.setObjectName(_fromUtf8("groupBox_28"))
        self.pushButton_25 = QtGui.QPushButton(self.groupBox_28)
        self.pushButton_25.setGeometry(QtCore.QRect(140, 70, 161, 41))
        self.pushButton_25.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.tableWidget_10 = QtGui.QTableWidget(self.groupBox_28)
        self.tableWidget_10.setGeometry(QtCore.QRect(10, 130, 1031, 371))
        self.tableWidget_10.setObjectName(_fromUtf8("tableWidget_10"))
        self.tableWidget_10.setColumnCount(10)
        self.tableWidget_10.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(9, item)
        self.dateEdit_13 = QtGui.QDateEdit(self.groupBox_28)
        self.dateEdit_13.setGeometry(QtCore.QRect(120, 30, 110, 22))
        self.dateEdit_13.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_13.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_13.setObjectName(_fromUtf8("dateEdit_13"))
        self.comboBox_20 = QtGui.QComboBox(self.groupBox_28)
        self.comboBox_20.setGeometry(QtCore.QRect(20, 70, 101, 22))
        self.comboBox_20.setObjectName(_fromUtf8("comboBox_20"))
        self.comboBox_20.addItem(_fromUtf8(""))
        self.comboBox_20.addItem(_fromUtf8(""))
        self.comboBox_20.addItem(_fromUtf8(""))
        self.dateEdit_35 = QtGui.QDateEdit(self.groupBox_28)
        self.dateEdit_35.setGeometry(QtCore.QRect(280, 30, 110, 22))
        self.dateEdit_35.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_35.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_35.setObjectName(_fromUtf8("dateEdit_35"))
        self.label_205 = QtGui.QLabel(self.groupBox_28)
        self.label_205.setGeometry(QtCore.QRect(250, 30, 31, 16))
        self.label_205.setObjectName(_fromUtf8("label_205"))
        self.label_162 = QtGui.QLabel(self.groupBox_28)
        self.label_162.setGeometry(QtCore.QRect(70, 30, 41, 16))
        self.label_162.setObjectName(_fromUtf8("label_162"))
        self.groupBox_29 = QtGui.QGroupBox(self.tab_26)
        self.groupBox_29.setGeometry(QtCore.QRect(1090, 10, 151, 151))
        self.groupBox_29.setObjectName(_fromUtf8("groupBox_29"))
        self.pushButton_26 = QtGui.QPushButton(self.groupBox_29)
        self.pushButton_26.setGeometry(QtCore.QRect(20, 50, 111, 41))
        self.pushButton_26.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.tabWidget_4.addTab(self.tab_26, _fromUtf8(""))
        self.tab_27 = QtGui.QWidget()
        self.tab_27.setObjectName(_fromUtf8("tab_27"))
        self.groupBox_30 = QtGui.QGroupBox(self.tab_27)
        self.groupBox_30.setGeometry(QtCore.QRect(800, 10, 441, 201))
        self.groupBox_30.setObjectName(_fromUtf8("groupBox_30"))
        self.pushButton_27 = QtGui.QPushButton(self.groupBox_30)
        self.pushButton_27.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_27.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.groupBox_31 = QtGui.QGroupBox(self.tab_27)
        self.groupBox_31.setGeometry(QtCore.QRect(10, 10, 761, 521))
        self.groupBox_31.setObjectName(_fromUtf8("groupBox_31"))
        self.pushButton_28 = QtGui.QPushButton(self.groupBox_31)
        self.pushButton_28.setGeometry(QtCore.QRect(140, 70, 161, 41))
        self.pushButton_28.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.tableWidget_11 = QtGui.QTableWidget(self.groupBox_31)
        self.tableWidget_11.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_11.setObjectName(_fromUtf8("tableWidget_11"))
        self.tableWidget_11.setColumnCount(7)
        self.tableWidget_11.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(6, item)
        self.comboBox_21 = QtGui.QComboBox(self.groupBox_31)
        self.comboBox_21.setGeometry(QtCore.QRect(20, 70, 101, 22))
        self.comboBox_21.setObjectName(_fromUtf8("comboBox_21"))
        self.comboBox_21.addItem(_fromUtf8(""))
        self.comboBox_21.addItem(_fromUtf8(""))
        self.comboBox_21.addItem(_fromUtf8(""))
        self.dateEdit_36 = QtGui.QDateEdit(self.groupBox_31)
        self.dateEdit_36.setGeometry(QtCore.QRect(230, 30, 110, 22))
        self.dateEdit_36.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_36.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_36.setObjectName(_fromUtf8("dateEdit_36"))
        self.label_163 = QtGui.QLabel(self.groupBox_31)
        self.label_163.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label_163.setObjectName(_fromUtf8("label_163"))
        self.dateEdit_37 = QtGui.QDateEdit(self.groupBox_31)
        self.dateEdit_37.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_37.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_37.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_37.setObjectName(_fromUtf8("dateEdit_37"))
        self.label_206 = QtGui.QLabel(self.groupBox_31)
        self.label_206.setGeometry(QtCore.QRect(200, 30, 31, 16))
        self.label_206.setObjectName(_fromUtf8("label_206"))
        self.tabWidget_4.addTab(self.tab_27, _fromUtf8(""))
        self.tab_28 = QtGui.QWidget()
        self.tab_28.setObjectName(_fromUtf8("tab_28"))
        self.groupBox_32 = QtGui.QGroupBox(self.tab_28)
        self.groupBox_32.setGeometry(QtCore.QRect(800, 10, 441, 201))
        self.groupBox_32.setObjectName(_fromUtf8("groupBox_32"))
        self.pushButton_29 = QtGui.QPushButton(self.groupBox_32)
        self.pushButton_29.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_29.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.groupBox_33 = QtGui.QGroupBox(self.tab_28)
        self.groupBox_33.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.groupBox_33.setObjectName(_fromUtf8("groupBox_33"))
        self.label_92 = QtGui.QLabel(self.groupBox_33)
        self.label_92.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_92.setObjectName(_fromUtf8("label_92"))
        self.pushButton_30 = QtGui.QPushButton(self.groupBox_33)
        self.pushButton_30.setGeometry(QtCore.QRect(30, 70, 161, 41))
        self.pushButton_30.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.tableWidget_12 = QtGui.QTableWidget(self.groupBox_33)
        self.tableWidget_12.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_12.setObjectName(_fromUtf8("tableWidget_12"))
        self.tableWidget_12.setColumnCount(5)
        self.tableWidget_12.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, item)
        self.dateEdit_15 = QtGui.QDateEdit(self.groupBox_33)
        self.dateEdit_15.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.dateEdit_15.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_15.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_15.setObjectName(_fromUtf8("dateEdit_15"))
        self.dateEdit_24 = QtGui.QDateEdit(self.groupBox_33)
        self.dateEdit_24.setGeometry(QtCore.QRect(240, 30, 110, 22))
        self.dateEdit_24.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_24.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_24.setObjectName(_fromUtf8("dateEdit_24"))
        self.label_170 = QtGui.QLabel(self.groupBox_33)
        self.label_170.setGeometry(QtCore.QRect(210, 30, 31, 16))
        self.label_170.setObjectName(_fromUtf8("label_170"))
        self.tabWidget_4.addTab(self.tab_28, _fromUtf8(""))
        self.tab_13 = QtGui.QWidget()
        self.tab_13.setObjectName(_fromUtf8("tab_13"))
        self.groupBox_36 = QtGui.QGroupBox(self.tab_13)
        self.groupBox_36.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.groupBox_36.setObjectName(_fromUtf8("groupBox_36"))
        self.pushButton_35 = QtGui.QPushButton(self.groupBox_36)
        self.pushButton_35.setGeometry(QtCore.QRect(30, 70, 161, 41))
        self.pushButton_35.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_35.setObjectName(_fromUtf8("pushButton_35"))
        self.dateEdit_16 = QtGui.QDateEdit(self.groupBox_36)
        self.dateEdit_16.setGeometry(QtCore.QRect(120, 30, 110, 22))
        self.dateEdit_16.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_16.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_16.setObjectName(_fromUtf8("dateEdit_16"))
        self.tableWidget_16 = QtGui.QTableWidget(self.groupBox_36)
        self.tableWidget_16.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_16.setObjectName(_fromUtf8("tableWidget_16"))
        self.tableWidget_16.setColumnCount(5)
        self.tableWidget_16.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(4, item)
        self.label_171 = QtGui.QLabel(self.groupBox_36)
        self.label_171.setGeometry(QtCore.QRect(260, 30, 31, 16))
        self.label_171.setObjectName(_fromUtf8("label_171"))
        self.dateEdit_25 = QtGui.QDateEdit(self.groupBox_36)
        self.dateEdit_25.setGeometry(QtCore.QRect(290, 30, 110, 22))
        self.dateEdit_25.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_25.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_25.setObjectName(_fromUtf8("dateEdit_25"))
        self.label_172 = QtGui.QLabel(self.groupBox_36)
        self.label_172.setGeometry(QtCore.QRect(80, 30, 41, 16))
        self.label_172.setObjectName(_fromUtf8("label_172"))
        self.groupBox_37 = QtGui.QGroupBox(self.tab_13)
        self.groupBox_37.setGeometry(QtCore.QRect(800, 10, 441, 201))
        self.groupBox_37.setObjectName(_fromUtf8("groupBox_37"))
        self.pushButton_36 = QtGui.QPushButton(self.groupBox_37)
        self.pushButton_36.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_36.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_36.setObjectName(_fromUtf8("pushButton_36"))
        self.tabWidget_4.addTab(self.tab_13, _fromUtf8(""))
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.groupBox_38 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_38.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.groupBox_38.setObjectName(_fromUtf8("groupBox_38"))
        self.pushButton_37 = QtGui.QPushButton(self.groupBox_38)
        self.pushButton_37.setGeometry(QtCore.QRect(30, 70, 161, 41))
        self.pushButton_37.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.dateEdit_18 = QtGui.QDateEdit(self.groupBox_38)
        self.dateEdit_18.setGeometry(QtCore.QRect(120, 30, 110, 22))
        self.dateEdit_18.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_18.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_18.setObjectName(_fromUtf8("dateEdit_18"))
        self.tableWidget_18 = QtGui.QTableWidget(self.groupBox_38)
        self.tableWidget_18.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_18.setObjectName(_fromUtf8("tableWidget_18"))
        self.tableWidget_18.setColumnCount(5)
        self.tableWidget_18.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(4, item)
        self.label_173 = QtGui.QLabel(self.groupBox_38)
        self.label_173.setGeometry(QtCore.QRect(80, 30, 41, 16))
        self.label_173.setObjectName(_fromUtf8("label_173"))
        self.dateEdit_26 = QtGui.QDateEdit(self.groupBox_38)
        self.dateEdit_26.setGeometry(QtCore.QRect(290, 30, 110, 22))
        self.dateEdit_26.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit_26.setDate(QtCore.QDate(2016, 12, 1))
        self.dateEdit_26.setObjectName(_fromUtf8("dateEdit_26"))
        self.label_174 = QtGui.QLabel(self.groupBox_38)
        self.label_174.setGeometry(QtCore.QRect(260, 30, 31, 16))
        self.label_174.setObjectName(_fromUtf8("label_174"))
        self.groupBox_39 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_39.setGeometry(QtCore.QRect(800, 10, 441, 201))
        self.groupBox_39.setObjectName(_fromUtf8("groupBox_39"))
        self.pushButton_38 = QtGui.QPushButton(self.groupBox_39)
        self.pushButton_38.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_38.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.tabWidget_4.addTab(self.tab_14, _fromUtf8(""))
        self.tab_25 = QtGui.QWidget()
        self.tab_25.setObjectName(_fromUtf8("tab_25"))
        self.groupBox_34 = QtGui.QGroupBox(self.tab_25)
        self.groupBox_34.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.groupBox_34.setObjectName(_fromUtf8("groupBox_34"))
        self.pushButton_33 = QtGui.QPushButton(self.groupBox_34)
        self.pushButton_33.setGeometry(QtCore.QRect(30, 60, 161, 41))
        self.pushButton_33.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.tableWidget_14 = QtGui.QTableWidget(self.groupBox_34)
        self.tableWidget_14.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_14.setObjectName(_fromUtf8("tableWidget_14"))
        self.tableWidget_14.setColumnCount(7)
        self.tableWidget_14.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(6, item)
        self.groupBox_35 = QtGui.QGroupBox(self.tab_25)
        self.groupBox_35.setGeometry(QtCore.QRect(800, 10, 441, 201))
        self.groupBox_35.setObjectName(_fromUtf8("groupBox_35"))
        self.pushButton_34 = QtGui.QPushButton(self.groupBox_35)
        self.pushButton_34.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_34.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_34.setObjectName(_fromUtf8("pushButton_34"))
        self.tabWidget_4.addTab(self.tab_25, _fromUtf8(""))
        self.tabWidget.addTab(self.ghjghj, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 10, 551, 201))
        self.groupBox_10.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.pushButton_41 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_41.setGeometry(QtCore.QRect(180, 40, 171, 41))
        self.pushButton_41.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_41.setObjectName(_fromUtf8("pushButton_41"))
        self.pushButton_42 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_42.setGeometry(QtCore.QRect(180, 100, 171, 41))
        self.pushButton_42.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_42.setObjectName(_fromUtf8("pushButton_42"))
        self.label_115 = QtGui.QLabel(self.groupBox_10)
        self.label_115.setGeometry(QtCore.QRect(20, 160, 331, 31))
        self.label_115.setStyleSheet(_fromUtf8("color:blue;"))
        self.label_115.setText(_fromUtf8(""))
        self.label_115.setObjectName(_fromUtf8("label_115"))
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.tabWidget_6 = QtGui.QTabWidget(self.tab_8)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 0, 1261, 591))
        self.tabWidget_6.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"    QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.tabWidget_6.setObjectName(_fromUtf8("tabWidget_6"))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        self.groupBox_46 = QtGui.QGroupBox(self.tab_18)
        self.groupBox_46.setGeometry(QtCore.QRect(10, 10, 331, 381))
        self.groupBox_46.setObjectName(_fromUtf8("groupBox_46"))
        self.label_148 = QtGui.QLabel(self.groupBox_46)
        self.label_148.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_148.setObjectName(_fromUtf8("label_148"))
        self.lineEdit_23 = QtGui.QLineEdit(self.groupBox_46)
        self.lineEdit_23.setGeometry(QtCore.QRect(100, 30, 191, 20))
        self.lineEdit_23.setText(_fromUtf8(""))
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.label_151 = QtGui.QLabel(self.groupBox_46)
        self.label_151.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_151.setObjectName(_fromUtf8("label_151"))
        self.label_153 = QtGui.QLabel(self.groupBox_46)
        self.label_153.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_153.setObjectName(_fromUtf8("label_153"))
        self.lineEdit_79 = QtGui.QLineEdit(self.groupBox_46)
        self.lineEdit_79.setGeometry(QtCore.QRect(100, 130, 191, 20))
        self.lineEdit_79.setText(_fromUtf8(""))
        self.lineEdit_79.setObjectName(_fromUtf8("lineEdit_79"))
        self.pushButton_47 = QtGui.QPushButton(self.groupBox_46)
        self.pushButton_47.setGeometry(QtCore.QRect(100, 220, 171, 41))
        self.pushButton_47.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_47.setObjectName(_fromUtf8("pushButton_47"))
        self.plainTextEdit_6 = QtGui.QPlainTextEdit(self.groupBox_46)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(100, 60, 191, 61))
        self.plainTextEdit_6.setObjectName(_fromUtf8("plainTextEdit_6"))
        self.label_154 = QtGui.QLabel(self.groupBox_46)
        self.label_154.setGeometry(QtCore.QRect(50, 190, 271, 21))
        self.label_154.setStyleSheet(_fromUtf8("color:red;"))
        self.label_154.setText(_fromUtf8(""))
        self.label_154.setObjectName(_fromUtf8("label_154"))
        self.comboBox_12 = QtGui.QComboBox(self.groupBox_46)
        self.comboBox_12.setGeometry(QtCore.QRect(100, 160, 69, 22))
        self.comboBox_12.setObjectName(_fromUtf8("comboBox_12"))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.pushButton_59 = QtGui.QPushButton(self.groupBox_46)
        self.pushButton_59.setGeometry(QtCore.QRect(100, 270, 171, 41))
        self.pushButton_59.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}"))
        self.pushButton_59.setObjectName(_fromUtf8("pushButton_59"))
        self.groupBox_45 = QtGui.QGroupBox(self.tab_18)
        self.groupBox_45.setGeometry(QtCore.QRect(360, 10, 251, 381))
        self.groupBox_45.setObjectName(_fromUtf8("groupBox_45"))
        self.label_139 = QtGui.QLabel(self.groupBox_45)
        self.label_139.setGeometry(QtCore.QRect(10, 30, 191, 20))
        self.label_139.setObjectName(_fromUtf8("label_139"))
        self.label_140 = QtGui.QLabel(self.groupBox_45)
        self.label_140.setGeometry(QtCore.QRect(10, 60, 191, 20))
        self.label_140.setObjectName(_fromUtf8("label_140"))
        self.label_141 = QtGui.QLabel(self.groupBox_45)
        self.label_141.setGeometry(QtCore.QRect(10, 90, 191, 20))
        self.label_141.setObjectName(_fromUtf8("label_141"))
        self.label_142 = QtGui.QLabel(self.groupBox_45)
        self.label_142.setGeometry(QtCore.QRect(10, 120, 191, 20))
        self.label_142.setObjectName(_fromUtf8("label_142"))
        self.label_143 = QtGui.QLabel(self.groupBox_45)
        self.label_143.setGeometry(QtCore.QRect(10, 150, 191, 20))
        self.label_143.setObjectName(_fromUtf8("label_143"))
        self.label_144 = QtGui.QLabel(self.groupBox_45)
        self.label_144.setGeometry(QtCore.QRect(10, 180, 191, 20))
        self.label_144.setObjectName(_fromUtf8("label_144"))
        self.label_145 = QtGui.QLabel(self.groupBox_45)
        self.label_145.setGeometry(QtCore.QRect(10, 210, 191, 20))
        self.label_145.setObjectName(_fromUtf8("label_145"))
        self.label_146 = QtGui.QLabel(self.groupBox_45)
        self.label_146.setGeometry(QtCore.QRect(10, 270, 191, 20))
        self.label_146.setObjectName(_fromUtf8("label_146"))
        self.label_147 = QtGui.QLabel(self.groupBox_45)
        self.label_147.setGeometry(QtCore.QRect(10, 240, 191, 20))
        self.label_147.setObjectName(_fromUtf8("label_147"))
        self.label_193 = QtGui.QLabel(self.groupBox_45)
        self.label_193.setGeometry(QtCore.QRect(10, 300, 191, 20))
        self.label_193.setObjectName(_fromUtf8("label_193"))
        self.tabWidget_6.addTab(self.tab_18, _fromUtf8(""))
        self.tab_29 = QtGui.QWidget()
        self.tab_29.setObjectName(_fromUtf8("tab_29"))
        self.groupBox_47 = QtGui.QGroupBox(self.tab_29)
        self.groupBox_47.setGeometry(QtCore.QRect(10, 10, 761, 521))
        self.groupBox_47.setObjectName(_fromUtf8("groupBox_47"))
        self.pushButton_48 = QtGui.QPushButton(self.groupBox_47)
        self.pushButton_48.setGeometry(QtCore.QRect(30, 50, 161, 41))
        self.pushButton_48.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_48.setObjectName(_fromUtf8("pushButton_48"))
        self.tableWidget_21 = QtGui.QTableWidget(self.groupBox_47)
        self.tableWidget_21.setGeometry(QtCore.QRect(10, 130, 731, 371))
        self.tableWidget_21.setObjectName(_fromUtf8("tableWidget_21"))
        self.tableWidget_21.setColumnCount(7)
        self.tableWidget_21.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(6, item)
        self.groupBox_48 = QtGui.QGroupBox(self.tab_29)
        self.groupBox_48.setGeometry(QtCore.QRect(790, 10, 431, 201))
        self.groupBox_48.setObjectName(_fromUtf8("groupBox_48"))
        self.pushButton_49 = QtGui.QPushButton(self.groupBox_48)
        self.pushButton_49.setGeometry(QtCore.QRect(120, 80, 171, 41))
        self.pushButton_49.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_49.setObjectName(_fromUtf8("pushButton_49"))
        self.tabWidget_6.addTab(self.tab_29, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 521, 551))
        self.groupBox_6.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.lineEdit_37 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_37.setGeometry(QtCore.QRect(120, 20, 231, 20))
        self.lineEdit_37.setText(_fromUtf8(""))
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.label_93 = QtGui.QLabel(self.groupBox_6)
        self.label_93.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_93.setObjectName(_fromUtf8("label_93"))
        self.label_97 = QtGui.QLabel(self.groupBox_6)
        self.label_97.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_97.setObjectName(_fromUtf8("label_97"))
        self.lineEdit_52 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_52.setGeometry(QtCore.QRect(120, 50, 231, 20))
        self.lineEdit_52.setText(_fromUtf8(""))
        self.lineEdit_52.setObjectName(_fromUtf8("lineEdit_52"))
        self.label_100 = QtGui.QLabel(self.groupBox_6)
        self.label_100.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_100.setObjectName(_fromUtf8("label_100"))
        self.lineEdit_67 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_67.setGeometry(QtCore.QRect(120, 110, 231, 20))
        self.lineEdit_67.setText(_fromUtf8(""))
        self.lineEdit_67.setObjectName(_fromUtf8("lineEdit_67"))
        self.label_101 = QtGui.QLabel(self.groupBox_6)
        self.label_101.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_101.setObjectName(_fromUtf8("label_101"))
        self.lineEdit_68 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_68.setGeometry(QtCore.QRect(120, 80, 231, 20))
        self.lineEdit_68.setText(_fromUtf8(""))
        self.lineEdit_68.setObjectName(_fromUtf8("lineEdit_68"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 20, 131, 41))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tableWidget_13 = QtGui.QTableWidget(self.groupBox_6)
        self.tableWidget_13.setGeometry(QtCore.QRect(10, 230, 501, 311))
        self.tableWidget_13.setObjectName(_fromUtf8("tableWidget_13"))
        self.tableWidget_13.setColumnCount(4)
        self.tableWidget_13.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, item)
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 70, 131, 41))
        self.pushButton_8.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lineEdit_77 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_77.setGeometry(QtCore.QRect(120, 140, 231, 20))
        self.lineEdit_77.setText(_fromUtf8(""))
        self.lineEdit_77.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_77.setObjectName(_fromUtf8("lineEdit_77"))
        self.pushButton_32 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_32.setGeometry(QtCore.QRect(370, 150, 131, 41))
        self.pushButton_32.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.label_112 = QtGui.QLabel(self.groupBox_6)
        self.label_112.setGeometry(QtCore.QRect(10, 140, 91, 16))
        self.label_112.setObjectName(_fromUtf8("label_112"))
        self.lineEdit_78 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_78.setGeometry(QtCore.QRect(120, 170, 231, 20))
        self.lineEdit_78.setText(_fromUtf8(""))
        self.lineEdit_78.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_78.setObjectName(_fromUtf8("lineEdit_78"))
        self.label_113 = QtGui.QLabel(self.groupBox_6)
        self.label_113.setGeometry(QtCore.QRect(10, 170, 91, 16))
        self.label_113.setObjectName(_fromUtf8("label_113"))
        self.label_29 = QtGui.QLabel(self.groupBox_6)
        self.label_29.setGeometry(QtCore.QRect(110, 200, 281, 31))
        self.label_29.setStyleSheet(_fromUtf8("color:red;"))
        self.label_29.setText(_fromUtf8(""))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_7.setGeometry(QtCore.QRect(540, 10, 351, 551))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 20, 131, 41))
        self.pushButton_6.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}\n"
""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_98 = QtGui.QLabel(self.groupBox_7)
        self.label_98.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_98.setObjectName(_fromUtf8("label_98"))
        self.lineEdit_53 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_53.setGeometry(QtCore.QRect(120, 70, 211, 20))
        self.lineEdit_53.setText(_fromUtf8(""))
        self.lineEdit_53.setObjectName(_fromUtf8("lineEdit_53"))
        self.lineEdit_69 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_69.setGeometry(QtCore.QRect(120, 100, 211, 20))
        self.lineEdit_69.setText(_fromUtf8(""))
        self.lineEdit_69.setObjectName(_fromUtf8("lineEdit_69"))
        self.lineEdit_70 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_70.setGeometry(QtCore.QRect(120, 130, 211, 20))
        self.lineEdit_70.setText(_fromUtf8(""))
        self.lineEdit_70.setObjectName(_fromUtf8("lineEdit_70"))
        self.label_102 = QtGui.QLabel(self.groupBox_7)
        self.label_102.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label_102.setObjectName(_fromUtf8("label_102"))
        self.label_103 = QtGui.QLabel(self.groupBox_7)
        self.label_103.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_103.setObjectName(_fromUtf8("label_103"))
        self.tableWidget_15 = QtGui.QTableWidget(self.groupBox_7)
        self.tableWidget_15.setGeometry(QtCore.QRect(10, 230, 331, 311))
        self.tableWidget_15.setObjectName(_fromUtf8("tableWidget_15"))
        self.tableWidget_15.setColumnCount(3)
        self.tableWidget_15.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(2, item)
        self.comboBox = QtGui.QComboBox(self.groupBox_7)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_8.setGeometry(QtCore.QRect(900, 10, 351, 301))
        self.groupBox_8.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_99 = QtGui.QLabel(self.groupBox_8)
        self.label_99.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_99.setObjectName(_fromUtf8("label_99"))
        self.lineEdit_66 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_66.setGeometry(QtCore.QRect(120, 30, 221, 20))
        self.lineEdit_66.setText(_fromUtf8(""))
        self.lineEdit_66.setObjectName(_fromUtf8("lineEdit_66"))
        self.label_104 = QtGui.QLabel(self.groupBox_8)
        self.label_104.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_104.setObjectName(_fromUtf8("label_104"))
        self.lineEdit_71 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_71.setGeometry(QtCore.QRect(120, 90, 221, 20))
        self.lineEdit_71.setText(_fromUtf8(""))
        self.lineEdit_71.setObjectName(_fromUtf8("lineEdit_71"))
        self.lineEdit_72 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_72.setGeometry(QtCore.QRect(120, 120, 221, 20))
        self.lineEdit_72.setText(_fromUtf8(""))
        self.lineEdit_72.setObjectName(_fromUtf8("lineEdit_72"))
        self.lineEdit_73 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_73.setGeometry(QtCore.QRect(120, 60, 221, 20))
        self.lineEdit_73.setText(_fromUtf8(""))
        self.lineEdit_73.setObjectName(_fromUtf8("lineEdit_73"))
        self.label_105 = QtGui.QLabel(self.groupBox_8)
        self.label_105.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_105.setObjectName(_fromUtf8("label_105"))
        self.label_106 = QtGui.QLabel(self.groupBox_8)
        self.label_106.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.label_106.setObjectName(_fromUtf8("label_106"))
        self.label_107 = QtGui.QLabel(self.groupBox_8)
        self.label_107.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_107.setObjectName(_fromUtf8("label_107"))
        self.lineEdit_74 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_74.setGeometry(QtCore.QRect(120, 150, 221, 20))
        self.lineEdit_74.setText(_fromUtf8(""))
        self.lineEdit_74.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_74.setObjectName(_fromUtf8("lineEdit_74"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_8)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 250, 131, 41))
        self.pushButton_7.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_108 = QtGui.QLabel(self.groupBox_8)
        self.label_108.setGeometry(QtCore.QRect(10, 180, 81, 16))
        self.label_108.setObjectName(_fromUtf8("label_108"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox.setGeometry(QtCore.QRect(120, 180, 171, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_28 = QtGui.QLabel(self.groupBox_8)
        self.label_28.setGeometry(QtCore.QRect(40, 210, 281, 31))
        self.label_28.setStyleSheet(_fromUtf8("color:red;"))
        self.label_28.setText(_fromUtf8(""))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_9.setGeometry(QtCore.QRect(900, 320, 351, 241))
        self.groupBox_9.setStyleSheet(_fromUtf8("QLabel {\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit:disabled {\n"
"color:blue;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}\n"
"QLineEdit,QListWidget,QPlainTextEdit :enabled {    \n"
"    color:black;\n"
"       border: 1px solid rgb(0, 0, 0);               \n"
"       border-radius: 3px;                \n"
"     \n"
"\n"
"       selection-background-color: rgb(253, 216, 134);                selection-background-color: rgb(253, 216, 134);    \n"
"\n"
"       font-size: 12px;                font-size: 12px;    \n"
"}"))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_110 = QtGui.QLabel(self.groupBox_9)
        self.label_110.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_110.setObjectName(_fromUtf8("label_110"))
        self.lineEdit_76 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_76.setGeometry(QtCore.QRect(120, 130, 221, 20))
        self.lineEdit_76.setText(_fromUtf8(""))
        self.lineEdit_76.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_76.setObjectName(_fromUtf8("lineEdit_76"))
        self.pushButton_31 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_31.setGeometry(QtCore.QRect(120, 190, 131, 41))
        self.pushButton_31.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"color: black;\n"
"background-color: grey;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( );\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.label_111 = QtGui.QLabel(self.groupBox_9)
        self.label_111.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_111.setObjectName(_fromUtf8("label_111"))
        self.label_27 = QtGui.QLabel(self.groupBox_9)
        self.label_27.setGeometry(QtCore.QRect(50, 160, 281, 21))
        self.label_27.setStyleSheet(_fromUtf8("color:red;"))
        self.label_27.setText(_fromUtf8(""))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_9)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 30, 131, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.label_38 = QtGui.QLabel(self.centralWidget)
        self.label_38.setGeometry(QtCore.QRect(30, 10, 311, 21))
        self.label_38.setStyleSheet(_fromUtf8("color:red;"))
        self.label_38.setText(_fromUtf8(""))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_149 = QtGui.QLabel(self.centralWidget)
        self.label_149.setGeometry(QtCore.QRect(430, 690, 321, 16))
        self.label_149.setObjectName(_fromUtf8("label_149"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralWidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(1120, 40, 172, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.label.setBuddy(self.label)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(5)
        self.tabWidget_5.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(2)
        self.tabWidget_6.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_3, self.plainTextEdit_4)
        MainWindow.setTabOrder(self.plainTextEdit_4, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_14)
        MainWindow.setTabOrder(self.lineEdit_14, self.plainTextEdit_5)
        MainWindow.setTabOrder(self.plainTextEdit_5, self.lineEdit_17)
        MainWindow.setTabOrder(self.lineEdit_17, self.lineEdit_18)
        MainWindow.setTabOrder(self.lineEdit_18, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.plainTextEdit_17)
        MainWindow.setTabOrder(self.plainTextEdit_17, self.lineEdit_98)
        MainWindow.setTabOrder(self.lineEdit_98, self.comboBox_15)
        MainWindow.setTabOrder(self.comboBox_15, self.plainTextEdit_18)
        MainWindow.setTabOrder(self.plainTextEdit_18, self.pushButton_56)
        MainWindow.setTabOrder(self.pushButton_56, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_57)
        MainWindow.setTabOrder(self.pushButton_57, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.comboBox_14)
        MainWindow.setTabOrder(self.comboBox_14, self.plainTextEdit_9)
        MainWindow.setTabOrder(self.plainTextEdit_9, self.lineEdit_96)
        MainWindow.setTabOrder(self.lineEdit_96, self.lineEdit_95)
        MainWindow.setTabOrder(self.lineEdit_95, self.plainTextEdit_16)
        MainWindow.setTabOrder(self.plainTextEdit_16, self.lineEdit_94)
        MainWindow.setTabOrder(self.lineEdit_94, self.lineEdit_97)
        MainWindow.setTabOrder(self.lineEdit_97, self.plainTextEdit_19)
        MainWindow.setTabOrder(self.plainTextEdit_19, self.lineEdit_99)
        MainWindow.setTabOrder(self.lineEdit_99, self.comboBox_16)
        MainWindow.setTabOrder(self.comboBox_16, self.plainTextEdit_20)
        MainWindow.setTabOrder(self.plainTextEdit_20, self.comboBox_22)
        MainWindow.setTabOrder(self.comboBox_22, self.lineEdit_100)
        MainWindow.setTabOrder(self.lineEdit_100, self.pushButton_54)
        MainWindow.setTabOrder(self.pushButton_54, self.pushButton_55)
        MainWindow.setTabOrder(self.pushButton_55, self.lineEdit_27)
        MainWindow.setTabOrder(self.lineEdit_27, self.comboBox_23)
        MainWindow.setTabOrder(self.comboBox_23, self.lineEdit_38)
        MainWindow.setTabOrder(self.lineEdit_38, self.lineEdit_39)
        MainWindow.setTabOrder(self.lineEdit_39, self.plainTextEdit_10)
        MainWindow.setTabOrder(self.plainTextEdit_10, self.lineEdit_32)
        MainWindow.setTabOrder(self.lineEdit_32, self.lineEdit_33)
        MainWindow.setTabOrder(self.lineEdit_33, self.lineEdit_34)
        MainWindow.setTabOrder(self.lineEdit_34, self.lineEdit_35)
        MainWindow.setTabOrder(self.lineEdit_35, self.lineEdit_29)
        MainWindow.setTabOrder(self.lineEdit_29, self.lineEdit_28)
        MainWindow.setTabOrder(self.lineEdit_28, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.lineEdit_30)
        MainWindow.setTabOrder(self.lineEdit_30, self.lineEdit_51)
        MainWindow.setTabOrder(self.lineEdit_51, self.lineEdit_31)
        MainWindow.setTabOrder(self.lineEdit_31, self.pushButton_43)
        MainWindow.setTabOrder(self.pushButton_43, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.comboBox_6)
        MainWindow.setTabOrder(self.comboBox_6, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_19)
        MainWindow.setTabOrder(self.lineEdit_19, self.plainTextEdit)
        MainWindow.setTabOrder(self.plainTextEdit, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_12)
        MainWindow.setTabOrder(self.lineEdit_12, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_15)
        MainWindow.setTabOrder(self.lineEdit_15, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.plainTextEdit_2)
        MainWindow.setTabOrder(self.plainTextEdit_2, self.pushButton_58)
        MainWindow.setTabOrder(self.pushButton_58, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.comboBox_17)
        MainWindow.setTabOrder(self.comboBox_17, self.dateEdit_19)
        MainWindow.setTabOrder(self.dateEdit_19, self.lineEdit_64)
        MainWindow.setTabOrder(self.lineEdit_64, self.lineEdit_62)
        MainWindow.setTabOrder(self.lineEdit_62, self.lineEdit_56)
        MainWindow.setTabOrder(self.lineEdit_56, self.lineEdit_57)
        MainWindow.setTabOrder(self.lineEdit_57, self.lineEdit_58)
        MainWindow.setTabOrder(self.lineEdit_58, self.lineEdit_59)
        MainWindow.setTabOrder(self.lineEdit_59, self.lineEdit_61)
        MainWindow.setTabOrder(self.lineEdit_61, self.lineEdit_60)
        MainWindow.setTabOrder(self.lineEdit_60, self.lineEdit_55)
        MainWindow.setTabOrder(self.lineEdit_55, self.lineEdit_54)
        MainWindow.setTabOrder(self.lineEdit_54, self.plainTextEdit_13)
        MainWindow.setTabOrder(self.plainTextEdit_13, self.plainTextEdit_12)
        MainWindow.setTabOrder(self.plainTextEdit_12, self.lineEdit_63)
        MainWindow.setTabOrder(self.lineEdit_63, self.lineEdit_65)
        MainWindow.setTabOrder(self.lineEdit_65, self.pushButton_61)
        MainWindow.setTabOrder(self.pushButton_61, self.pushButton_39)
        MainWindow.setTabOrder(self.pushButton_39, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.comboBox_18)
        MainWindow.setTabOrder(self.comboBox_18, self.lineEdit_43)
        MainWindow.setTabOrder(self.lineEdit_43, self.dateEdit_20)
        MainWindow.setTabOrder(self.dateEdit_20, self.plainTextEdit_14)
        MainWindow.setTabOrder(self.plainTextEdit_14, self.plainTextEdit_11)
        MainWindow.setTabOrder(self.plainTextEdit_11, self.lineEdit_40)
        MainWindow.setTabOrder(self.lineEdit_40, self.lineEdit_36)
        MainWindow.setTabOrder(self.lineEdit_36, self.lineEdit_42)
        MainWindow.setTabOrder(self.lineEdit_42, self.lineEdit_41)
        MainWindow.setTabOrder(self.lineEdit_41, self.lineEdit_44)
        MainWindow.setTabOrder(self.lineEdit_44, self.lineEdit_45)
        MainWindow.setTabOrder(self.lineEdit_45, self.lineEdit_49)
        MainWindow.setTabOrder(self.lineEdit_49, self.lineEdit_48)
        MainWindow.setTabOrder(self.lineEdit_48, self.lineEdit_47)
        MainWindow.setTabOrder(self.lineEdit_47, self.lineEdit_46)
        MainWindow.setTabOrder(self.lineEdit_46, self.lineEdit_50)
        MainWindow.setTabOrder(self.lineEdit_50, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.tableWidget_2)
        MainWindow.setTabOrder(self.tableWidget_2, self.comboBox_7)
        MainWindow.setTabOrder(self.comboBox_7, self.lineEdit_20)
        MainWindow.setTabOrder(self.lineEdit_20, self.pushButton_40)
        MainWindow.setTabOrder(self.pushButton_40, self.commandLinkButton_2)
        MainWindow.setTabOrder(self.commandLinkButton_2, self.tableWidget_17)
        MainWindow.setTabOrder(self.tableWidget_17, self.tableWidget_19)
        MainWindow.setTabOrder(self.tableWidget_19, self.tableWidget_3)
        MainWindow.setTabOrder(self.tableWidget_3, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.dateEdit_2)
        MainWindow.setTabOrder(self.dateEdit_2, self.comboBox_8)
        MainWindow.setTabOrder(self.comboBox_8, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.tableWidget_4)
        MainWindow.setTabOrder(self.tableWidget_4, self.dateEdit_3)
        MainWindow.setTabOrder(self.dateEdit_3, self.dateEdit_4)
        MainWindow.setTabOrder(self.dateEdit_4, self.comboBox_9)
        MainWindow.setTabOrder(self.comboBox_9, self.pushButton_15)
        MainWindow.setTabOrder(self.pushButton_15, self.pushButton_16)
        MainWindow.setTabOrder(self.pushButton_16, self.tableWidget_5)
        MainWindow.setTabOrder(self.tableWidget_5, self.dateEdit_5)
        MainWindow.setTabOrder(self.dateEdit_5, self.dateEdit_6)
        MainWindow.setTabOrder(self.dateEdit_6, self.comboBox_10)
        MainWindow.setTabOrder(self.comboBox_10, self.pushButton_17)
        MainWindow.setTabOrder(self.pushButton_17, self.tableWidget_6)
        MainWindow.setTabOrder(self.tableWidget_6, self.pushButton_18)
        MainWindow.setTabOrder(self.pushButton_18, self.dateEdit_7)
        MainWindow.setTabOrder(self.dateEdit_7, self.dateEdit_8)
        MainWindow.setTabOrder(self.dateEdit_8, self.comboBox_11)
        MainWindow.setTabOrder(self.comboBox_11, self.pushButton_19)
        MainWindow.setTabOrder(self.pushButton_19, self.tableWidget_7)
        MainWindow.setTabOrder(self.tableWidget_7, self.pushButton_20)
        MainWindow.setTabOrder(self.pushButton_20, self.lineEdit_91)
        MainWindow.setTabOrder(self.lineEdit_91, self.lineEdit_93)
        MainWindow.setTabOrder(self.lineEdit_93, self.lineEdit_92)
        MainWindow.setTabOrder(self.lineEdit_92, self.pushButton_52)
        MainWindow.setTabOrder(self.pushButton_52, self.lineEdit_101)
        MainWindow.setTabOrder(self.lineEdit_101, self.lineEdit_102)
        MainWindow.setTabOrder(self.lineEdit_102, self.lineEdit_103)
        MainWindow.setTabOrder(self.lineEdit_103, self.dateEdit_21)
        MainWindow.setTabOrder(self.dateEdit_21, self.dateEdit_27)
        MainWindow.setTabOrder(self.dateEdit_27, self.pushButton_62)
        MainWindow.setTabOrder(self.pushButton_62, self.tableWidget_22)
        MainWindow.setTabOrder(self.tableWidget_22, self.pushButton_53)
        MainWindow.setTabOrder(self.pushButton_53, self.dateEdit_9)
        MainWindow.setTabOrder(self.dateEdit_9, self.dateEdit_10)
        MainWindow.setTabOrder(self.dateEdit_10, self.pushButton_21)
        MainWindow.setTabOrder(self.pushButton_21, self.tableWidget_8)
        MainWindow.setTabOrder(self.tableWidget_8, self.pushButton_22)
        MainWindow.setTabOrder(self.pushButton_22, self.dateEdit_11)
        MainWindow.setTabOrder(self.dateEdit_11, self.lineEdit_21)
        MainWindow.setTabOrder(self.lineEdit_21, self.lineEdit_22)
        MainWindow.setTabOrder(self.lineEdit_22, self.plainTextEdit_3)
        MainWindow.setTabOrder(self.plainTextEdit_3, self.lineEdit_24)
        MainWindow.setTabOrder(self.lineEdit_24, self.lineEdit_25)
        MainWindow.setTabOrder(self.lineEdit_25, self.pushButton_44)
        MainWindow.setTabOrder(self.pushButton_44, self.pushButton_60)
        MainWindow.setTabOrder(self.pushButton_60, self.dateEdit_17)
        MainWindow.setTabOrder(self.dateEdit_17, self.dateEdit_22)
        MainWindow.setTabOrder(self.dateEdit_22, self.pushButton_45)
        MainWindow.setTabOrder(self.pushButton_45, self.tableWidget_20)
        MainWindow.setTabOrder(self.tableWidget_20, self.pushButton_46)
        MainWindow.setTabOrder(self.pushButton_46, self.dateEdit_12)
        MainWindow.setTabOrder(self.dateEdit_12, self.comboBox_19)
        MainWindow.setTabOrder(self.comboBox_19, self.pushButton_23)
        MainWindow.setTabOrder(self.pushButton_23, self.tableWidget_9)
        MainWindow.setTabOrder(self.tableWidget_9, self.pushButton_24)
        MainWindow.setTabOrder(self.pushButton_24, self.dateEdit_13)
        MainWindow.setTabOrder(self.dateEdit_13, self.comboBox_20)
        MainWindow.setTabOrder(self.comboBox_20, self.pushButton_25)
        MainWindow.setTabOrder(self.pushButton_25, self.tableWidget_10)
        MainWindow.setTabOrder(self.tableWidget_10, self.pushButton_26)
        MainWindow.setTabOrder(self.pushButton_26, self.comboBox_21)
        MainWindow.setTabOrder(self.comboBox_21, self.pushButton_28)
        MainWindow.setTabOrder(self.pushButton_28, self.tableWidget_11)
        MainWindow.setTabOrder(self.tableWidget_11, self.pushButton_27)
        MainWindow.setTabOrder(self.pushButton_27, self.dateEdit_15)
        MainWindow.setTabOrder(self.dateEdit_15, self.dateEdit_24)
        MainWindow.setTabOrder(self.dateEdit_24, self.pushButton_30)
        MainWindow.setTabOrder(self.pushButton_30, self.tableWidget_12)
        MainWindow.setTabOrder(self.tableWidget_12, self.pushButton_29)
        MainWindow.setTabOrder(self.pushButton_29, self.dateEdit_16)
        MainWindow.setTabOrder(self.dateEdit_16, self.dateEdit_25)
        MainWindow.setTabOrder(self.dateEdit_25, self.pushButton_35)
        MainWindow.setTabOrder(self.pushButton_35, self.tableWidget_16)
        MainWindow.setTabOrder(self.tableWidget_16, self.pushButton_36)
        MainWindow.setTabOrder(self.pushButton_36, self.dateEdit_18)
        MainWindow.setTabOrder(self.dateEdit_18, self.dateEdit_26)
        MainWindow.setTabOrder(self.dateEdit_26, self.pushButton_37)
        MainWindow.setTabOrder(self.pushButton_37, self.tableWidget_18)
        MainWindow.setTabOrder(self.tableWidget_18, self.pushButton_38)
        MainWindow.setTabOrder(self.pushButton_38, self.pushButton_33)
        MainWindow.setTabOrder(self.pushButton_33, self.tableWidget_14)
        MainWindow.setTabOrder(self.tableWidget_14, self.pushButton_34)
        MainWindow.setTabOrder(self.pushButton_34, self.lineEdit_16)
        MainWindow.setTabOrder(self.lineEdit_16, self.pushButton_42)
        MainWindow.setTabOrder(self.pushButton_42, self.pushButton_41)
        MainWindow.setTabOrder(self.pushButton_41, self.lineEdit_23)
        MainWindow.setTabOrder(self.lineEdit_23, self.plainTextEdit_6)
        MainWindow.setTabOrder(self.plainTextEdit_6, self.lineEdit_79)
        MainWindow.setTabOrder(self.lineEdit_79, self.comboBox_12)
        MainWindow.setTabOrder(self.comboBox_12, self.pushButton_47)
        MainWindow.setTabOrder(self.pushButton_47, self.pushButton_59)
        MainWindow.setTabOrder(self.pushButton_59, self.pushButton_48)
        MainWindow.setTabOrder(self.pushButton_48, self.tableWidget_21)
        MainWindow.setTabOrder(self.tableWidget_21, self.pushButton_49)
        MainWindow.setTabOrder(self.pushButton_49, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.lineEdit_77)
        MainWindow.setTabOrder(self.lineEdit_77, self.lineEdit_78)
        MainWindow.setTabOrder(self.lineEdit_78, self.pushButton_32)
        MainWindow.setTabOrder(self.pushButton_32, self.lineEdit_37)
        MainWindow.setTabOrder(self.lineEdit_37, self.lineEdit_52)
        MainWindow.setTabOrder(self.lineEdit_52, self.lineEdit_68)
        MainWindow.setTabOrder(self.lineEdit_68, self.lineEdit_67)
        MainWindow.setTabOrder(self.lineEdit_67, self.tableWidget_13)
        MainWindow.setTabOrder(self.tableWidget_13, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.lineEdit_53)
        MainWindow.setTabOrder(self.lineEdit_53, self.lineEdit_69)
        MainWindow.setTabOrder(self.lineEdit_69, self.lineEdit_70)
        MainWindow.setTabOrder(self.lineEdit_70, self.tableWidget_15)
        MainWindow.setTabOrder(self.tableWidget_15, self.lineEdit_66)
        MainWindow.setTabOrder(self.lineEdit_66, self.lineEdit_73)
        MainWindow.setTabOrder(self.lineEdit_73, self.lineEdit_71)
        MainWindow.setTabOrder(self.lineEdit_71, self.lineEdit_72)
        MainWindow.setTabOrder(self.lineEdit_72, self.lineEdit_74)
        MainWindow.setTabOrder(self.lineEdit_74, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.lineEdit_76)
        MainWindow.setTabOrder(self.lineEdit_76, self.pushButton_31)
        MainWindow.setTabOrder(self.pushButton_31, self.tabWidget_5)
        MainWindow.setTabOrder(self.tabWidget_5, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.commandLinkButton)
        MainWindow.setTabOrder(self.commandLinkButton, self.tabWidget_4)
        MainWindow.setTabOrder(self.tabWidget_4, self.tabWidget_3)
        MainWindow.setTabOrder(self.tabWidget_3, self.tabWidget_6)
        MainWindow.setTabOrder(self.tabWidget_6, self.tabWidget_2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_21.setText(_translate("MainWindow", "Name  <span style=\"color: red\">*</span>", None))
        self.label_22.setText(_translate("MainWindow", "NIC Number <span style=\"color: red\">*</span>", None))
        self.label_23.setText(_translate("MainWindow", "Telephone number <span style=\"color: red\">*</span>", None))
        self.label_24.setText(_translate("MainWindow", "Address  <span style=\"color: red\">*</span>", None))
        self.label_25.setText(_translate("MainWindow", "Age  <span style=\"color: red\">*</span>", None))
        self.label_26.setText(_translate("MainWindow", "Occupation  <span style=\"color: red\">*</span>", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Add Customer", None))
        self.pushButton_3.setText(_translate("MainWindow", "Submit Customer Data", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mr.", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Mrs.", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Miss.", None))
        self.label_184.setText(_translate("MainWindow", "Office Phone", None))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "Mrs.", None))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "Mr.", None))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "Miss.", None))
        self.label_185.setText(_translate("MainWindow", "Spouse", None))
        self.pushButton_56.setText(_translate("MainWindow", "Select Image", None))
        self.pushButton_57.setText(_translate("MainWindow", "Clear All", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Printout", None))
        self.pushButton_4.setText(_translate("MainWindow", "Print Current Customer Data", None))
        self.label_183.setText(_translate("MainWindow", "Office Address  ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Data Entry", None))
        self.label_176.setText(_translate("MainWindow", "Occupation  <span style=\"color: red\">*</span>", None))
        self.groupBox_53.setTitle(_translate("MainWindow", "Add Guarantor", None))
        self.pushButton_54.setText(_translate("MainWindow", "Submit Guaranter Data", None))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "Mr.", None))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "Mrs.", None))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "Miss.", None))
        self.label_186.setText(_translate("MainWindow", "Office Phone  ", None))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "Mrs.", None))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "Mr.", None))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "Miss.", None))
        self.label_187.setText(_translate("MainWindow", "Spouse  ", None))
        self.lineEdit_100.setText(_translate("MainWindow", "MT/DL/", None))
        self.label_191.setText(_translate("MainWindow", "Loan Number <span style=\"color: red\">*</span>", None))
        self.comboBox_22.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_22.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_22.setItemText(2, _translate("MainWindow", "Daily", None))
        self.pushButton_55.setText(_translate("MainWindow", "Clear All", None))
        self.label_178.setText(_translate("MainWindow", "Age  <span style=\"color: red\">*</span>", None))
        self.label_188.setText(_translate("MainWindow", "Office Address  ", None))
        self.label_179.setText(_translate("MainWindow", "Name  <span style=\"color: red\">*</span>", None))
        self.label_180.setText(_translate("MainWindow", "Address  <span style=\"color: red\">*</span>", None))
        self.label_181.setText(_translate("MainWindow", "NIC Number <span style=\"color: red\">*</span>", None))
        self.label_182.setText(_translate("MainWindow", "Telephone number <span style=\"color: red\">*</span>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Guarantor File", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Delete Loan", None))
        self.label_39.setText(_translate("MainWindow", "Loan Number <span style=\"color: red\">*</span>", None))
        self.lineEdit_27.setText(_translate("MainWindow", "MT/DL/", None))
        self.label_40.setText(_translate("MainWindow", "NIC No ", None))
        self.label_49.setText(_translate("MainWindow", "Period M", None))
        self.label_53.setText(_translate("MainWindow", "Name", None))
        self.label_54.setText(_translate("MainWindow", "Total Amount", None))
        self.label_55.setText(_translate("MainWindow", "Loan Amount", None))
        self.label_56.setText(_translate("MainWindow", "Total Paid", None))
        self.label_57.setText(_translate("MainWindow", "Balance", None))
        self.label_41.setText(_translate("MainWindow", "Username  <span style=\"color: red\">*</span>", None))
        self.label_42.setText(_translate("MainWindow", "Password  <span style=\"color: red\">*</span>", None))
        self.pushButton_9.setText(_translate("MainWindow", "Cancel Loan", None))
        self.comboBox_23.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_23.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_23.setItemText(2, _translate("MainWindow", "Daily", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Cancel Loan", None))
        self.groupBox_40.setTitle(_translate("MainWindow", "Delete Loan", None))
        self.label_117.setText(_translate("MainWindow", "Loan Number <span style=\"color: red\">*</span>", None))
        self.label_118.setText(_translate("MainWindow", "Password  <span style=\"color: red\">*</span>", None))
        self.label_119.setText(_translate("MainWindow", "Username  <span style=\"color: red\">*</span>", None))
        self.pushButton_43.setText(_translate("MainWindow", "Delete Loan", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Delete Loan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tjj), _translate("MainWindow", "Main Data file", None))
        self.groupBox.setTitle(_translate("MainWindow", "Data Entry", None))
        self.label_2.setText(_translate("MainWindow", "Loan No <span style=\"color: red\">*</span>", None))
        self.label_3.setText(_translate("MainWindow", "Period <span style=\"color: red\">*</span>", None))
        self.label_4.setText(_translate("MainWindow", "Name <span style=\"color: red\">*</span>", None))
        self.label_5.setText(_translate("MainWindow", "Purpose", None))
        self.label_6.setText(_translate("MainWindow", "Loan Amount <span style=\"color: red\">*</span>", None))
        self.label_7.setText(_translate("MainWindow", "TT/NSL (%)", None))
        self.label_8.setText(_translate("MainWindow", "Total Amount <span style=\"color: red\">*</span>", None))
        self.label_9.setText(_translate("MainWindow", "Inst. No <span style=\"color: red\">*</span>", None))
        self.label_10.setText(_translate("MainWindow", "(Less) Inst.Value X Bal. Inst <span style=\"color: red\">*</span>", None))
        self.label_11.setText(_translate("MainWindow", "Inst. Value <span style=\"color: red\">*</span>", None))
        self.label_12.setText(_translate("MainWindow", "Inv. Chrages", None))
        self.label_13.setText(_translate("MainWindow", "Part Payment", None))
        self.label_14.setText(_translate("MainWindow", "Initial Inst. <span style=\"color: red\">*</span>", None))
        self.lineEdit_8.setText(_translate("MainWindow", "3", None))
        self.label_15.setText(_translate("MainWindow", "Interest Rate <span style=\"color: red\">*</span>", None))
        self.label_16.setText(_translate("MainWindow", "Interest <span style=\"color: red\">*</span>", None))
        self.label_17.setText(_translate("MainWindow", "Stamps", None))
        self.label_18.setText(_translate("MainWindow", "Collection <span style=\"color: red\">*</span>", None))
        self.label_19.setText(_translate("MainWindow", "Total <span style=\"color: red\">*</span>", None))
        self.pushButton.setText(_translate("MainWindow", "Submit Work Sheet", None))
        self.label_20.setText(_translate("MainWindow", "NIC No <span style=\"color: red\">*</span>", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Daily", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "6%", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "3 Months", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "6 Months", None))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "12 Months", None))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "18 Months", None))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "24 Months", None))
        self.pushButton_58.setText(_translate("MainWindow", "Clear All", None))
        self.label_155.setText(_translate("MainWindow", "Pay Date", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Printout", None))
        self.pushButton_2.setText(_translate("MainWindow", "Print Current Work Sheet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Work Sheet", None))
        self.groupBox_13.setTitle(_translate("MainWindow", " Receipt Entry", None))
        self.label_64.setText(_translate("MainWindow", "Date", None))
        self.label_65.setText(_translate("MainWindow", "Name", None))
        self.label_66.setText(_translate("MainWindow", "Address", None))
        self.label_67.setText(_translate("MainWindow", "Installment", None))
        self.label_68.setText(_translate("MainWindow", "Arreas", None))
        self.label_69.setText(_translate("MainWindow", "Default Charges", None))
        self.label_70.setText(_translate("MainWindow", "Down Payment", None))
        self.label_71.setText(_translate("MainWindow", "Inv.Charges", None))
        self.label_72.setText(_translate("MainWindow", "D / C", None))
        self.label_73.setText(_translate("MainWindow", "Total Payment", None))
        self.label_74.setText(_translate("MainWindow", "Stamp Fees", None))
        self.label_75.setText(_translate("MainWindow", "T / R No", None))
        self.label_76.setText(_translate("MainWindow", "R / No", None))
        self.label_77.setText(_translate("MainWindow", "Loan Number <span style=\"color: red\">*</span>", None))
        self.lineEdit_64.setText(_translate("MainWindow", "MT/DL/", None))
        self.label_78.setText(_translate("MainWindow", "Cashier", None))
        self.pushButton_11.setText(_translate("MainWindow", "Add and Print Receipt", None))
        self.dateEdit_19.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_39.setText(_translate("MainWindow", "Add Receipt", None))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_17.setItemText(2, _translate("MainWindow", "Daily", None))
        self.pushButton_61.setText(_translate("MainWindow", "Clear All", None))
        self.label_150.setText(_translate("MainWindow", "Part Payment", None))
        self.label_152.setText(_translate("MainWindow", "Last Paid", None))
        self.label_156.setText(_translate("MainWindow", "Pay Dates", None))
        self.label_157.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_20), _translate("MainWindow", "Receipt", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Debtors Card", None))
        self.label_43.setText(_translate("MainWindow", "Date", None))
        self.label_44.setText(_translate("MainWindow", "Name", None))
        self.label_45.setText(_translate("MainWindow", "T.P Number", None))
        self.label_46.setText(_translate("MainWindow", "Address", None))
        self.label_47.setText(_translate("MainWindow", "Loan Value", None))
        self.label_48.setText(_translate("MainWindow", "Article", None))
        self.label_50.setText(_translate("MainWindow", "Period", None))
        self.lineEdit_43.setText(_translate("MainWindow", "MT/DL/", None))
        self.label_51.setText(_translate("MainWindow", "Contract No <span style=\"color: red\">*</span>", None))
        self.label_52.setText(_translate("MainWindow", "P.Payment", None))
        self.label_58.setText(_translate("MainWindow", "Total Amount", None))
        self.label_59.setText(_translate("MainWindow", "Installment", None))
        self.label_60.setText(_translate("MainWindow", "Init.Installment", None))
        self.label_61.setText(_translate("MainWindow", "B.T.T / VAT", None))
        self.label_62.setText(_translate("MainWindow", "Interest", None))
        self.label_63.setText(_translate("MainWindow", "Balance", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Receipt No.", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Monthly Rental", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Default Interest", None))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Balance", None))
        self.pushButton_10.setText(_translate("MainWindow", "Print Debtors Card", None))
        self.dateEdit_20.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_18.setItemText(2, _translate("MainWindow", "Daily", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Debtors Card", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Search Loan or Customer", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Loan No.", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "NIC No.", None))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Customer Name", None))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Loan Date (eg. 2016-12-01)", None))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Guaranters (Search By Loan No)", None))
        self.label_94.setText(_translate("MainWindow", "Search by ", None))
        self.pushButton_40.setText(_translate("MainWindow", "Search", None))
        item = self.tableWidget_17.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan No", None))
        item = self.tableWidget_17.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_17.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Interest Rate", None))
        item = self.tableWidget_17.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Amount", None))
        item = self.tableWidget_17.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Installment No", None))
        item = self.tableWidget_17.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Purpose", None))
        item = self.tableWidget_17.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Collection", None))
        item = self.tableWidget_17.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Balance", None))
        item = self.tableWidget_19.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Customer Name", None))
        item = self.tableWidget_19.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NIC No", None))
        item = self.tableWidget_19.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.tableWidget_19.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Age", None))
        item = self.tableWidget_19.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Occupation", None))
        item = self.tableWidget_19.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telephone", None))
        item = self.tableWidget_19.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Loan No", None))
        item = self.tableWidget_19.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_19.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Office Address", None))
        item = self.tableWidget_19.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Office TP", None))
        item = self.tableWidget_19.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Spouse", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "View Customer Image", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), _translate("MainWindow", "Search", None))
        self.groupBox_14.setTitle(_translate("MainWindow", "All receipts of today", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Receipt No", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "T/R Number", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Amount", None))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cashier", None))
        self.groupBox_15.setTitle(_translate("MainWindow", "Print Receipt register", None))
        self.pushButton_12.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Day All Receipts", None))
        self.groupBox_16.setTitle(_translate("MainWindow", "Installments", None))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_79.setText(_translate("MainWindow", "From", None))
        self.label_80.setText(_translate("MainWindow", "To", None))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_13.setText(_translate("MainWindow", "Display Installments", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Installment", None))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Loan Date", None))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Paid Installments", None))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Daily", None))
        self.groupBox_17.setTitle(_translate("MainWindow", "Print Installments", None))
        self.pushButton_14.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_19), _translate("MainWindow", "Installment Collectible", None))
        self.groupBox_18.setTitle(_translate("MainWindow", "Interest", None))
        self.dateEdit_3.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_81.setText(_translate("MainWindow", "From", None))
        self.label_82.setText(_translate("MainWindow", "To", None))
        self.dateEdit_4.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_15.setText(_translate("MainWindow", "Display Interests", None))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Interest", None))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Installment", None))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Loan Date", None))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Daily", None))
        self.groupBox_19.setTitle(_translate("MainWindow", "Interest report", None))
        self.pushButton_16.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Interest Collectible", None))
        self.groupBox_20.setTitle(_translate("MainWindow", "Actual Installments", None))
        self.dateEdit_5.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_83.setText(_translate("MainWindow", "From", None))
        self.label_84.setText(_translate("MainWindow", "To", None))
        self.dateEdit_6.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_17.setText(_translate("MainWindow", "Display Installments", None))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Installment", None))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Receipt No", None))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Paid Date", None))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Daily", None))
        self.groupBox_21.setTitle(_translate("MainWindow", "Actual Installments report", None))
        self.pushButton_18.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_21), _translate("MainWindow", "Actual Installment Collections", None))
        self.groupBox_22.setTitle(_translate("MainWindow", "Print Actual Interest Collections report", None))
        self.dateEdit_7.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_85.setText(_translate("MainWindow", "From", None))
        self.label_86.setText(_translate("MainWindow", "To", None))
        self.dateEdit_8.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_19.setText(_translate("MainWindow", "Display Interests", None))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Receipt No", None))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Interest", None))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Installment", None))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Paid Date", None))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "Daily", None))
        self.groupBox_23.setTitle(_translate("MainWindow", "Print Actual Interest Collections report", None))
        self.pushButton_20.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_22), _translate("MainWindow", "Actual Interest Collections", None))
        self.groupBox_49.setTitle(_translate("MainWindow", "Cancel Receipt", None))
        self.label_175.setText(_translate("MainWindow", "Receipt Number <span style=\"color: red\">*</span>", None))
        self.label_194.setText(_translate("MainWindow", "Password  <span style=\"color: red\">*</span>", None))
        self.label_195.setText(_translate("MainWindow", "Username  <span style=\"color: red\">*</span>", None))
        self.pushButton_52.setText(_translate("MainWindow", "Cancel Receipt", None))
        self.label_197.setText(_translate("MainWindow", "Loan Number ", None))
        self.label_198.setText(_translate("MainWindow", "Receipt Total", None))
        self.label_199.setText(_translate("MainWindow", "Receipt Date", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_30), _translate("MainWindow", "Cancel Receipt", None))
        self.groupBox_50.setTitle(_translate("MainWindow", "Print Receipt register", None))
        self.pushButton_53.setText(_translate("MainWindow", "Print Report", None))
        self.groupBox_51.setTitle(_translate("MainWindow", "Cancelled Receipts", None))
        item = self.tableWidget_22.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Receipt No", None))
        item = self.tableWidget_22.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "T/R Number", None))
        item = self.tableWidget_22.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_22.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Amount", None))
        item = self.tableWidget_22.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Receipt date", None))
        item = self.tableWidget_22.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cashier", None))
        self.label_109.setText(_translate("MainWindow", "From", None))
        self.pushButton_62.setText(_translate("MainWindow", "Display Receipts", None))
        self.label_114.setText(_translate("MainWindow", "To", None))
        self.dateEdit_21.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.dateEdit_27.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_31), _translate("MainWindow", "Cancelled Receipts Report", None))
        self.groupBox_24.setTitle(_translate("MainWindow", "Closed Loans", None))
        self.dateEdit_9.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_87.setText(_translate("MainWindow", "From", None))
        self.label_88.setText(_translate("MainWindow", "To", None))
        self.dateEdit_10.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_21.setText(_translate("MainWindow", "Display Closed Loans", None))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Date", None))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Customer Name", None))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Closed Date", None))
        self.groupBox_25.setTitle(_translate("MainWindow", "Print Closed Loans report", None))
        self.pushButton_22.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_23), _translate("MainWindow", "Closing Register", None))
        self.groupBox_41.setTitle(_translate("MainWindow", "Votes", None))
        self.label_121.setText(_translate("MainWindow", "01 - Dealer Payment", None))
        self.label_122.setText(_translate("MainWindow", "02 - Loan", None))
        self.label_123.setText(_translate("MainWindow", "03 - Petty Cash", None))
        self.label_124.setText(_translate("MainWindow", "04 - Salary", None))
        self.label_125.setText(_translate("MainWindow", "05 - Utility Bill", None))
        self.label_126.setText(_translate("MainWindow", "06 - Fuel", None))
        self.label_127.setText(_translate("MainWindow", "07 - Vehicle Maintain", None))
        self.label_128.setText(_translate("MainWindow", "09 - Miscellaneous", None))
        self.label_129.setText(_translate("MainWindow", "08 - Leasing Rental", None))
        self.label_192.setText(_translate("MainWindow", "10 - Transfer Of funds", None))
        self.groupBox_42.setTitle(_translate("MainWindow", "Voucher Entry", None))
        self.label_130.setText(_translate("MainWindow", "Vote No <span style=\"color: red\">*</span>", None))
        self.label_131.setText(_translate("MainWindow", "Date <span style=\"color: red\">*</span>", None))
        self.dateEdit_11.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_132.setText(_translate("MainWindow", "Debit A/C <span style=\"color: red\">*</span>", None))
        self.label_133.setText(_translate("MainWindow", "Desc <span style=\"color: red\">*</span>", None))
        self.label_134.setText(_translate("MainWindow", "Cheque No <span style=\"color: red\">*</span>", None))
        self.label_135.setText(_translate("MainWindow", "Amount <span style=\"color: red\">*</span>", None))
        self.pushButton_44.setText(_translate("MainWindow", "Enter Voucher", None))
        self.pushButton_60.setText(_translate("MainWindow", "Clear All", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_15), _translate("MainWindow", "Data Entry", None))
        self.groupBox_43.setTitle(_translate("MainWindow", "Voucher Report", None))
        self.dateEdit_17.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_137.setText(_translate("MainWindow", "From", None))
        self.label_138.setText(_translate("MainWindow", "To", None))
        self.dateEdit_22.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.pushButton_45.setText(_translate("MainWindow", "Display Vouchers", None))
        item = self.tableWidget_20.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_20.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Voucher No.", None))
        item = self.tableWidget_20.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vote No.", None))
        item = self.tableWidget_20.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description", None))
        item = self.tableWidget_20.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cheque No.", None))
        item = self.tableWidget_20.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Amount", None))
        self.groupBox_44.setTitle(_translate("MainWindow", "Print Voucher Report", None))
        self.pushButton_46.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_16), _translate("MainWindow", "Voucher Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vbnbv), _translate("MainWindow", "Vouchers", None))
        self.groupBox_26.setTitle(_translate("MainWindow", " Loans", None))
        self.label_89.setText(_translate("MainWindow", "Select Month", None))
        self.pushButton_23.setText(_translate("MainWindow", "Display Loans", None))
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Agreement Date", None))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telephone", None))
        item = self.tableWidget_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_9.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date Expire", None))
        self.dateEdit_12.setDisplayFormat(_translate("MainWindow", "M/yyyy", None))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_19.setItemText(2, _translate("MainWindow", "Daily", None))
        self.groupBox_27.setTitle(_translate("MainWindow", " Print Loans Report", None))
        self.pushButton_24.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_24), _translate("MainWindow", "Loan Regitster", None))
        self.groupBox_28.setTitle(_translate("MainWindow", " Loan Accounts", None))
        self.pushButton_25.setText(_translate("MainWindow", "Display Accounts", None))
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Date", None))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Article Value", None))
        item = self.tableWidget_10.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_10.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Installment Value", None))
        item = self.tableWidget_10.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "P/P", None))
        item = self.tableWidget_10.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "D/P", None))
        item = self.tableWidget_10.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Doc. Charge", None))
        item = self.tableWidget_10.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Total D/P", None))
        item = self.tableWidget_10.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Receipt Number", None))
        self.dateEdit_13.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "Daily", None))
        self.dateEdit_35.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_205.setText(_translate("MainWindow", "To", None))
        self.label_162.setText(_translate("MainWindow", "From", None))
        self.groupBox_29.setTitle(_translate("MainWindow", " Print Loan Accounts Report", None))
        self.pushButton_26.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_26), _translate("MainWindow", "Loan Accounts", None))
        self.groupBox_30.setTitle(_translate("MainWindow", "Print Monthly Collections Report", None))
        self.pushButton_27.setText(_translate("MainWindow", "Print Report", None))
        self.groupBox_31.setTitle(_translate("MainWindow", "Monthly Collections", None))
        self.pushButton_28.setText(_translate("MainWindow", "Display Collections", None))
        item = self.tableWidget_11.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_11.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_11.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Init. Installment", None))
        item = self.tableWidget_11.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P/P", None))
        item = self.tableWidget_11.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "D/C", None))
        item = self.tableWidget_11.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Invest. Charges", None))
        item = self.tableWidget_11.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Total D/P", None))
        self.comboBox_21.setItemText(0, _translate("MainWindow", "Monthly", None))
        self.comboBox_21.setItemText(1, _translate("MainWindow", "Weekly", None))
        self.comboBox_21.setItemText(2, _translate("MainWindow", "Daily", None))
        self.dateEdit_36.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_163.setText(_translate("MainWindow", "From", None))
        self.dateEdit_37.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_206.setText(_translate("MainWindow", "To", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_27), _translate("MainWindow", "D / P Collection", None))
        self.groupBox_32.setTitle(_translate("MainWindow", "Print Monthly Collectible Report", None))
        self.pushButton_29.setText(_translate("MainWindow", "Print Report", None))
        self.groupBox_33.setTitle(_translate("MainWindow", "Monthly Collectible", None))
        self.label_92.setText(_translate("MainWindow", "From", None))
        self.pushButton_30.setText(_translate("MainWindow", "Display Accounts", None))
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_12.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Monthly Rent", None))
        item = self.tableWidget_12.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telephone", None))
        self.dateEdit_15.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.dateEdit_24.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_170.setText(_translate("MainWindow", "To", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_28), _translate("MainWindow", "Monthly Collectible", None))
        self.groupBox_36.setTitle(_translate("MainWindow", "Weekly Collectible", None))
        self.pushButton_35.setText(_translate("MainWindow", "Display Accounts", None))
        self.dateEdit_16.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        item = self.tableWidget_16.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_16.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_16.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_16.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Monthly Rent", None))
        item = self.tableWidget_16.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telephone", None))
        self.label_171.setText(_translate("MainWindow", "To", None))
        self.dateEdit_25.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_172.setText(_translate("MainWindow", "From", None))
        self.groupBox_37.setTitle(_translate("MainWindow", "Print Weekly Collectible Report", None))
        self.pushButton_36.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), _translate("MainWindow", "Weekly Collectible", None))
        self.groupBox_38.setTitle(_translate("MainWindow", "Daily Collectible", None))
        self.pushButton_37.setText(_translate("MainWindow", "Display Accounts", None))
        self.dateEdit_18.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        item = self.tableWidget_18.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_18.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_18.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loan Amount", None))
        item = self.tableWidget_18.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Monthly Rent", None))
        item = self.tableWidget_18.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telephone", None))
        self.label_173.setText(_translate("MainWindow", "From", None))
        self.dateEdit_26.setDisplayFormat(_translate("MainWindow", "d/M/yyyy", None))
        self.label_174.setText(_translate("MainWindow", "To", None))
        self.groupBox_39.setTitle(_translate("MainWindow", "Print Daily Collectible Report", None))
        self.pushButton_38.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MainWindow", "Daily Collectible", None))
        self.groupBox_34.setTitle(_translate("MainWindow", "Default Register", None))
        self.pushButton_33.setText(_translate("MainWindow", "Display Defaults", None))
        item = self.tableWidget_14.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan Number", None))
        item = self.tableWidget_14.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_14.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Monthly Rent", None))
        item = self.tableWidget_14.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Last Pay", None))
        item = self.tableWidget_14.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Arreas", None))
        item = self.tableWidget_14.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "D/C", None))
        item = self.tableWidget_14.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Telephone", None))
        self.groupBox_35.setTitle(_translate("MainWindow", "Print Default Register Report", None))
        self.pushButton_34.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_25), _translate("MainWindow", "Default Register", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ghjghj), _translate("MainWindow", "Monthly Report", "ghjg"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Backup", None))
        self.pushButton_41.setText(_translate("MainWindow", "Backup to Drive D:\\", None))
        self.pushButton_42.setText(_translate("MainWindow", "Backup to Custom path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Data Backup", None))
        self.groupBox_46.setTitle(_translate("MainWindow", "Cash Book Entry", None))
        self.label_148.setText(_translate("MainWindow", "Vote No <span style=\"color: red\">*</span>", None))
        self.label_151.setText(_translate("MainWindow", "Desc <span style=\"color: red\">*</span>", None))
        self.label_153.setText(_translate("MainWindow", "Amount <span style=\"color: red\">*</span>", None))
        self.pushButton_47.setText(_translate("MainWindow", "Enter to Cash Book", None))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Debit", None))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "Credit", None))
        self.pushButton_59.setText(_translate("MainWindow", "Clear All", None))
        self.groupBox_45.setTitle(_translate("MainWindow", "Votes", None))
        self.label_139.setText(_translate("MainWindow", "01 - Dealer Payment", None))
        self.label_140.setText(_translate("MainWindow", "02 - Loan", None))
        self.label_141.setText(_translate("MainWindow", "03 - Petty Cash", None))
        self.label_142.setText(_translate("MainWindow", "04 - Salary", None))
        self.label_143.setText(_translate("MainWindow", "05 - Utility Bill", None))
        self.label_144.setText(_translate("MainWindow", "06 - Fuel", None))
        self.label_145.setText(_translate("MainWindow", "07 - Vehicle Maintain", None))
        self.label_146.setText(_translate("MainWindow", "09 - Miscellaneous", None))
        self.label_147.setText(_translate("MainWindow", "08 - Leasing Rental", None))
        self.label_193.setText(_translate("MainWindow", "10 - Transfer Of funds", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_18), _translate("MainWindow", "Data Entry", None))
        self.groupBox_47.setTitle(_translate("MainWindow", "Cash Book", None))
        self.pushButton_48.setText(_translate("MainWindow", "Display CashBook", None))
        item = self.tableWidget_21.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_21.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description", None))
        item = self.tableWidget_21.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vote No.", None))
        item = self.tableWidget_21.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Debit", None))
        item = self.tableWidget_21.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_21.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        item = self.tableWidget_21.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CR/DR", None))
        self.groupBox_48.setTitle(_translate("MainWindow", "Print Cash Book", None))
        self.pushButton_49.setText(_translate("MainWindow", "Print Report", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_29), _translate("MainWindow", "Cash book Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Cash Book", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Current User", None))
        self.label_93.setText(_translate("MainWindow", "Name", None))
        self.label_97.setText(_translate("MainWindow", "Username", None))
        self.label_100.setText(_translate("MainWindow", "Telephone", None))
        self.label_101.setText(_translate("MainWindow", "Address", None))
        self.pushButton_5.setText(_translate("MainWindow", "Load Window", None))
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username", None))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Activity", None))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_13.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time", None))
        self.pushButton_8.setText(_translate("MainWindow", "Log Out", None))
        self.pushButton_32.setText(_translate("MainWindow", "Change Password", None))
        self.label_112.setText(_translate("MainWindow", "Old Password", None))
        self.label_113.setText(_translate("MainWindow", "New Password", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "View Another User", None))
        self.pushButton_6.setText(_translate("MainWindow", "View Details", None))
        self.label_98.setText(_translate("MainWindow", "Name", None))
        self.label_102.setText(_translate("MainWindow", "Address", None))
        self.label_103.setText(_translate("MainWindow", "Telephone", None))
        item = self.tableWidget_15.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Activity", None))
        item = self.tableWidget_15.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_15.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Add User", None))
        self.label_99.setText(_translate("MainWindow", "Username", None))
        self.label_104.setText(_translate("MainWindow", "Name", None))
        self.label_105.setText(_translate("MainWindow", "Address", None))
        self.label_106.setText(_translate("MainWindow", "Telephone", None))
        self.label_107.setText(_translate("MainWindow", "Password", None))
        self.pushButton_7.setText(_translate("MainWindow", "Add User", None))
        self.label_108.setText(_translate("MainWindow", "Privileges", None))
        self.checkBox.setText(_translate("MainWindow", "Grant All Privileges", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Delete User", None))
        self.label_110.setText(_translate("MainWindow", "Password", None))
        self.pushButton_31.setText(_translate("MainWindow", "Delete User", None))
        self.label_111.setText(_translate("MainWindow", "Select User", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Users", None))
        self.label_149.setText(_translate("MainWindow", "Developed by Vitaz | Contact 0715654548 - 0779078862", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Calculator", None))

