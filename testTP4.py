#Objectifs: fichier de tests pour la réalisation du jeu de casse brique pour le TP4 de développement python, CPE Lyon
#Crée le 08/10/2026
#Réalisé par SAVATIER Noah / TORTEROLO Alexis
#TO DO:
import tkinter as Tk

#test de l'affichage 
Mafenetre = Tk.Tk()
Canevas = Tk.Canvas(Mafenetre, width= 1300 , height = 600, bg = 'black')
Canevas.pack(padx=5,pady=5)
Canevas.create_rectangle(20, 50, 80, 30, fill='green', width=0)
Canevas.create_oval(60 - 10, 30 - 10, 60 + 10, 30 + 10, width = 0, fill = 'red')
Mafenetre.mainloop()

