from tkinter import *

# Fenetre

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1920x1080")

# Zone de jeu

fondecran=PhotoImage(file="etoiles.gif")

ZoneJeu=Canvas(Fenetre, height=1080,width=1920,bg="black")
ZoneJeu.create_image(950,510,image=fondecran)
ZoneJeu.pack()


############# JOUEUR 1 ###############

# Fonction de tir ( joueur 1)

def TirJoueur1():
    Coordonnes=ZoneJeu.coords("Joueur1")
    ZoneJeu.create_line(Coordonees[0], Coordonees[1]+20, Coordonees[2], Coordonees[3], fill="red", width=5, tag="Laser")
    MouvementTirJoueur1("Laser")

#Fonction pour faire avancer les projectiles ( joueur 1)

def MouvementTirJoueur1(Projectile):
    ZoneJeu.after(100,MouvementTirJoueur1,"Laser")
    ZoneJeu.move(Projectile,0, -5)

# Fonction de mouvement (joueur 1)

def MouvementJoueur1(Action1):
    Coordonees=ZoneJeu.coords("Joueur1")
    if Action1.keysym=="Left" and Coordonees[0]>20:
        ZoneJeu.move("Joueur1", -20,0)
    elif Action1.keysym=="Right" and Coordonees[2]<780:
        ZoneJeu.move("Joueur1", 20, 0)
    elif Action1.keysym=="Up" and Coordonees[1]>650:
        ZoneJeu.move("Joueur1", 0, -20)
    elif Action1.keysym=="Down" and Coordonees[3]<740:
        ZoneJeu.move("Joueur1", 0, 20)
    elif Action1.keysym=="Shift_R":
        ZoneJeu.create_line(Coordonees[0], Coordonees[1]+5, Coordonees[2], Coordonees[3], fill="red", width=3, tag="Laser")
        MouvementTirJoueur1("Laser")

# Vaisseau joueur 1 (flèches)

ZoneJeu.create_line(380, 750, 380, 700, width= 20, fill="orange",tag="Joueur1")
ZoneJeu.bind_all("<Key>", MouvementJoueur1)

########JOUEUR 2 #########

#Fonction de mouvement (joueur 2)

def MouvementJoueur2(Action2):
    Coordonees2=ZoneJeu.coords("Joueur2")
    if Action2.keysym=="Control_L" and Coordonees2[0]>20:
        ZoneJeu.move("Joueur2", -20,0)
    elif Action2.keysym=="Control_R" and Coordonees2[2]<780:
        ZoneJeu.move("Joueur2", 20, 0)
    elif Action2.keysym=="Shift_L" and Coordonees2[1]>650:
        ZoneJeu.move("Joueur2", 0, -20)
    elif Action2.keysym=="Shift_R" and Coordonees2[3]<740:
        ZoneJeu.move("Joueur2", 0, 20)
    elif Action2.keysym=="":
        ZoneJeu.create_line(Coordonees2[0], Coordonees2[1]+5, Coordonees2[2], Coordonees2[3], fill="red", width=3, tag="Laser")
        MouvementTir("Laser")


#Vaisseau 2 (ZQSD)

ZoneJeu.create_line(380, 100, 380, 50, width= 20, fill="orange", tag="Joueur2")
ZoneJeu.bind_all("<Key>", MouvementJoueur2)


Fenetre.mainloop()