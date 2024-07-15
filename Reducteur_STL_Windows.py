# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:37:47 2024

@author: cleme
"""

import sys
import trimesh as tm
import os
from PyQt5.QtWidgets import QApplication,QToolBar,QAction, QMainWindow, QLineEdit, QLabel, QMessageBox, QWidget, QStatusBar, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Réducteur du nombre de face d'un STL")
        self.resize(700,500)
        self.setStyleSheet("background-color: lightgrey;")
        self.setWindowIcon(QIcon("Triangle.png"))
        
        self.conteneur = QWidget()
        self.box = QVBoxLayout(self.conteneur)
        
        self.Pourcentage = None
        self.Fichier = ''
            
        self.bouton_charger = QPushButton("Ouvrir fichier STL")
        self.bouton_charger.clicked.connect(self.charger)
        self.bouton_charger.setMinimumHeight(50)
        self.bouton_charger.setStyleSheet("background-color: orange;")
        self.box.addWidget(self.bouton_charger)
        
        self.info_fichier = QLabel()
        self.info_fichier.setText(f'Vous avez selectioné : {self.Fichier}')
        self.box.addWidget(self.info_fichier)
        
        self.pourcentage_layout = QHBoxLayout()
        
        self.lineEdit = QLineEdit()
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setPlaceholderText("Personnaliser le %")
        self.lineEdit.setStyleSheet("background-color: orange;")
        
        self.lineEdit.textChanged.connect(self.text_changed)
        self.lineEdit.setFixedWidth(150)
        self.lineEdit.setFixedHeight(40)
        
        self.pourcentage_layout.addWidget(self.lineEdit)
        
        self.bouton10 = QPushButton("90 %")
        self.bouton10.clicked.connect(self.value10)
        self.bouton10.setStyleSheet("background-color: white;")
        self.pourcentage_layout.addWidget(self.bouton10)
        
        self.bouton30 = QPushButton("70 %")
        self.bouton30.clicked.connect(self.value30)
        self.bouton30.setStyleSheet("background-color: white;")
        self.pourcentage_layout.addWidget(self.bouton30)
        
        self.bouton50 = QPushButton("50 %")
        self.bouton50.clicked.connect(self.value50)
        self.bouton50.setStyleSheet("background-color: white;")
        self.pourcentage_layout.addWidget(self.bouton50)
        
        self.bouton70 = QPushButton("30 %")
        self.bouton70.clicked.connect(self.value70)
        self.bouton70.setStyleSheet("background-color: white;")
        self.pourcentage_layout.addWidget(self.bouton70)
        
        self.box.addLayout(self.pourcentage_layout)
        
        self.info_pourcentage = QLabel()
        self.set_pourcentage()
        self.box.addWidget(self.info_pourcentage)
        
        self.bouton_valider = QPushButton("Demarrer la réduction")
        self.bouton_valider.clicked.connect(self.validation)
        self.bouton_valider.setMinimumHeight(50)
        self.bouton_valider.setStyleSheet("background-color: orange;")
        
        self.box.addWidget(self.bouton_valider)
        
        self.setCentralWidget(self.conteneur)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def update_status_bar(self):
        self.pourcentage_str = f"{100-self.Pourcentage}%" if self.Pourcentage is not None else "N/A"
        self.fichier_str = os.path.basename(self.Fichier) if self.Fichier else "Aucun fichier"
        self.status_bar.showMessage(f"Votre % : {self.pourcentage_str} | Votre Fichier selectioné: {self.fichier_str}")
        
    def update_ecran(self):
        self.pourcentage_str = f"{100-self.Pourcentage}%" if self.Pourcentage is not None else "N/A"
        self.fichier_str = os.path.basename(self.Fichier) if self.Fichier else "Aucun fichier"
        self.info_fichier.setText(f'Vous avez selectioné : {self.fichier_str}\n\n\n\n\nChoisissez le % de réduction de votre STL :')
        
    def set_pourcentage(self):
        if self.Fichier != '' and self.Pourcentage is not None:
            self.info_pourcentage.setText(f'Votre fichier fait {os.path.getsize(self.Fichier)/1000000} alors le fichier final fera {(os.path.getsize(self.Fichier)*self.Pourcentage)/100000000} Mo')
            
        elif self.Fichier == '' and self.Pourcentage is None:
            self.info_pourcentage.setText('Exemple : si votre fichier fait 100Mo alors le fichier final fera __ Mo')
            
        elif self.Fichier == '':
            self.info_pourcentage.setText(f'Exemple : si votre fichier fait 100Mo alors le fichier final fera {self.Pourcentage} Mo')
            
        elif self.Pourcentage is None:
            self.info_pourcentage.setText(f'Votre fichier fait {os.path.getsize(self.Fichier)/1000000} Mo alors le fichier final fera __ Mo')
        
    def charger(self):
        fichier, _ = QFileDialog.getOpenFileName(self, "Ouvrir fichier STL", "", "STL (*.STL);;All Files (*)")
        if fichier:
            self.Fichier = fichier
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def creator(self):
        easter=QMessageBox()
        easter.setText('Concepteur : Clément Gaschet')
        easter.exec()
        
    def value10(self):
        self.Pourcentage = 10
        self.bouton10.setStyleSheet("background-color: lightgreen;")
        self.bouton30.setStyleSheet("background-color: white;")
        self.bouton50.setStyleSheet("background-color: white;")
        self.bouton70.setStyleSheet("background-color: white;")
        self.lineEdit.setStyleSheet("background-color: orange;")
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def value30(self):
        self.Pourcentage = 30
        self.bouton10.setStyleSheet("background-color: white;")
        self.bouton30.setStyleSheet("background-color: lightgreen;")
        self.bouton50.setStyleSheet("background-color: white;")
        self.bouton70.setStyleSheet("background-color: white;")
        self.lineEdit.setStyleSheet("background-color: orange;")
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def value50(self):
        self.Pourcentage = 50
        self.bouton10.setStyleSheet("background-color: white;")
        self.bouton30.setStyleSheet("background-color: white;")
        self.bouton50.setStyleSheet("background-color: lightgreen;")
        self.bouton70.setStyleSheet("background-color: white;")
        self.lineEdit.setStyleSheet("background-color: orange;")
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def value70(self):
        self.Pourcentage = 70
        self.bouton10.setStyleSheet("background-color: white;")
        self.bouton30.setStyleSheet("background-color: white;")
        self.bouton50.setStyleSheet("background-color: white;")
        self.bouton70.setStyleSheet("background-color: lightgreen;")
        self.lineEdit.setStyleSheet("background-color: orange;")
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def text_changed(self, s):
        if self.verifier_nombre_str(s):
            self.Pourcentage = 100-int(s)
            self.bouton10.setStyleSheet("background-color: white;")
            self.bouton30.setStyleSheet("background-color: white;")
            self.bouton50.setStyleSheet("background-color: white;")
            self.lineEdit.setStyleSheet("background-color: lightgreen;")
            self.bouton70.setStyleSheet("background-color: white;")
        else:
            self.Pourcentage = None
            self.lineEdit.setText('')
            self.bouton10.setStyleSheet("background-color: white;")
            self.bouton30.setStyleSheet("background-color: white;")
            self.bouton50.setStyleSheet("background-color: white;")
            self.lineEdit.setStyleSheet("background-color: #FF6B4B;")
            self.bouton70.setStyleSheet("background-color: white;")
        self.update_status_bar()
        self.update_ecran()
        self.set_pourcentage()
        
    def validation(self):
        if self.Fichier != '' and self.Pourcentage is not None:
            alerte = QMessageBox()
            alerte.setWindowIcon(QIcon('Triangle.png'))
            alerte.setWindowTitle('Terminer')
            ouvrir_bouton = QPushButton('Ouvrir')
            ouvrir_bouton.clicked.connect(lambda: self.open_file(self.Fichier))
            alerte.addButton(ouvrir_bouton, QMessageBox.AcceptRole)
            alerte.addButton(QMessageBox.Ok)
            chargement = QMessageBox()
            chargement.setWindowIcon(QIcon('Triangle.png'))
            chargement.setWindowTitle('Chargement')
            chargement.setText('Veuillez patienter\nFichier en cours de réduction . . .')
            chargement.show()
            chargement.setStandardButtons(QMessageBox.NoButton)
            app.processEvents()
            path = self.reduction_faces(self.Fichier, self.Pourcentage)
            chargement.close()
            alerte.setText(f"Réduction Terminée\nPourcentage de réduction retenu : {100-self.Pourcentage}\nFichier retenu : {self.Fichier}\nChemin d'arrivé :{path}")
            alerte.exec()
            
        elif self.Fichier == '' and self.Pourcentage is None:
            alerte = QMessageBox()
            alerte.setText("Pourcentage non sélectionné\nFichier non chargé")
            alerte.exec()
            
        elif self.Fichier == '':
            alerte = QMessageBox()
            alerte.setText("Fichier non chargé")
            alerte.exec()
            
        elif self.Pourcentage is None:
            alerte = QMessageBox()
            alerte.setText("Pourcentage non sélectionné")
            alerte.exec()
            
    def open_file(self, chemin):
        os.startfile(os.path.dirname(chemin))
        
    def verifier_nombre_str(self, variable):
        try:
            nombre = int(variable)
            if 1 <= nombre <= 100:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def reduction_faces(self, chemin, ratio):
        input = tm.load(chemin)
        n = int(len(input.faces)*(ratio/100))
        output = input.simplify_quadratic_decimation(face_count=n)
        
        name, extension = os.path.splitext(self.fichier_str)
        chemin_arriver = os.path.dirname(chemin) + f'/{name}_Dago_Lite_{100-self.Pourcentage}{extension}'
        
        _ = output.export(chemin_arriver)
        return chemin_arriver
    
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
    
window = Fenetre()
window.show()

app.exec_()
