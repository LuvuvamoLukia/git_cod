import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLayout, QLineEdit



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



janela = QWidget()
janela.resize(800,800)
janela.setWindowTitle("Lukia Transfer System")
janela.setStyleSheet('background-color:DarkRed')
janela.adjustSize()

btn = QPushButton("Acessar", janela)
btn.setGeometry(100,100,140,50)
btn.setStyleSheet('background-color:GhostWhite;color:black')
btn.clicked.connect(func1)

btn1 = QPushButton("Cadastrar 2", janela)
btn1.setGeometry(100,160,140,50)
btn1.setStyleSheet('background-color:GhostWhite;color:black')
btn1.clicked.connect(func2)


btn2 = QPushButton("Botão 3", janela)
btn2.setGeometry(100,220,140,50)
btn2.setStyleSheet('background-color:GhostWhite;color:black')
btn2.clicked.connect(func3)


lbl = QLabel("digite o seu usuario e senha !", janela)
lbl.move(300,120)

le = QLineEdit("", janela)
le.setGeometry(300,220,140,50)


janela.show()

app.exec()


