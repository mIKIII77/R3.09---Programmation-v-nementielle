import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Saisir votre nom")
        self.text = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        self.prenom = QLabel("")
        

        # Ajouter les widgets dans la grille
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.text, 2, 0)
        grid.addWidget(ok, 3, 0)
        grid.addWidget(self.prenom, 4, 0)
        grid.addWidget(quit, 5, 0)


        # Changement de la taille de la fenetre par defaut
        self.resize(600, 100)

        # Connexion des signaux
        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Une première fenêtre")
    

    def __actionOk(self): # Recuperer le texte saisi et rajouer bonjour devant le texte
        self.prenom.setText("Bonjour " + self.text.text())
        pass




    def __actionQuitter(self):
        QCoreApplication.exit(0)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()