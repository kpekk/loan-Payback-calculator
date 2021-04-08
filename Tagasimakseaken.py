import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
from tagasimaksegraafik import tagasimaksegraafik
from themes import dark

class Tagasimakse(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()
        fail = open("graafik.txt", "r", encoding = "utf-8")
        self.setWindowIcon(QtGui.QIcon("pics/logo.jpg")) #akna ikoon
        self.setWindowTitle("Laenu tagasimaksegraafik")

        self.setGeometry(7000, 60, 655, 600)#1- no idea, 2-no idea, 3- laius(vasak-parem), 4- pikkus(üles-alla)
        self.move(900, 150) #kus programm paikneb, (vasak-parem, üles-alla)
        
        self.show()
        self.setLayout(grid)  
        self.setPalette(dark)
        
        loendur = 0 #realoendur
        for rida in fail:
            loendur += 1
        fail.seek(0)

        tabel = QTableWidget()
        tabel.setRowCount(loendur - 1)
        tabel.setColumnCount(4)
        tabel.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #et kaste muuta ei saaks
        j = 0
        i = 0
        for line in fail:
            if line.split()[0] == "Intress": #lisa viimane rida labelina
                viimanerida = QLabel(line)
            j = 0
            nmk = list(line.split(" "))
            for elem in nmk:
                tabel.setItem(i,j, QTableWidgetItem(elem))
                j += 1
            i += 1

        #tabeli ja koguintressi lisamine
        grid.addWidget(tabel)
        tabel.move(0, 0)
        grid.addWidget(viimanerida)
        #sulgemisnupp
        sulgenupp = QPushButton("Sulge")
        grid.addWidget(sulgenupp)
        sulgenupp.clicked.connect(QtCore.QCoreApplication.instance().quit)