# -*- coding: utf-8 -*

from tkinter import *

# Fenetre

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1280x720")

# Zone de jeu

vaisseau2=PhotoImage(file="Images/vaisseau2.gif")
vaisseau1=PhotoImage(file="Images/vaisseau1.gif")
fondecran=PhotoImage(file="Images/etoiles.gif")
FondMenu=PhotoImage(file="Images/FondMenu.gif")
FondTuto=PhotoImage(file="Images/tuto.gif")

ZoneJeu=Canvas(Fenetre, height=720,width=1280,bg="black")
ZoneJeu.create_image(640,360,image=FondMenu)
ZoneJeu.pack()

DelaiTir=0

# Fonction de mouvement (joueur 1 et 2)

def MouvementJoueur1(Action1):
    global DelaiTir

    Coordonees=ZoneJeu.coords("VaisseauJoueur1")
    Coordonees2=ZoneJeu.coords("VaisseauJoueur2")
    CoordoneesJoueur1=ZoneJeu.coords("Joueur1")
    CoordonneesJoueur2=ZoneJeu.coords("Joueur2")

                #####JOUEUR 1####

    if Action1.keysym=="Left" and Coordonees[0]>60:
        ZoneJeu.move("VaisseauJoueur1", -20,0)
        ZoneJeu.move("Joueur1", -20,0)

    elif Action1.keysym=="Right" and Coordonees[0]<1100:
        ZoneJeu.move("VaisseauJoueur1", 20, 0)
        ZoneJeu.move("Joueur1", 20, 0)

    elif Action1.keysym=="Up" and Coordonees[1]>430:
        ZoneJeu.move("VaisseauJoueur1", 0, -20)
        ZoneJeu.move("Joueur1", 0, -20)

    elif Action1.keysym=="Down" and Coordonees[1]<980:
        ZoneJeu.move("VaisseauJoueur1", 0, 20)
        ZoneJeu.move("Joueur1", 0, 20)

    elif Action1.keysym=="Control_R" and DelaiTir==0:
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

    elif Action1.keysym=="Control_L":
        ZoneJeu.create_line(CoordonneesJoueur2[0], CoordonneesJoueur2[1]+100, CoordonneesJoueur2[2],CoordonneesJoueur2[3]+100, fill="red", width=3, tag="Laser2")
        DelaiTir=1
        MouvementTirJoueur2("Laser2")

             ######JOUEUR 2 ########

#Fonction pour faire avancer les projectiles (joueur 1)

def MouvementTirJoueur1(Projectile):
    ZoneJeu.after(100,MouvementTirJoueur1,"Laser")
    ZoneJeu.move(Projectile,0, -5)

#Fonction pour faire bouger le projectile (joueur 2)

def MouvementTirJoueur2(Projectile):

    ZoneJeu.after(100,MouvementTirJoueur2,"Laser2")
    ZoneJeu.move(Projectile,0, 5)


# # # # # # # # # # # #    Collision/Degats/Vie    # # # # # # # # # # # #

AncienneCollision=0
Degats1=5
Degats2=5

def ComparaisonDegats():


    global Compa, AncienneCollision, Degats1, Degats2
    Compa=Fenetre.after(1,ComparaisonDegats)

    # Barre de vie du joueur 1

    CollisionsJoueur1=ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur1")[0],ZoneJeu.coords("Joueur1")[1],ZoneJeu.coords("Joueur1")[2],ZoneJeu.coords("Joueur1")[3])
    NombreCollisionJoueur1=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur1")[0],ZoneJeu.coords("Joueur1")[1],ZoneJeu.coords("Joueur1")[2],ZoneJeu.coords("Joueur1")[3])))

    if NombreCollisionJoueur1 != 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==5:
        ZoneJeu.delete(VieJoueurDeux5)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 != 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==4:
        ZoneJeu.delete(VieJoueurDeux4)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 != 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==3:
        ZoneJeu.delete(VieJoueurDeux3)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 != 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==2:
        ZoneJeu.delete(VieJoueurDeux2)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 != 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==1:
        ZoneJeu.delete(VieJoueurDeux1)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    # Barre de vie du joueur 2

    CollisionsJoueur2=ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur2")[0],ZoneJeu.coords("Joueur2")[1],ZoneJeu.coords("Joueur2")[2],ZoneJeu.coords("Joueur2")[3])
    NombreCollisionJoueur2=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur2")[0],ZoneJeu.coords("Joueur2")[1],ZoneJeu.coords("Joueur2")[2],ZoneJeu.coords("Joueur2")[3])))

    if NombreCollisionJoueur2 != 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==5:
        ZoneJeu.delete(VieJoueurUn5)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 != 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==4:
        ZoneJeu.delete(VieJoueurUn4)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 != 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==3:
        ZoneJeu.delete(VieJoueurUn3)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 != 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==2:
        ZoneJeu.delete(VieJoueurUn2)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 != 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==1:
        ZoneJeu.delete(VieJoueurUn1)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def Lancer():

    global vaisseau2, vaisseau1


    BoutonMulti.destroy()
    BoutonSolo.destroy()
    BoutonTuto.destroy()
    BoutonTraductionAnglais.destroy()
    BoutonBo3.destroy()
    BoutonBo5.destroy()

    ZoneJeu.create_image(640,360,image=fondecran)

    ZoneJeu.create_line(250, 600, 250, 650, width= 20, fill="orange", tag="Joueur1")
    ZoneJeu.bind_all("<Key>", MouvementJoueur1)

    ZoneJeu.create_line(250, 20, 250, 70, width= 20, fill="orange", tag="Joueur2")
    ZoneJeu.bind_all("<Key>", MouvementJoueur1)


    ZoneJeu.create_image(250,50,image=vaisseau2,tag="VaisseauJoueur2")

    ZoneJeu.create_image(250,600,image=vaisseau1,tag="VaisseauJoueur1")

    VieJoueurUn1= ZoneJeu.create_rectangle (1015+(30*1),550,1035+(30*1),587, fill="blue")
    VieJoueurUn2= ZoneJeu.create_rectangle (1007+(30*2),550,1027+(30*2),587, fill="blue")
    VieJoueurUn3= ZoneJeu.create_rectangle (999+(30*3),550,1019+(30*3),587, fill="blue")
    VieJoueurUn4= ZoneJeu.create_rectangle (991+(30*4),550,1011+(30*4),587, fill="blue")
    VieJoueurUn5= ZoneJeu.create_rectangle (983+(30*5),550,1003+(30*5),587, fill="blue")

    VieJoueurDeux1= ZoneJeu.create_rectangle (1015+(30*1),100,1035+(30*1),137, fill="red")
    VieJoueurDeux2= ZoneJeu.create_rectangle (1007+(30*2),100,1027+(30*2),137, fill="red")
    VieJoueurDeux3= ZoneJeu.create_rectangle (999+(30*3),100,1019+(30*3),137, fill="red")
    VieJoueurDeux4= ZoneJeu.create_rectangle (991+(30*4),100,1011+(30*4),137, fill="red")
    VieJoueurDeux5= ZoneJeu.create_rectangle (983+(30*5),100,1003+(30*5),137, fill="red")

    global VieJoueurDeux5, VieJoueurDeux4, VieJoueurDeux3, VieJoueurDeux2, VieJoueurDeux1
    global VieJoueurUn5, VieJoueurUn4, VieJoueurUn3, VieJoueurUn2, VieJoueurUn1
    ZoneJeu.pack()
    ComparaisonDegats()


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