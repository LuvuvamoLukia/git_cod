import sys
import mysql.connector
from datetime import date
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLayout, QLineEdit , QMainWindow



def func1():
    lbl.setText("conectando a nova fonte!")
    lbl.adjustSize()

def func2():
    lbl.setText("conectando a nova fonte 2!")
    lbl.adjustSize()

def func3():
    vlr_lido = le.text()
    lbl.setText(vlr_lido)
    lbl.adjustSize()



app = QApplication(sys.argv)



janela1 = QWidget()
janela1.resize(2100,800)
janela1.setWindowTitle("Lukia Transfer System")
janela1.setStyleSheet('background-color:DarkRed')
janela1.adjustSize()

btn0 = QPushButton("Acessar", janela1)
btn0.setGeometry(100,100,140,50)
btn0.setStyleSheet('background-color:GhostWhite;color:black;font-size:30px')
btn0.clicked.connect(func1)

btn01 = QPushButton("Cadastrar 2", janela1)
btn01.setGeometry(100,160,140,50)
btn01.setStyleSheet('background-color:GhostWhite;color:black')
btn01.clicked.connect(func2)


btn02 = QPushButton("Botão 3", janela1)
btn02.setGeometry(100,220,140,50)
btn02.setStyleSheet('background-color:GhostWhite;color:black')
btn02.clicked.connect(func3)



lbl = QLabel("digite o seu usuario e senha !", janela1)
lbl.move(300,120)
lbl.setStyleSheet('color:GhostWhite')

le = QLineEdit("", janela1)
le.setGeometry(300,220,140,50)


janela1.show()

app.exec()


