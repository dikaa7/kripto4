# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crypto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 21, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 21, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 340, 111, 17))
        self.label_4.setObjectName("label_4")
        self.encButton = QtWidgets.QPushButton(self.centralwidget)
        self.encButton.setGeometry(QtCore.QRect(120, 440, 151, 41))
        self.encButton.setObjectName("encButton")
        self.decButton = QtWidgets.QPushButton(self.centralwidget)
        self.decButton.setGeometry(QtCore.QRect(330, 440, 151, 41))
        self.decButton.setObjectName("decButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 261, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 50, 101, 17))
        self.label_6.setObjectName("label_6")
        self.rsa = QtWidgets.QRadioButton(self.centralwidget)
        self.rsa.setGeometry(QtCore.QRect(490, 70, 97, 23))
        self.rsa.setObjectName("rsa")
        self.elgamal = QtWidgets.QRadioButton(self.centralwidget)
        self.elgamal.setGeometry(QtCore.QRect(490, 90, 97, 23))
        self.elgamal.setObjectName("elgamal")
        self.pailer = QtWidgets.QRadioButton(self.centralwidget)
        self.pailer.setGeometry(QtCore.QRect(490, 110, 97, 23))
        self.pailer.setObjectName("pailer")
        self.p = QtWidgets.QTextEdit(self.centralwidget)
        self.p.setGeometry(QtCore.QRect(60, 50, 401, 51))
        self.p.setObjectName("p")
        self.q = QtWidgets.QTextEdit(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(60, 110, 401, 51))
        self.q.setObjectName("q")
        self.encoded = QtWidgets.QTextEdit(self.centralwidget)
        self.encoded.setGeometry(QtCore.QRect(50, 270, 511, 61))
        self.encoded.setObjectName("encoded")
        self.result = QtWidgets.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(50, 370, 511, 61))
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.info = QtWidgets.QTextEdit(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(50, 500, 511, 111))
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.g = QtWidgets.QTextEdit(self.centralwidget)
        self.g.setEnabled(False)
        self.g.setGeometry(QtCore.QRect(60, 170, 401, 51))
        self.g.setObjectName("g")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 180, 21, 31))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crack Your Code"))
        self.label.setText(_translate("MainWindow", "P"))
        self.label_2.setText(_translate("MainWindow", "Q"))
        self.label_3.setText(_translate("MainWindow", "Encoded Text"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.encButton.setText(_translate("MainWindow", "Encrypt"))
        self.decButton.setText(_translate("MainWindow", "Decrypt"))
        self.label_5.setText(_translate("MainWindow", "RSA, Elgamal, Pailer Cryptosystem"))
        self.label_6.setText(_translate("MainWindow", "Choose Algoritm"))
        self.rsa.setText(_translate("MainWindow", "RSA"))
        self.elgamal.setText(_translate("MainWindow", "ElGamal"))
        self.pailer.setText(_translate("MainWindow", "Pailler"))
        self.p.setPlaceholderText(_translate("MainWindow", "Masukkan sebuah bilangan prima"))
        self.q.setPlaceholderText(_translate("MainWindow", "Masukkan sebuah bilangan prima"))
        self.encoded.setPlaceholderText(_translate("MainWindow", "Masukkan Text, Untuk dekripsi text dalam bentuk angka, contoh 34,23,12"))
        self.result.setPlaceholderText(_translate("MainWindow", "Hasiil Enkripsi / Dekripsi"))
        self.info.setPlaceholderText(_translate("MainWindow", "Program Info"))
        self.g.setPlaceholderText(_translate("MainWindow", "Masukkan sebuah G antara nilai 1 hingga P-1"))
        self.label_7.setText(_translate("MainWindow", "G"))
