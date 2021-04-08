import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtGui, QtCore, QtWidgets
from tagasimaksegraafik import tagasimaksegraafik
from Tagasimakseaken import Tagasimakse
from themes import *
class Algaken(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640,440)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.setWindowIcon(QtGui.QIcon('pics/logo.jpg'))
        self.setWindowTitle("Laenukalkulaator")
        self.setStyleSheet(styledef)
        
        self.algsummaLabel = QLabel("Laenatud summa")
        self.algsummatekst = QLineEdit(self)
        self.intressLabel = QLabel("Aastane intress")
        self.intresstekst = QLineEdit(self)
        self.perioodLabel = QLabel("Laenuperiood")
        self.perioodtekst = QLineEdit(self)
        self.genereerinupp = QPushButton("genereeri tagasimaksegraafik")
        self.metsnupp = QPushButton("style:mets")
        self.dunenupp = QPushButton("style:dune")
        self.darknupp = QPushButton("style:dark")
        self.lightnupp = QPushButton("style:light")

        lay = QGridLayout(self.centralwidget)
        #algsumma
        lay.addWidget(self.algsummaLabel,0,0) 
        self.algsummaLabel.setStyleSheet(darkstyle)
        lay.addWidget(self.algsummatekst,0,1,1,3)
        self.algsummatekst.setStyleSheet(darkstyle)
        #intress
        lay.addWidget(self.intressLabel,1,0)
        self.intressLabel.setStyleSheet(darkstyle)
        lay.addWidget(self.intresstekst,1,1,1,3)
        self.intresstekst.setStyleSheet(darkstyle)
        #periood
        lay.addWidget(self.perioodLabel,2,0)
        self.perioodLabel.setStyleSheet(darkstyle)
        lay.addWidget(self.perioodtekst,2,1,1,3)
        self.perioodtekst.setStyleSheet(darkstyle)
        #genereit, lisa tühje labeleid vahele et ruumi tekitada?- doesnt really wörk
        lay.addWidget(self.genereerinupp,3,1,1,2)
        self.genereerinupp.setStyleSheet(darkstyle)
        self.genereerinupp.clicked.connect(self.genereeri)

        lay.addWidget(self.metsnupp,4,0)
        self.metsnupp.setStyleSheet(darkstyle)
        self.metsnupp.clicked.connect(self.mets)

        lay.addWidget(self.dunenupp,4,3)
        self.dunenupp.setStyleSheet(darkstyle)
        self.dunenupp.clicked.connect(self.dune)

        lay.addWidget(self.darknupp,4,2)
        self.darknupp.setStyleSheet(darkstyle)
        self.darknupp.clicked.connect(self.darkmode)

        lay.addWidget(self.lightnupp,4,1)
        self.lightnupp.setStyleSheet(darkstyle)
        self.lightnupp.clicked.connect(self.lightmode)

    def mets(self):
        self.setStyleSheet(stylemets)
    def dune(self):
        self.setStyleSheet(styledune)
    def darkmode(self):
        self.setStyleSheet(styledef)
    def lightmode(self):
        self.setStyleSheet(stylelight)
       
    def genereeri(self):
        algsumma = self.algsummatekst.text()
        intress = self.intresstekst.text()
        periood = self.perioodtekst.text()
        tagasimaksegraafik(algsumma, intress, periood)
        self.hide()
        next = Tagasimakse()
        next.__init__()