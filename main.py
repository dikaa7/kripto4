from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
import ui
import rsa, elgamal, pailer

class MainApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.chiper = 'Vigenere'
        self.rsa.toggled.connect(self.onClicked)
        self.rsa.value = 'rsa'
        self.rsa.setChecked(True)
        self.elgamal.toggled.connect(self.onClicked)
        self.elgamal.value = 'elgamal'
        self.pailer.toggled.connect(self.onClicked)
        self.pailer.value = 'pailer'

        self.encButton.clicked.connect(self.onEncrypt)
        self.decButton.clicked.connect(self.onDecrypt)

        self.message = self.encoded.toPlainText()
        self.file = ''
        self.path = ''

    def listToText(self,l):
        return ",".join([str(x) for x in l])

    def textToList(self,t):
        l = t.split(",")
        return [int(x) for x in l]

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.chosen = radioButton.value
            if(self.chosen == "elgamal"):
                self.g.setDisabled(False)
                self.q.setDisabled(True)
            else:
                self.g.setDisabled(True)
                self.q.setDisabled(False)
    
    def onEncrypt(self):
        p = int(self.p.toPlainText())
        plaintext = self.encoded.toPlainText()

        if self.chosen == "rsa":
            q = int(self.q.toPlainText())
            self.rsapub, self.rsapri = rsa.generate_keypair(p,q)
            ct = rsa.rsa_encrypt(self.rsapub, plaintext)
            self.result.setText(self.listToText(ct))
            self.info.setText("Public Key (e,n) : " + str(self.rsapub) + 
            "\nPrivate Key (d,n) : " + str(self.rsapri))
        
        elif self.chosen == "elgamal":
            g = int(self.g.toPlainText())
            self.elgamalpub, self.elgamalpri = elgamal.generate_keypair(p,g)
            ct, self.elgamalc1 = elgamal.elgamal_encrypt(self.elgamalpub, plaintext)
            self.result.setText(self.listToText(ct))
            self.info.setText("Public Key (p,g,A) : " + str(self.elgamalpub) + 
            "\nPrivate Key (a) : " + str(self.elgamalpri) + 
            "\nc1 : " + str(self.elgamalc1) )
        
        elif self.chosen == "pailer":
            q = int(self.q.toPlainText())
            self.pailerpub, self.pailerpri = pailer.generate_keypair(p,q)
            ct = pailer.pailer_encrypt(self.pailerpub, plaintext)
            self.result.setText(self.listToText(ct))
            self.info.setText("Public Key (g,n) : " + str(self.pailerpub) + 
            "\nPrivate Key (phi, u) : " + str(self.pailerpri))

    def onDecrypt(self):
        ciphertext = self.textToList(self.encoded.toPlainText())

        if self.chosen == "rsa":
            pt = rsa.rsa_decrypt(self.rsapri, ciphertext)
            self.result.setText(pt)
            self.info.setText("Public Key (e,n) : " + str(self.rsapub) + 
            "\nPrivate Key (d,n) : " + str(self.rsapri))

        elif self.chosen == "elgamal":
            pt = elgamal.elgamal_decrypt(self.elgamalc1, self.elgamalpri, self.elgamalpub[0], ciphertext)
            self.result.setText(pt)
            self.info.setText("Public Key (p,g,A) : " + str(self.elgamalpub) + 
            "\nPrivate Key (a) : " + str(self.elgamalpri) + 
            "\nc1 : " + str(self.elgamalc1))

        elif self.chosen == "pailer":
            pt = pailer.pailer_decrypt(self.pailerpri, self.pailerpub[1], ciphertext)
            self.result.setText(pt)
            self.info.setText("Public Key (g,n) : " + str(self.pailerpub) + 
            "\nPrivate Key (phi, u) : " + str(self.pailerpri))

def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()