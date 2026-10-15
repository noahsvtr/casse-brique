#Objectifs: définir les différentes classes pour réaliser le jeu de casse brique pour le TP4 de développement python, CPE Lyon
#Crée le 08/10/2026
#Réalisé par SAVATIER Noah / TORTEROLO Alexis
#TO DO: classe raquette, colisions avec la brique
#Infos : taille de la fenêtre ( 700*700+400+200)

import tkinter as tk
import math 

#Classe 1: Brique classique. Concept: rectangle immobile, disparaissant lorsqu'elle entre en contact avec la balle une fois.  

class briqueclassique:
    def __init__(self, x, y, caneva, largeur=20, longueur = 30, points = 10, couleur = "green"):
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__longueur = longueur
        self.__points = points
        self.__couleur = couleur
        self.__caneva = caneva

    def rectangle(self): #crée le visuel de la brique
        self.rectangle = self.__caneva.create_rectangle(self.__x, self.__y, self.__x + self.__longueur, self.__y + self.__largeur, fill = self.__couleur, width = 0)
    
    def touche(self, balle): # vérifie si la balle touche la brique
        if balle.__x + balle.__rayon > self.__x and balle.__y + balle.__rayon > self.__y and balle.__y - balle.__rayon < self.__y + self.__largeur and balle.__x - balle.__rayon < self.__x + self.__longueur:
            return True
        else:
            return False

    def cotetouche(self, balle): # dit si la balle a touche un cote ou le dessus / dessous
        gauche = balle.x + balle.rayon - self.__x
        droite = self.__x + self.__longueur - (balle.x - balle.rayon)
        haut = balle.y + balle.rayon - self.__y
        bas = self.__y + self.__largeur - (balle.y - balle.rayon)
        if min (gauche, droite) < min (haut,  bas): # la côté touché est celui où la valeur gauche / droite / bas / haut est la plus petite
            return "cote"
        else:
            return "dessusdessous"
        

    def supp(self, balle, points): #supprime la brique si elle est touchée par la balle et augmente le score du joueur
        if self.touche(self,balle) == True:
            self.caneva.delete(self.rectangle)
            points = points + 10

        

#Classe 2: Balle. Concept: cercle qui rebondit sur les bords de la fenêtre, sauf celui du bas. Elle rebondit également sur les briques
#          et a un effet sur elles qui diffère selon le type de la brique.

class balle:
    def __init__(self, x, y, dx, dy, caneva, angle, vitesse, fenetre, briques, rayon=10, couleur = "red"):
            self.__x = x
            self.__y = y
            self.__rayon = rayon
            self.__couleur = couleur
            self.__caneva = caneva
            self.__vitesse = vitesse
            self.__angle = angle
            self.__fenetre = fenetre
            self.__dx = dx
            self.__dy = dy
            self.disque()
    def disque(self): #crée le visuel de la balle
        self.__id = self.__caneva.create_oval(self.__x - self.__rayon, self.__y - self.__rayon, self.__x + self.__rayon, self.__y + self.__rayon, width = 1, fill = self.__couleur)

    def deplacement(self): # permet à la balle de se déplacer selon les règles de déplacement définies
        largeur = int(self.__caneva.cget("width"))
        hauteur = int(self.__caneva.cget("height"))
        if self.__x + self.__rayon + self.__dx > largeur:
            self.__x = 2*(largeur - self.__rayon) - self.__x
            self.__dx = - self.__dx

        if self.__x - self.__rayon + self.__dx < 0 :
            self.__x = 2 * self.__rayon - self.__x
            self.__dx = -self.__dx
        
        
        if self.__y + self.__rayon + self.__dy > hauteur:
            self.__y = 2*(hauteur - self.__rayon) - self.__y
            self.__dy = -self.__dy

        if self.__y - self.__rayon + self.__dy < 0:
            self.__y = 2*self.__rayon - self.__y
            self.__dy = -self.__dy

        self.__x = self.__x + self.__dx
        self.__y = self.__y + self.__dy

        for brique in briques 
        
        
        
        
        self.__caneva.coords(self.__id, self.__x - self.__rayon, self.__y - self.__rayon, self.__x + self.__rayon, self.__y + self.__rayon )

        self.__fenetre.after(20, self.deplacement)


#Classe 3: Raquette. Concept: raquette qui fait rebondir la balle.
#Située en bas de la fenêtre.

class raquette:
    def __init__(self):
        