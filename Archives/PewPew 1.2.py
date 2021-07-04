from tkinter import *

# Fenetre

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1920x1080")

# Zone de jeu

fondecran=PhotoImage(file="Essai.gif")

ZoneJeu=Canvas(Fenetre, height=1080,width=1920,bg="black")
ZoneJeu.create_image(500,400,image=fondecran)
ZoneJeu.pack()




# Gestion des ennemis:

# Fonction de tir

def Tir():
    Coordonnes=ZoneJeu.coords("Joueur1")
    ZoneJeu.create_line(Coordonees[0], Coordonees[1]+20, Coordonees[2], Coordonees[3], fill="red", width=5, tag="Laser")
    MouvementTir("Laser")

def MouvementTir(Projectile):
    ZoneJeu.after(100,MouvementTir,"Laser")
    ZoneJeu.move(Projectile,0, -5)


# Fonction de mouvement (joueur 1)

def Mouvement(Action):
    Coordonees=ZoneJeu.coords("Joueur1")
    if Action.keysym=="Left" and Coordonees[0]>20:
        ZoneJeu.move("Joueur1", -20,0)
    elif Action.keysym=="Right" and Coordonees[2]<780:
        ZoneJeu.move("Joueur1", 20, 0)
    elif Action.keysym=="Up" and Coordonees[1]>650:
        ZoneJeu.move("Joueur1", 0, -20)
    elif Action.keysym=="Down" and Coordonees[3]<740:
        ZoneJeu.move("Joueur1", 0, 20)
    elif Action.keysym=="Shift_R":
        ZoneJeu.create_line(Coordonees[0], Coordonees[1]+5, Coordonees[2], Coordonees[3], fill="red", width=3, tag="Laser")
        MouvementTir("Laser")

#Fonction de mouvement (joueur 2)


def Tir():
    Coordonnes=ZoneJeu.coords("Joueur")
    ZoneJeu.create_line(Coordonees[0], Coordonees[1]+20, Coordonees[2], Coordonees[3], fill="red", width=5, tag="Laser")
    MouvementTir("Laser")

# Vaisseau 1 (flèches)



ZoneJeu.create_line(380, 750, 380, 700, width= 20, fill="orange",tag="Joueur1")
ZoneJeu.bind_all("<Key>", Mouvement)

#Vaisseau 2 (ZQSD)

ZoneJeu.create_line(380, 100, 380, 50, width= 20, fill="orange", tag="Joueur2")
ZoneJeu.bind_all("<Key>", Mouvement)


Fenetre.mainloop()