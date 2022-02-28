import sys
from tkinter.tix import Tree
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from RN import *
import random

class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view.ui", self)
        opcion = False
        self.botonIngresar.clicked.connect(self.option1)
        self.aleatorio.clicked.connect(self.option2)
    
    def generarWs(self):
        listWs = []
        for i in range(6):
            ws = round(random.uniform(-1, 1), 4)
            listWs.append(ws)
        return listWs
    
    def option1(self):
        opcion = False
        self.ingresarDatos(opcion)
    
    def option2(self):
        opcion = True
        self.ingresarDatos(opcion)


    def ingresarDatos(self, opcion):
        ws = ""
        if opcion == True:
            ws = self.generarWs()
            self.wsA.setText(str(ws))
        else:
            ws = self.ws.text()
            ws = ws.split(',')

        print("Ws = ", ws)
        n1 = self.n1.text()
        n2 = self.n2.text()
        n3 = self.n3.text()
        n4 = self.n4.text()
        n5 = self.n5.text()

        iteraciones(n1, n2, n3, n4, n5, ws)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())