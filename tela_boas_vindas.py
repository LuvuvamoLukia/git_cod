import sys
import mysql.connector
from datetime import date
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLayout, QLineEdit , QMainWindow


app = QApplication(sys.argv)

janela = QWidget()
janela.resize(1800,900)
janela.setWindowTitle("Lukia Transfer System")
janela.setStyleSheet('background-color:DarkRed')
janela.adjustSize()

    #chama a função da boas vindas
def func1():
    lbl.setText("conectando a nova fonte!")
    lbl.adjustSize()


    # chama a função de direitos reservados 
def func1():
    lbl1.setText("conectando a nova fonte!")
    lbl1.adjustSize()


    #label da boas vindas
lbl = QLabel("Bem-vindo ao Sistema Transferência", janela)
lbl.move(200,100)
lbl.setStyleSheet('color:GhostWhite;font-size:50px')


    #label de direitos reservados
lbl1 = QLabel("todos direitos reservados@Lukia Comercio e Servicos", janela)
lbl1.move(360,600)
lbl1.setStyleSheet('color:GhostWhite;font-size:20px')


le = QLineEdit("", janela)
le.setGeometry(300,220,140,50)
le.get()

usuario = 'blaise_joao@gmail.com'
senha = 'BlaiseJS@'

#while True:
#	seu_usuario = input('Digite seu usuário: ')
#	sua_senha = input('Digite sua senha: ')
#	if usuario == seu_usuario and senha == sua_senha:
##		print('Seja Bem-Vindo!' usuario)
#		break
#	else:
#		print('usuario ou senha incorretos! \nTente novamente!')
#		break

def func0():
    lbl0.setText("conectando ao Sistema Transferência...!")
    lbl0.adjustSize()


lbl0 = QLabel("Digite o seu usuário e senha!", janela)
lbl0.move(480,360)
lbl0.setStyleSheet('color:GhostWhite;font-size:20px')

btn0 = QPushButton("Acessar", janela)
btn0.setGeometry(540,400,140,50)
btn0.setStyleSheet('background-color:GhostWhite;color:black;font-size:30px')
btn0.clicked.connect(func0)

janela.show()

app.exec()


