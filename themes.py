from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QPixmap
from PyQt5 import QtGui, QtCore, QtWidgets
QApplication.setStyle("Fusion") #ülejäänud themed koledad
dark = QPalette()
dark.setColor(QPalette.Window, QColor(53, 53, 53)) #taustavärv
dark.setColor(QPalette.WindowText, Qt.red) #labelite teksti värv
dark.setColor(QPalette.Base, QColor(25, 25, 25)) 
dark.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark.setColor(QPalette.ToolTipBase, Qt.white)
dark.setColor(QPalette.ToolTipText, Qt.white)
dark.setColor(QPalette.Text, Qt.white) #tekstikasti teksti värv
dark.setColor(QPalette.Button, QColor(53, 53, 53)) #nupu värv
dark.setColor(QPalette.ButtonText, QColor(255,1,248)) #nupu tekstivärv

darkstyle = """
QPushButton{
    background-color:rgb(53,53,53); color:red; border-style: outset; border-width: 4px; border-color: rgb(53,53,53) 
}
QPushButton:pressed{
    background-color:gray;   
}
QLabel{
    background-color:rgb(53,53,53); color:red;
    border-width: 4px; border-color: rgb(53,53,53);
}
QLineEdit{
    background-color:rgb(53,53,53); color:red;
    border-style: outset; border-width: 4px; border-color: rgb(53,53,53);
}
"""
stylemets = """
Algaken {
    background-image: url("pics/mets.jpg");
    background-position: center;
}
"""
stylelight = """
Algaken {
    background-color: rgb(186,224,246);
}
"""
styledune = """
Algaken {
    background-image: url("pics/dunes.jpg");
    background-position: center;
}
"""
styledef = """
Algaken {
    background-color: rgb(57,57,57);
}
"""