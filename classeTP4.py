#Objectifs: définir les différentes classes pour réaliser le jeu de casse brique pour le TP4 de développement python, CPE Lyon
#Crée le 08/10/2026
#Réalisé par SAVATIER Noah / TORTEROLO Alexis
#TO DO: classe brique, classe raquette, classse balle

#Classe 1: Brique classique. Concept: rectangle immobile, disparaissant lorsqu'elle entre en contact avec la balle une fois.
import tkinter as tk    

class briqueclassique:
    def __init__(self, x, y, canva, largeur=20, longueur = 30, points = 10, couleur = "green"):
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__longueur = longueur
        self.__points = points
        self.__couleur = couleur
        self.__canva = canva

    def rectangle(self): #crée le visuel de la brique
        self.rectangle = self.__canva.create_rectangle(self.__x, self.__y, self.__x + self.__longueur, self.__y + self.__largeur, fill=self.__couleur, width=0)
    
    def touche(self, balle): # vérifie si la balle touche la brique
        if balle.__x + balle.__rayon > self.__x and balle.__y + balle.__rayon > self.__y and balle.__y - balle.__rayon < self.__y + self.__largeur and balle.__x - balle.__rayon < self.__x + self.__longueur:
            return True
        else:
            return False

    def supp(self, balle): #supprime la brique si elle est touchée par la balle
        if self.touche(self,balle) == True:
            self.canva.delete(self.rectangle)
        

#Classe 2: Balle. Concept: cercle qui rebondit sur les bords de la fenêtre, sauf celui du bas. Elle rebondit également sur les briques
#          et a un effet sur elles qui diffère selon le type de la brique.

class balle:
    