from tkinter import *

# Fenetre

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1920x1080")

# Zone de jeu
tank=PhotoImage(file="espace.gif")

ZoneJeu=Canvas(Fenetre,bg="black")
ZoneJeu.pack(fill=BOTH,expand=1)
ZoneJeu.create_image(0,800, image=tank)
ZoneJeu.pack()


# Gestion des ennemis:

# Fonction de tir

def Tir():
    Coordonnes=ZoneJeu.coords("Joueur")
    ZoneJeu.create_line(Coordonees[0], Coordonees[1]+20, Coordonees[2], Coordonees[3], fill="red", width=5, tag="Laser")
    MouvementTir("Laser")

def MouvementTir(Projectile):
    ZoneJeu.after(100,MouvementTir,"Laser")
    ZoneJeu.move(Projectile,0, -5)


# Fonction de mouvement

def Mouvement(Action):
    Coordonees=ZoneJeu.coords("Joueur")
    if Action.keysym=="Left" and Coordonees[0]>20:
        ZoneJeu.move("Joueur", -20,0)
    elif Action.keysym=="Right" and Coordonees[2]<780:
        ZoneJeu.move("Joueur", 20, 0)
    elif Action.keysym=="Up" and Coordonees[1]>650:
        ZoneJeu.move("Joueur", 0, -20)
    elif Action.keysym=="Down" and Coordonees[3]<740:
        ZoneJeu.move("Joueur", 0, 20)
    elif Action.keysym=="Caps_Lock":
        ZoneJeu.create_line(Coordonees[0], Coordonees[1]+5, Coordonees[2], Coordonees[3], fill="red", width=3, tag="Laser")
        MouvementTir("Laser")

def Tir():
    Coordonnes=ZoneJeu.coords("Joueur")
    ZoneJeu.create_line(Coordonees[0], Coordonees[1]+20, Coordonees[2], Coordonees[3], fill="red", width=5, tag="Laser")
    MouvementTir("Laser")

# Vaisseau du joueur

ZoneJeu.create_line(380, 750, 380, 700, width= 20, fill="orange",tag="Joueur")
ZoneJeu.bind_all("<Key>", Mouvement)



Fenetre.mainloop()