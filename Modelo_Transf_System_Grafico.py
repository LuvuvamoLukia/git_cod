import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLayout, QLineEdit



def func1():
    lbl.setText("conectando a nova fonte!")
    lbl.adjustSize()

def func2():
    lbl.setText("conectando a nova fonte 2!")
    lbl.adjustSize()



app = QApplication(sys.argv)



janela = QWidget()
janela.resize(800,800)
janela.setWindowTitle("Lukia Transfer System")
janela.adjustSize()

btn = QPushButton("Botão 1", janela)
btn.setGeometry(100,100,140,50)
btn.setStyleSheet('background-color:Grey;color:black')
btn.clicked.connect(func1)

btn1 = QPushButton("Botão 2", janela)
btn1.setGeometry(100,160,140,50)
btn1.setStyleSheet('background-color:Grey;color:black')
btn1.clicked.connect(func2)


lbl = QLabel("digite o seu usuario", janela)
lbl.move(300,120)

janela.show()

app.exec()


