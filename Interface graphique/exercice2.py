import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Application de conversion de temperature
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Saisir la temperature :")
        lab2 = QLabel("Conversion")
        self.temp = QLineEdit("")
        self.unit = QLabel("Celcius")
        self.unit2 = QLabel("Kalvin")
        conv = QPushButton("Convertir")
        aide = QPushButton("Aide")
        resultat = QLineEdit("")
        self.choise = QComboBox()
        self.choise.addItem("Celcius vers Kalvin")
        self.choise.addItem("Kalvin vers Celcius")


        
        
        self.resultat = resultat
        self.aide = aide
        self.conv = conv
        self.lab = lab

        # Ajouter les widgets dans la grille
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.temp, 0, 1)
        grid.addWidget(self.unit, 0, 2)

        grid.addWidget(conv, 1, 1)
        grid.addWidget(self.choise, 1, 2)
        grid.addWidget(lab2, 2, 0)
        grid.addWidget(resultat, 2, 1)
        grid.addWidget(self.unit2, 2, 2)

        grid.addWidget(aide, 3, 3)


        self.resize(600, 400)

        aide.clicked.connect(self.__actionAide)
        self.choise.currentIndexChanged.connect(self.__actionchoise)
        self.choise.currentIndexChanged.connect(self.__actionSup)
        conv.clicked.connect(self.__actionConv)




        self.setWindowTitle("Conversion de temperature")


    def __actionAide(self): # afficher une fenetre d'aide
        QMessageBox.information(self, "Aide", "Cette application permet de convertir une temperature en Celcius en Fahrenheit ou Kelvin")
        pass
       



    def __actionchoise(self): # Choisir la conversion de temperature a faire Celcius vers Kalvin ou le contraire
        if self.choise.currentIndex() == 0:
            self.unit.setText("Celcius")
            self.unit2.setText("Kalvin")
        else:
            self.unit.setText("Kalvin")
            self.unit2.setText("Celcius")
        pass
        
    
    def __actionSup(self): # Supprimer le contenu de la zone de texte resultat
        self.resultat.setText("")
        self.temp.setText("")
        pass
        
        

    def __actionConv(self): # Convertir la temperature
        msg = QMessageBox()
        msg.setWindowTitle("Erreur")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("La temperature doit etre un nombre")
        try:
            x = float(self.temp.text())
        except ValueError:
            msg.exec()
        else:
            if self.choise.currentIndex() != 0:
                # Formatrer le resultat a 2 chiffres apres la virgule
                # Ne pas autoriser la saisie de nombre negatif pour la temperature en Kalvin
                if x < 0:
                    msg.setText("La temperature en Kalvin est incorrecte")
                    msg.exec()
                self.resultat.setText("{:.2f}".format(float(self.temp.text()) + 273.15))
            elif self.choise.currentIndex() == 0:
                if x < -273.15:
                    msg.setText("La temperature en Celcius est incorrecte")
                    msg.exec()
                self.resultat.setText("{:.2f}".format(float(self.temp.text()) - 273.15))
            pass





        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    app.exec()








