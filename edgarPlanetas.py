import threading
from PyQt5 import QtWidgets, QtCore, QtTest

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys, time
from PyQt5 import uic
from multiprocessing.pool import ThreadPool
import threading



class index(QMainWindow, threading.Thread):

    

    def __init__(self, nombre, tiempo):
        super().__init__()
        uic.loadUi("vista.ui", self)
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tiempo = tiempo 
        
        
        
        self.botonIniciar.clicked.connect(lambda:met(self))
        
    def movimiento(self):

        global ban1,ban2,ban3,ban4,ban5,ban6,ban7,ban8
        ban1= True
        ban2= True
        ban3= True
        ban4= True
        ban5= True
        ban6= True
        ban7= True
        ban8= True
        
        dias = 51
        contadorTiempo = 0
        while dias != contadorTiempo:
            
            time.sleep(self.tiempo)       
            #print('Planeta: ',self.nombre,'dias:',contadorTiempo)
            contadorTiempo += 1

        print("termino: ", self.nombre)
        
        
            
    def run(self):
        
        self.movimiento()
        self.label_neptuno.setText(str('termine'))


def met(self):
    print("entre")

    planeta = index("mercurio", 0.1)
    planeta2 = index('venus',0.22)
    planeta3 = index('tierra',0.3)
    planeta4 = index('marte',0.33)
    planeta5 = index('jupiter',0.37)
    planeta6 = index('saturno',0.01)
    planeta7 = index('urano',0.02)
    planeta8 = index('neptuno',0.01)
    planeta.start()
    planeta2.start()
    planeta3.start()
    planeta4.start()
    planeta5.start()
    planeta6.start()
    planeta7.start()
    planeta8.start()

    self.label_mercurio.setText(str('moving'))
    self.label_neptuno.setText(str('moving'))
    self.label_urano.setText(str('moving'))
    self.label_saturno.setText(str('moving'))
    self.label_jupiter.setText(str('moving'))
    self.label_marte.setText(str('moving'))
    self.label_tierra.setText(str('moving'))
    self.label_venus.setText(str('moving'))

def vista():
    app = QApplication(sys.argv)
    GUI = index("mercurio", 0.1)
    GUI.show()
    
    sys.exit(app.exec_())  

if __name__ == '__main__':

    vista()

     