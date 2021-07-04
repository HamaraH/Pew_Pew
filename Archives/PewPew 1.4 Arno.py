# -*- coding: utf-8 -*

from tkinter import *

# Fenetre

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1920x1080")

# Zone de jeu

fondecran=PhotoImage(file="Images/etoiles.gif")

ZoneJeu=Canvas(Fenetre, height=1080,width=1920,bg="black")
ZoneJeu.create_image(950,510,image=fondecran)
ZoneJeu.pack()

############# JOUEUR 1 ###############

# Fonction de tir ( joueur 1)  §§§§§§ USELESS §§§§§§§

def TirJoueur1():
    Coordonnes=ZoneJeu.coords("Joueur1")
    ZoneJeu.create_line(Coordonees[0], Coordonees[1]+20, Coordonees[2], Coordonees[3], fill="red", width=5, tag="Laser")
    MouvementTirJoueur1("Laser")



#Fonction pour faire avancer les projectiles (joueur 1)

def MouvementTirJoueur1(Projectile):
    ZoneJeu.after(100,MouvementTirJoueur1,"Laser")
    ZoneJeu.move(Projectile,0, -5)

# Fonction de mouvement (joueur 1 et 2)

def MouvementJoueur1(Action1):

                 #####JOUEUR 1####

    Coordonees=ZoneJeu.coords("VaisseauJoueur1")
    Coordonees2=ZoneJeu.coords("VaisseauJoueur2")
    CoordoneesJoueur1=ZoneJeu.coords("Joueur1")
    CoordonneesJoueur2=ZoneJeu.coords("Joueur2")


    if Action1.keysym=="Left" and Coordonees[0]>60:
        ZoneJeu.move("VaisseauJoueur1", -20,0)
        ZoneJeu.move("Joueur1", -20,0)

    elif Action1.keysym=="Right" and Coordonees[0]<1000:
        ZoneJeu.move("VaisseauJoueur1", 20, 0)
        ZoneJeu.move("Joueur1", 20, 0)

    elif Action1.keysym=="Up" and Coordonees[1]>600:
        ZoneJeu.move("VaisseauJoueur1", 0, -20)
        ZoneJeu.move("Joueur1", 0, -20)

    elif Action1.keysym=="Down" and Coordonees[1]<980:
        ZoneJeu.move("VaisseauJoueur1", 0, 20)
        ZoneJeu.move("Joueur1", 0, 20)

    elif Action1.keysym=="Shift_R":
        ZoneJeu.create_line(CoordoneesJoueur1[0], CoordoneesJoueur1[1]+5, CoordoneesJoueur1[2], CoordoneesJoueur1[3], fill="red", width=3, tag="Laser")
        MouvementTirJoueur1("Laser")

                  #####JOUEUR 2#####

    elif Action1.char=="q" and Coordonees2[0]>60:
        ZoneJeu.move("VaisseauJoueur2", -20, 0)
        ZoneJeu.move("Joueur2", -20, 0)

    elif Action1.char=="d" and Coordonees2[0]<1000:
        ZoneJeu.move("VaisseauJoueur2", 20, 0)
        ZoneJeu.move("Joueur2", 20, 0)

    elif Action1.char=="s" and Coordonees2[1]<450:
        ZoneJeu.move("VaisseauJoueur2", 0, 20)
        ZoneJeu.move("Joueur2", 0, 20)

    elif Action1.char=="z" and Coordonees2[1]>60:
        ZoneJeu.move("VaisseauJoueur2", 0, -20)
        ZoneJeu.move("Joueur2", 0, -20)

    elif Action1.keysym=="Caps_Lock":
        ZoneJeu.create_line(CoordonneesJoueur2[0], CoordonneesJoueur2[1], CoordonneesJoueur2[2],CoordonneesJoueur2[3], fill="red", width=3, tag="Laser2")
        MouvementTirJoueur2("Laser2")

             ######JOUEUR 2 ########

#Fonction pour faire bouger le projectile (joueur 2)

def MouvementTirJoueur2(Projectile):

    ZoneJeu.after(100,MouvementTirJoueur2,"Laser2")
    ZoneJeu.move(Projectile,0, 5)

#Rectangle vaisseau2 :

ZoneJeu.create_line(250, 25, 250, 87, width= 20, fill="orange", tag="Joueur2")
ZoneJeu.bind_all("<Key>", MouvementJoueur1)

#Rectangle vaisseau1 :

ZoneJeu.create_line(250, 670, 250, 740, width= 20, fill="orange", tag="Joueur1")
ZoneJeu.bind_all("<Key>", MouvementJoueur1)

#Vaisseau 2(ZQSD):

vaisseau2=PhotoImage(file="Images/vaisseau2.gif")

ZoneJeu.create_image(250,50,image=vaisseau2,tag="VaisseauJoueur2")
ZoneJeu.pack()

#Vaisseau 1( flèches direct):

vaisseau1=PhotoImage(file="Images/vaisseau1.gif")

ZoneJeu.create_image(250,700,image=vaisseau1,tag="VaisseauJoueur1")
ZoneJeu.pack()

Fenetre.mainloop()