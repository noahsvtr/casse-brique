
import tkinter as Tk

mw=Tk.Tk() #crée une fenêtre principale
mw.title("Casse brique") # met un titre à la fenêtre
mw["bg"]='black' #fenetre de couleur noir
mw.geometry('700x700') #geométrie de la fenêtre (largeur x hauteur )
num = 0
score = 0
def Nouveaulance_prime():
    print ("Lancement du jeu") #affiche un message dans la console pour indiquer que le jeu est lancé
    mw.destroy() #ferme la fenêtre principale
    nw=Tk.Tk() #crée une nouvelle fenêtre principale

    nw.title("Casse brique") # met un titre à la fenêtre
    nw["bg"]='black' #fenetre de couleur noir
    nw.geometry('700x700')
    Label= Tk.Label(nw, text= "jeu lancé", fg='black', bg='white') #crée un label pour indiquer que le jeu est lancé
    frame1 = Tk.Frame(nw, bg='black') #crée un cadre pour contenir les boutons
    frame1.pack(side='top', fill='x') #place le cadre en haut de la fenêtre et le fait remplir horizontalement
    

    frame2 = Tk.Frame(nw, bg='black') #crée un cadre pour contenir les boutons
    frame2.pack(side='top', fill='x') #place le cadre en haut de la fenêtre et le fait remplir horizontalement


    Tk.Label(frame1, text= "Vies:" +str(num), fg="yellow", bg='black').pack(side='left', padx= 5, pady= 5) #crée un label pour afficher le nombre de vies restantes
    Tk.Label(frame2, text= "Score:" +str(score), fg="yellow", bg='black').pack(side='right', padx= 5, pady= 5) #crée un label pour afficher le nombre de vies restantes
    
    BouttonQuitt1= Tk.Button(nw,fg='red',text='Quitter',command=nw.destroy) #boutton pour quitter le jeu
    BouttonQuitt1.pack(side = 'bottom') 



    BouttonRecommencer= Tk.Button(nw,fg='black',text='Recommencer',command=Nouveaulance) #boutton pour recommencer le jeu
    BouttonRecommencer.pack(side = 'bottom') 





    Canevas = Tk.Canvas(nw, width= 700 , height = 550, bg = 'black')
    Canevas.pack(padx=5,pady=5)





    nw.mainloop()











BouttonQuitt= Tk.Button(mw,fg='red',text='Quitter',command=mw.destroy,) #boutton pour quitter le jeu
BouttonQuitt.pack() 
BouttonLancer=Tk.Button(mw,fg='black',text='Lancer le jeu',command=Nouveaulance) #boutton pour lancer le jeu
BouttonLancer.pack(side='top',padx= 5,pady= 5) #bou







mw.mainloop() #maintient la fenêtre ouverte jusqu'à ce que l'utilisateur la ferme
