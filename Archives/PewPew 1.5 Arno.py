# -*- coding: utf-8 -*

from tkinter import *


               #Création de la fenêtre et des différentes variables :

Fenetre= Tk()
FondMenu=PhotoImage(file="Images/FondMenu.gif")

ZoneJeu=Canvas(Fenetre, height=720,width=1280,bg="black")
ZoneJeu.create_image(640,360,image=FondMenu)
ZoneJeu.pack()



Fenetre.title("Pew Pew")
Fenetre.geometry("1280x720")

vaisseau1=PhotoImage(file="Images/vaisseau1.gif")
vaisseau2=PhotoImage(file="Images/vaisseau2.gif")

fondecran=PhotoImage(file="Images/etoiles.gif")

FondTuto=PhotoImage(file="Images/tuto.gif")

DelaiTir=0

               #Fonction qui lance le mode multijoueur :
def Lancer():
    global vaisseau2

    BoutonMulti.destroy()
    BoutonSolo.destroy()
    BoutonTuto.destroy()
    BoutonTraductionAnglais.destroy()
    BoutonBo3.destroy()
    BoutonBo5.destroy()

    ZoneJeu.create_image(640,360,image=fondecran)

                    #Rectangle + image (vaisseau 2) :

    ZoneJeu.create_line(250, 20, 250, 70, width= 20, fill="orange", tag="Joueur2")
    ZoneJeu.create_image(250,50,image=vaisseau2,tag="VaisseauJoueur2")

                    #Rectangle + image (vaisseau 1) :

    ZoneJeu.create_line(250, 650, 250, 675, width= 20, fill="orange", tag="Joueur1")
    ZoneJeu.create_image(250,648,image=vaisseau1,tag="VaisseauJoueur1")

    ZoneJeu.bind_all("<Key>", MouvementJoueur1)
    ZoneJeu.create_line(1200,0,1200,1080,width=20,fill="black")

    ZoneJeu.create_line(1200,550,2000,550,width=20,fill="black")

            # Fonction de mouvement (joueur 1 et 2)

def MouvementJoueur1(Action1):
    global DelaiTir

                 #####JOUEUR 1####

    Coordonees=ZoneJeu.coords("VaisseauJoueur1")
    Coordonees2=ZoneJeu.coords("VaisseauJoueur2")
    CoordoneesJoueur1=ZoneJeu.coords("Joueur1")
    CoordonneesJoueur2=ZoneJeu.coords("Joueur2")


    if Action1.keysym=="Left" and Coordonees[0]>60:
        ZoneJeu.move("VaisseauJoueur1", -20,0)
        ZoneJeu.move("Joueur1", -20,0)

    elif Action1.keysym=="Right" and Coordonees[0]<1100:
        ZoneJeu.move("VaisseauJoueur1", 20, 0)
        ZoneJeu.move("Joueur1", 20, 0)

    elif Action1.keysym=="Up" and Coordonees[1]>600:
        ZoneJeu.move("VaisseauJoueur1", 0, -20)
        ZoneJeu.move("Joueur1", 0, -20)

    elif Action1.keysym=="Down" and Coordonees[1]<980:
        ZoneJeu.move("VaisseauJoueur1", 0, 20)
        ZoneJeu.move("Joueur1", 0, 20)

    elif Action1.keysym=="Shift_R" and DelaiTir==0:
        ZoneJeu.create_line(CoordoneesJoueur1[0], CoordoneesJoueur1[1]-20, CoordoneesJoueur1[2], CoordoneesJoueur1[3], fill="red", width=3, tag="Laser")
        DelaiTir=1
        MouvementTirJoueur1("Laser")

                  #####JOUEUR 2#####

    elif Action1.char=="q" and Coordonees2[0]>60:
        ZoneJeu.move("VaisseauJoueur2", -20, 0)
        ZoneJeu.move("Joueur2", -20, 0)

    elif Action1.char=="d" and Coordonees2[0]<1150:
        ZoneJeu.move("VaisseauJoueur2", 20, 0)
        ZoneJeu.move("Joueur2", 20, 0)

    elif Action1.char=="s" and Coordonees2[1]<330:
        ZoneJeu.move("VaisseauJoueur2", 0, 20)
        ZoneJeu.move("Joueur2", 0, 20)

    elif Action1.char=="z" and Coordonees2[1]>60:
        ZoneJeu.move("VaisseauJoueur2", 0, -20)
        ZoneJeu.move("Joueur2", 0, -20)

    elif Action1.keysym=="space" and DelaiTir==0:
        ZoneJeu.create_line(CoordonneesJoueur2[0], CoordonneesJoueur2[1], CoordonneesJoueur2[2],CoordonneesJoueur2[3], fill="red", width=3, tag="Laser2")
        DelaiTir=1
        MouvementTirJoueur2("Laser2")

def TraductionAnglais():

    BoutonMulti.config(text="Multiplayer")
    BoutonSolo.config(text="CoopVsBot")
    BoutonTuto.config(text="Tutorial")
    BoutonTraductionAnglais.config(text="Passer le jeu en français",command=TraductionFrancais)
    BoutonBo3.config(text="Best of 3")
    BoutonBo5.config(text="Best of 5")

def TraductionFrancais():

    BoutonMulti.config(text="Multijoueur")
    BoutonSolo.config(text="Joueur contre IA")
    BoutonTuto.config(text="Tutoriel")
    BoutonTraductionAnglais.config(text="Switch to the English version",command=TraductionAnglais)
    BoutonBo3.config(text="Match en trois manches")
    BoutonBo5.config(text="Match en cinq manches")

def Tuto():
    BoutonMulti.destroy()
    BoutonSolo.destroy()
    BoutonTraductionAnglais.destroy()
    BoutonBo3.destroy()
    BoutonBo5.destroy()
    ZoneJeu.create_image(640,360,image=FondTuto)
    BoutonTuto.config(text="Revenir au menu principal")

      #Fonction pour faire bouger le projectile (joueur 2) :

def MouvementTirJoueur2(Projectile):
    global DelaiTir

    id=ZoneJeu.after(15,MouvementTirJoueur2,"Laser2")

    CoordonneesLaser2=ZoneJeu.coords("Laser2")
    print(CoordonneesLaser2)

    ZoneJeu.move(Projectile,0, 7)

    if CoordonneesLaser2[1]>600:
        Fenetre.after_cancel(id)
        ZoneJeu.delete("Laser2")
        DelaiTir=0

      #Fonction pour faire bouger le projectile (joueur 1) :

def MouvementTirJoueur1(Projectile):
    ZoneJeu.after(100,MouvementTirJoueur1,"Laser")
    ZoneJeu.move(Projectile,0, -5)


BoutonMulti=Button(ZoneJeu,text="Multijoueur",command=Lancer)
BoutonMulti.config(height=5,width=30)
BoutonMulti.place(x=80,y=300)

BoutonSolo=Button(ZoneJeu,text="Joueur contre IA",relief=SUNKEN)
BoutonSolo.config(height=5,width=30)
BoutonSolo.place(x=1000,y=300)

BoutonTuto=Button(ZoneJeu,text="Tutoriel")
BoutonTuto.config(height=5,width=30,command=Tuto)
BoutonTuto.place(x=530,y=620)

BoutonTraductionAnglais=Button(ZoneJeu, text=" Switch to the English version",command=TraductionAnglais)
BoutonTraductionAnglais.config(height=5,width=30)
BoutonTraductionAnglais.place(x=1000,y=620)

BoutonBo3=Button(ZoneJeu,text="Match en trois manches")
BoutonBo3.config(height=5,width=30)
BoutonBo3.place(x=80,y=620)

BoutonBo5=Button(ZoneJeu,text="Match en cinq manches")
BoutonBo5.config(height=5,width=30)
BoutonBo5.place(x=80,y=520)



Fenetre.mainloop()