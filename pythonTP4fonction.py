#Objectifs: réaliser un jeu de casse brique pour le TP4 de développement python, CPE Lyon
#Crée le 08/10/2026
#Réalisé par SAVATIER Noah / TORTEROLO Alexis
#TO DO:
import tkinter as Tk

num = 0
score = 0








def Nouveaulance(mw):
    print("Lancement du jeu")
    nw = Tk.Toplevel(mw)
    mw.withdraw()
    CreerFenetreJeu(nw)
    CreerInformations(nw)
    CreerBoutons(nw)
    CreerCanevas(nw)


def CreerFenetreJeu(nw):
    nw.title("Casse brique")
    nw["bg"]='black'
    nw.geometry('700x700')

def CreerInformations(nw):
    Label= Tk.Label(nw, text= "jeu lancé", fg='black', bg='white') #crée un label pour indiquer que le jeu est lancé
    Label.pack()
    
    frame1 = Tk.Frame(nw, bg='black') #crée un cadre pour contenir les boutons
    frame1.pack(side='top', fill='x') #place le cadre en haut de la fenêtre et le fait remplir horizontalement
    

    frame2 = Tk.Frame(nw, bg='black') #crée un cadre pour contenir les boutons
    frame2.pack(side='top', fill='x') #place le cadre en haut de la fenêtre et le fait remplir horizontalement


    Tk.Label(frame1, text= "Vies:" +str(num), fg="yellow", bg='black').pack(side='left', padx= 5, pady= 5) #crée un label pour afficher le nombre de vies restantes
    Tk.Label(frame2, text= "Score:" +str(score), fg="yellow", bg='black').pack(side='right', padx= 5, pady= 5) #crée un label pour afficher le nombre de vies restantes
    



def CreerBoutons(nw):
    BouttonQuitt1= Tk.Button(nw,fg='red',text='Quitter',command=nw.destroy) #boutton pour quitter le jeu
    BouttonQuitt1.pack(side = 'bottom') 



    BouttonRecommencer= Tk.Button(nw,fg='black',text='Recommencer',command= lambda: Nouveaulance) #boutton pour recommencer le jeu
    BouttonRecommencer.pack(side = 'bottom') 



def CreerCanevas(nw):
    Canevas = Tk.Canvas(nw, width= 700 , height = 550, bg = 'black')
    Canevas.pack(padx=5,pady=5)
