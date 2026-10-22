#Objectifs: réaliser un jeu de casse brique pour le TP4 de développement python, CPE Lyon
#Crée le 08/10/2026
#Réalisé par SAVATIER Noah / TORTEROLO Alexis
#TO DO:
import tkinter as Tk
import pythonTP4fonction as fct



mw=Tk.Tk()
mw.title("Casse brique")
mw["bg"]='black'
mw.geometry('700x700+400+200')



Bouttonquiter= Tk.Button (mw,fg='red',text='Quitter',command=mw.destroy) #boutton pour quitter le jeu
Bouttonlancer=Tk.Button(mw,fg='black',text='Lancer le jeu',command= lambda: fct.Nouveaulance(mw)) #boutton pour lancer le jeu

Bouttonlancer.pack(side="top", padx=50, pady=5)
Bouttonquiter.pack()

mw.mainloop()

