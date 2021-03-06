# -*- coding: utf-8 -*

from tkinter import *
import pygame.mixer
from random import*

# # # # # # # # # # # #    Fenetre    # # # # # # # # # # # #

# Base

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1280x720")
ZoneJeu=Canvas(Fenetre, height=720,width=1280,bg="black")

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

# Zone de jeu et images

         # Images des vaisseaux joueurs 1 et 2

vaisseau2=PhotoImage(file="Images/vaisseau2.gif")
vaisseau1=PhotoImage(file="Images/vaisseau1.gif")
vaisseau3=PhotoImage(file="Images/vaisseau3.gif")

         # Fond d'écran menu, zone de jeu et tutoriel

FondEcran=PhotoImage(file="Images/etoiles.gif")
FondMenu=PhotoImage(file="Images/FondMenu.gif")
FondTutoFR=PhotoImage(file="Images/tuto.gif")
FondTutoENG=PhotoImage(file="Images/TutoENG.gif")

         # Images de victoire dans une partie normale

VictoireJ2=PhotoImage(file="Images/VictoireJoueur2.gif")
VictoireJ1=PhotoImage(file="Images/VictoireJoueur1.gif")

         # Images de victoire dans un Bo3

VictoireJ1Bo3FR=PhotoImage(file="Images/VictoireJoueur1Bo3.gif")
VictoireJ1Bo3ENG=PhotoImage(file="Images/VictoireJoueur1Bo3ENG.gif")
VictoireJ2Bo3FR=PhotoImage(file="Images/VictoireJoueur2Bo3.gif")
VictoireJ2Bo3ENG=PhotoImage(file="Images/VictoireJoueur2Bo3ENG.gif")

            # Images de victoire dans un Bo5

VictoireJ1Bo5FR=PhotoImage(file="Images/VictoireJoueur1Bo5.gif")
VictoireJ1Bo5ENG=PhotoImage(file="Images/VictoireJoueur1Bo5ENG.gif")
VictoireJ2Bo5FR=PhotoImage(file="Images/VictoireJoueur2Bo5.gif")
VictoireJ2Bo5ENG=PhotoImage(file="Images/VictoireJoueur2Bo5ENG.gif")

                     # Sons et bruitages

Sontir=pygame.mixer.Sound('Tir.wav')
Musiquefond=pygame.mixer.Sound('Interstellar.wav')
Musiquejeu=pygame.mixer.Sound('Bit Rush.wav')

          # Variables

DelaiTir1=0
DelaiTir2=0

Anglais=0
Francais=1

AncienneCollision=0
Degats1=5
Degats2=5

CompteurBo=666
Comparaison=0
ScoreSolo=0

Joueur1Bo3=0
Joueur2Bo3=0

Joueur1Bo5=0
Joueur2Bo5=0

musiquematch=0


# # # # # # # # # # # #    Actions des joueurs   # # # # # # # # # # # #


def MouvementJoueur(Action1):

    global DelaiTir1,DelaiTir2

    Coordonees=ZoneJeu.coords("VaisseauJoueur1")
    Coordonees2=ZoneJeu.coords("VaisseauJoueur2")
    CoordoneesJoueur1=ZoneJeu.coords("Joueur1")
    CoordonneesJoueur2=ZoneJeu.coords("Joueur2")

                      # Joueur 1

    if Action1.keysym=="Left" and Coordonees[0]>50:
        ZoneJeu.move("VaisseauJoueur1", -20,0)
        ZoneJeu.move("Joueur1", -20,0)

    elif Action1.keysym=="Right" and Coordonees[0]<890:
        ZoneJeu.move("VaisseauJoueur1", 20, 0)
        ZoneJeu.move("Joueur1", 20, 0)

    elif Action1.keysym=="Up" and Coordonees[1]>400:
        ZoneJeu.move("VaisseauJoueur1", 0, -20)
        ZoneJeu.move("Joueur1", 0, -20)

    elif Action1.keysym=="Down" and Coordonees[1]<650:
        ZoneJeu.move("VaisseauJoueur1", 0, 20)
        ZoneJeu.move("Joueur1", 0, 20)

    elif Action1.keysym=="Control_R" and DelaiTir1==0:
        ZoneJeu.create_line(CoordoneesJoueur1[0]+25, CoordoneesJoueur1[1]-100, CoordoneesJoueur1[2]-25, CoordoneesJoueur1[3]-50, fill="green", width=10, tag="Laser1")
        Sontir.play()
        DelaiTir1=1
        MouvementTirJoueur1("Laser1")

                     # Joueur 2

    elif Action1.char=="q" and Coordonees2[0]>50:
        ZoneJeu.move("VaisseauJoueur2", -20, 0)
        ZoneJeu.move("Joueur2", -20, 0)

    elif Action1.char=="d" and Coordonees2[0]<890:
        ZoneJeu.move("VaisseauJoueur2", 20, 0)
        ZoneJeu.move("Joueur2", 20, 0)

    elif Action1.char=="s" and Coordonees2[1]<300:
        ZoneJeu.move("VaisseauJoueur2", 0, 20)
        ZoneJeu.move("Joueur2", 0, 20)

    elif Action1.char=="z" and Coordonees2[1]>60:
        ZoneJeu.move("VaisseauJoueur2", 0, -20)
        ZoneJeu.move("Joueur2", 0, -20)

    elif Action1.keysym=="Control_L" and DelaiTir2==0:
        ZoneJeu.create_line(CoordonneesJoueur2[0]+15, CoordonneesJoueur2[1]+50, CoordonneesJoueur2[2]-15,CoordonneesJoueur2[3]+100, fill="green", width=10, tag="Laser2")
        Sontir.play()
        DelaiTir2=1
        MouvementTirJoueur2("Laser2")

# # # # # # # # # # # #   Propulsion des tirs  # # # # # # # # # # # #

                 # Joueur 1

def MouvementTirJoueur1(Projectile):
    global DelaiTir1

    id=ZoneJeu.after(12,MouvementTirJoueur1,"Laser1")

    CoordonneesLaser1=ZoneJeu.coords("Laser1")

    ZoneJeu.move(Projectile,0, -15)

    if CoordonneesLaser1[1]<60:
        Fenetre.after_cancel(id)
        ZoneJeu.delete("Laser1")
        DelaiTir1=0

                  # Joueur 2

def MouvementTirJoueur2(Projectile):
    global DelaiTir2

    id=ZoneJeu.after(12,MouvementTirJoueur2,"Laser2")

    CoordonneesLaser2=ZoneJeu.coords("Laser2")

    ZoneJeu.move(Projectile,0, 15)

    if CoordonneesLaser2[1]>680:
        Fenetre.after_cancel(id)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0


# # # # # # # # # # # #    Collision/Degats/Vie    # # # # # # # # # # # #

def ComparaisonDegats():

    global Compa, AncienneCollision, Degats1, Degats2, BoutonRejouer, CompteurBo, Joueur1Bo3,Joueur2Bo3, BoutonRetour,Joueur1Bo5,Joueur2Bo5,ZoneJeu,BoutonRejouer,BoutonFinBo3
    Compa=Fenetre.after(1,ComparaisonDegats)

    # Barre de vie du joueur 1

    CollisionsJoueur1=ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur1")[0],ZoneJeu.coords("Joueur1")[1],ZoneJeu.coords("Joueur1")[2],ZoneJeu.coords("Joueur1")[3])
    NombreCollisionJoueur1=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur1")[0],ZoneJeu.coords("Joueur1")[1],ZoneJeu.coords("Joueur1")[2],ZoneJeu.coords("Joueur1")[3])))

    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==5:
        ZoneJeu.delete(VieJoueurUn5)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==4:
        ZoneJeu.delete(VieJoueurUn4)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==3:
        ZoneJeu.delete(VieJoueurUn3)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==2:
        ZoneJeu.delete(VieJoueurUn2)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1
    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==1:
        ZoneJeu.delete(VieJoueurUn1)
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    # Barre de vie du joueur 2

    CollisionsJoueur2=ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur2")[0],ZoneJeu.coords("Joueur2")[1],ZoneJeu.coords("Joueur2")[2],ZoneJeu.coords("Joueur2")[3])
    NombreCollisionJoueur2=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur2")[0],ZoneJeu.coords("Joueur2")[1],ZoneJeu.coords("Joueur2")[2],ZoneJeu.coords("Joueur2")[3])))

    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==5:
        ZoneJeu.delete(VieJoueurDeux5)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==4:
        ZoneJeu.delete(VieJoueurDeux4)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==3:
        ZoneJeu.delete(VieJoueurDeux3)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==2:
        ZoneJeu.delete(VieJoueurDeux2)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1
    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==1:
        ZoneJeu.delete(VieJoueurDeux1)
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

          # Conditions de victoire dans un match normal

                 # Le joueur 2 gagne une manche

    if Degats1==0 and CompteurBo==0:

        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")

        ZoneJeu.create_image(640,360,image=VictoireJ2)

        if Francais==1:

            BoutonRejouer=Button(ZoneJeu,text="Cliquez ici pour rejouer",command=Rejouer)
            BoutonRejouer.config(height=5,width=30)
            BoutonRejouer.place(x=530,y=400)

            BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourBo)
            BoutonRetour.place(x=530,y=620)

        if Francais==0:
            BoutonRejouer=Button(ZoneJeu,text="Play another game",command=Rejouer)
            BoutonRejouer.config(height=5,width=30)
            BoutonRejouer.place(x=530,y=400)

            BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourBo)
            BoutonRetour.place(x=530,y=620)

                             # Le joueur 1 gagne une manche

    if Degats2==0 and CompteurBo==0:

        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")


        ZoneJeu.create_image(640,360,image=VictoireJ1)

        if Francais==1:

            BoutonRejouer=Button(ZoneJeu,text="Cliquez ici pour rejouer",command=Rejouer)
            BoutonRejouer.config(height=5,width=30)
            BoutonRejouer.place(x=530,y=400)

            BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourBo)
            BoutonRetour.place(x=530,y=620)

        if Francais==0:

            BoutonRejouer=Button(ZoneJeu,text="Play another game",command=Rejouer)
            BoutonRejouer.config(height=5,width=30)
            BoutonRejouer.place(x=530,y=400)

            BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourBo)
            BoutonRetour.place(x=530,y=620)


     # Conditions de victoire dans un Bo3

         # Le joueur 2 gagne une manche

    if Degats1==0 and CompteurBo==3:

        Joueur2Bo3+=1
        print(Joueur2Bo3)

        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")

        if Joueur1Bo3<2 and Joueur2Bo3<2:

            ZoneJeu.create_image(640,360,image=VictoireJ2)

            if Francais==1:

                BoutonRejouer=Button(ZoneJeu,text="Lancer la prochaine manche",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                BoutonRejouer=Button(ZoneJeu,text="Play the next game",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)


                    # Le joueur 2 gagne le Bo3

        if CompteurBo==3 and Joueur2Bo3==2:
            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")



            if Francais ==1:
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo3FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 2 remporte la partie !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo3ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 2 has won the Best of 3 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)



                        # Le joueur 1 gagne la manche

    if Degats2==0 and CompteurBo==3:
        Joueur1Bo3+=1
        print(Joueur1Bo3)

        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")

        if Joueur1Bo3<2 and Joueur2Bo3<2:

            ZoneJeu.create_image(640,360,image=VictoireJ1)

            if Francais==1:

                BoutonRejouer=Button(ZoneJeu,text="Lancer la prochaine manche",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                BoutonRejouer=Button(ZoneJeu,text="Play the next game ",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)


                   # Le joueur 1 remporte le Bo3

        if CompteurBo==3 and Joueur1Bo3==2:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")



            if Francais==1:
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo3FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 1 remporte la partie !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)


            if Francais==0:
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo3ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 1 has just won the best of 3!",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)


         # Conditions de victoire dans un Bo5

             # Joueur 2 gagne la manche

    if Degats1==0 and CompteurBo==5:
         Joueur2Bo5+=1
         print(Joueur2Bo5)

         Fenetre.after_cancel(Compa)
         ZoneJeu.delete("Joueur1")
         ZoneJeu.delete("Joueur2")

         if Joueur1Bo5<3 and Joueur2Bo5<3:

            ZoneJeu.create_image(640,360,image=VictoireJ2)

            if Francais==1:

                BoutonRejouer=Button(ZoneJeu,text="Lancer la prochaine manche",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                BoutonRejouer=Button(ZoneJeu,text="Play the next game",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)

                         # Le joueur 2 remporte le Bo5

         if CompteurBo==5 and Joueur2Bo5==3:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")



            if Francais==1:
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo5FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 2 remporte le Bo5 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo5ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 2 has won the best of 5 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)



                       # Le joueur 1 gagne une manche

    if Degats2==0 and CompteurBo==5:
        Joueur1Bo5+=1
        print(Joueur1Bo5)

        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")

        if Joueur1Bo5<3 and Joueur2Bo5<3:

            ZoneJeu.create_image(640,360,image=VictoireJ1)

            if Francais==1:

                BoutonRejouer=Button(ZoneJeu,text="Cliquez ici pour rejouer",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                BoutonRejouer=Button(ZoneJeu,text="Play the next game",command=Rejouerbo)
                BoutonRejouer.config(height=5,width=30)
                BoutonRejouer.place(x=530,y=400)

                            # Le joueur 1 remporte le Bo5

        if CompteurBo==5 and Joueur1Bo5==3:
            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")



            if Francais==1:
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo5FR)


                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 1 remporte la partie !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo5ENG)


                BoutonFinBo3=Button(ZoneJeu,text="Player 1 has won the best of 5 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourBo)
                BoutonRetour.place(x=530,y=620)



# # # # # # # # # # # #    Menu de lancement    # # # # # # # # # # # #

# Bouton partie rapide

def Lancer():
        global CompteurBo, musiquematch
        CompteurBo=0


        global vaisseau2, vaisseau1
        global VieJoueurDeux5, VieJoueurDeux4, VieJoueurDeux3, VieJoueurDeux2, VieJoueurDeux1
        global VieJoueurUn5, VieJoueurUn4, VieJoueurUn3, VieJoueurUn2, VieJoueurUn1

        BoutonMulti.destroy()
        BoutonSolo.destroy()
        BoutonTuto.destroy()
        BoutonTraductionAnglais.destroy()
        BoutonBo3.destroy()
        BoutonBo5.destroy()
        BoutonPantheon.destroy()

        ZoneJeu.delete("all")

        ZoneJeu.create_image(640,360,image=FondEcran)

        ZoneJeu.create_line(450, 611, 500, 611, width= 20, fill="orange", tag="Joueur1")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)

        ZoneJeu.create_line(460, 100, 490, 100, width= 20, fill="orange", tag="Joueur2")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)


        ZoneJeu.create_image(475,120,image=vaisseau2,tag="VaisseauJoueur2")

        ZoneJeu.create_image(475,600,image=vaisseau1,tag="VaisseauJoueur1")

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

        ZoneJeu.pack()

        ComparaisonDegats()

        if musiquematch==0:
            pygame.mixer.pause()
            Musiquejeu.play()
            musiquematch=1

#Fonction de lancement d'un Bo ( sans CompteurBo=0)

def Lancerbo():

        global vaisseau2, vaisseau1,musiquematch
        global VieJoueurDeux5, VieJoueurDeux4, VieJoueurDeux3, VieJoueurDeux2, VieJoueurDeux1
        global VieJoueurUn5, VieJoueurUn4, VieJoueurUn3, VieJoueurUn2, VieJoueurUn1

        BoutonMulti.destroy()
        BoutonSolo.destroy()
        BoutonTuto.destroy()
        BoutonTraductionAnglais.destroy()
        BoutonBo3.destroy()
        BoutonBo5.destroy()
        BoutonPantheon.destroy()

        ZoneJeu.delete("all")

        ZoneJeu.create_image(640,360,image=FondEcran)

        ZoneJeu.create_line(475, 600, 475, 650, width= 20, fill="orange", tag="Joueur1")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)

        ZoneJeu.create_line(475, 80, 475, 130, width= 20, fill="orange", tag="Joueur2")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)


        ZoneJeu.create_image(475,120,image=vaisseau2,tag="VaisseauJoueur2")

        ZoneJeu.create_image(475,600,image=vaisseau1,tag="VaisseauJoueur1")

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

        ZoneJeu.pack()

        ComparaisonDegats()

        if musiquematch==0:

            pygame.mixer.pause()
            Musiquejeu.play()
            musiquematch=1


# Bouton traduction anglais

def TraductionAnglais():
    global Francais

    Francais=0

    BoutonMulti.config(text="Multiplayer : Quick game")
    BoutonSolo.config(text="Training")
    BoutonTuto.config(text="Tutorial")
    BoutonTraductionAnglais.config(text="Switch to the french version",command=TraductionFrancais)
    BoutonBo3.config(text="Best of 3")
    BoutonBo5.config(text="Best of 5")
    BoutonPantheon.config(text="Best players")

    print(Francais)


# Compteur pour ne pas réinitialiser la variable francais à chaque fois



# Bouton traduction français

def TraductionFrancais():
    global Francais

    Francais=1

    BoutonMulti.config(text="Multijoueur : Partie rapide")
    BoutonSolo.config(text="Mode entraînement")
    BoutonTuto.config(text="Tutoriel")
    BoutonTraductionAnglais.config(text="Passer le jeu en anglais",command=TraductionAnglais)
    BoutonBo3.config(text="Match en trois manches")
    BoutonBo5.config(text="Match en cinq manches")
    BoutonPantheon.config(text="Pantheon des héros")
    print(Francais)


# Bouton tutoriel

def Tuto():

    BoutonMulti.destroy()
    BoutonSolo.destroy()
    BoutonTraductionAnglais.destroy()
    BoutonBo3.destroy()
    BoutonBo5.destroy()
    BoutonPantheon.destroy()


    if Francais==1:
     ZoneJeu.create_image(640,360,image=FondTutoFR)
     BoutonTuto.config(text="Revenir au menu principal", command=Retour)
     BoutonTuto.place(x=120,y=620)

    if Francais==0:
     ZoneJeu.create_image(640,360,image=FondTutoENG)
     BoutonTuto.config(text="Go back to main menu", command=Retour)
     BoutonTuto.place(x=120,y=620)



def RetourBo():
    global ZoneJeu,CompteurBo,Degats1,Degats2,BoutonRejouer,BoutonRetour,BoutonFinBo3,Joueur1Bo3,Joueur2Bo3,Joueur1Bo5,Joueur2Bo5,musiquematch

    BoutonRejouer.destroy()
    BoutonRetour.destroy()

    if CompteurBo==3 or CompteurBo==5:
        BoutonFinBo3.destroy()


    ZoneJeu.delete("all")
    Creationzonejeu()
    Degats2=5
    Degats1=5
    AncienneCollision=0
    Menu()
    CompteurBo=666
    Joueur1Bo3=0
    Joueur2Bo3=0
    Joueur1Bo5=0
    Joueur2Bo5=0

    musiquematch=0
    pygame.mixer.pause()
    Musiquefond.play()



# Bouton rejouer partie normale

def Rejouer():

    global BoutonRejouer, AncienneCollision, Degats1, Degats2,BoutonRetour

    BoutonRejouer.destroy()
    BoutonRetour.destroy()

    ZoneJeu.delete("all")


    AncienneCollision=0
    Degats1=5
    Degats2=5

    Lancer()

# Bouton rejouer Bo ( sans le BoutonRetour.destroy() )

def Rejouerbo():

    global BoutonRejouer, AncienneCollision, Degats1, Degats2,BoutonRetour

    BoutonRejouer.destroy()

    ZoneJeu.delete("all")

    AncienneCollision=0
    Degats1=5
    Degats2=5

    Lancerbo()

# Bouton retour

def Retour():

    global ZoneJeu

    BoutonTuto.destroy()
    ZoneJeu.delete("all")
    ZoneJeu.create_image(640,360,image=FondMenu)
    ZoneJeu.pack()
    Menu()

# Fonction pour lancer le Bo3

def LancerBo3():
    global CompteurBo
    Comparaison=0
    CompteurBo=3
    Lancerbo()

# Fonction pour lancer le Bo5

def LancerBo5():
    global CompteurBo
    Comparaison=0

    CompteurBo=5
    Lancerbo()

# Fonction pour créer le fond d'écran du menu

def Creationzonejeu():
    global ZoneJeu

    ZoneJeu.create_image(640,360,image=FondMenu)
    ZoneJeu.pack()

# Fonction qui lance le mode entraînement

def Lancersolo():

        global Comparaison,Labelscore,BoutonRetourSolo

        Comparaison=1

        BoutonMulti.destroy()
        BoutonSolo.destroy()
        BoutonTuto.destroy()
        BoutonTraductionAnglais.destroy()
        BoutonBo3.destroy()
        BoutonBo5.destroy()
        BoutonPantheon.destroy()

        ZoneJeu.delete("all")

        ZoneJeu.create_image(640,360,image=FondEcran)

        ZoneJeu.create_line(475, 600, 475, 650, width= 20, fill="orange", tag="Joueur1")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)

        ZoneJeu.create_image(475,600,image=vaisseau1,tag="VaisseauJoueur1")

        Labelscore=Label(ZoneJeu,text=ScoreSolo)
        Labelscore.place(x=1000,y=400)

        BoutonRetourSolo=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourSolo)
        BoutonRetourSolo.place(x=1000,y=620)

        ZoneJeu.pack()

        """if musiquematch==0:
            pygame.mixer.pause()
            Musiquejeu.play()
            musiquematch=1"""

        CreationVaisseauSolo()
        CompaSolo()

# Fonction permettant le retour au menu depuis le mode entraînement

def RetourSolo():

        global ZoneJeu,ComparaisonSolo,ScoreSolo,musiquematch,Musiquefond,Comparaison

        ZoneJeu.after_cancel(ComparaisonSolo)
        ScoreSolo=0
        Comparaison=0
        Labelscore.destroy()

        ZoneJeu.delete("all")

        Creationzonejeu()
        Menu()
        musiquematch=0
        pygame.mixer.pause()
        Musiquefond.play()

# Fonction qui crée les vaisseaux IA

def CreationVaisseauSolo():

    global VaisseauIA

    x1=randint(100,800)
    ZoneJeu.create_rectangle(x1,150,x1+19,200,fill="orange",tag="VaisseauSolo")
    ZoneJeu.create_image(x1+10,170,image=vaisseau3,tag="VaisseauJoueur3")
    ZoneJeu.pack()

# Fonction de comparaison des dégats subis par les vaisseaux IA

def CompaSolo():

    global ComparaisonSolo,ScoreSolo,Labelscore

    ComparaisonSolo=Fenetre.after(1,CompaSolo)

    NombreCollisionSolo=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("VaisseauSolo")[0],ZoneJeu.coords("VaisseauSolo")[1],ZoneJeu.coords("VaisseauSolo")[2],ZoneJeu.coords("VaisseauSolo")[3])))
    print(NombreCollisionSolo)

    if NombreCollisionSolo!=3:

        ScoreSolo+=1
        Labelscore.config(text=ScoreSolo)

        ZoneJeu.delete("VaisseauSolo")
        ZoneJeu.delete("VaisseauJoueur3")

        Fenetre.after_cancel(ComparaisonSolo)
        CreationVaisseauSolo()
        ComparaisonSolo=Fenetre.after(1,CompaSolo)

# Fonction menu principal

def Menu():

    global BoutonMulti, BoutonSolo, BoutonTuto, BoutonTraductionAnglais, BoutonBo3, BoutonBo5, ZoneJeu,BoutonPantheon, Francais,Comparaison
    Comparaison=0


    BoutonMulti=Button(ZoneJeu,text="Multijoueur : Partie rapide",command=Lancer)
    BoutonMulti.config(height=5,width=30)
    BoutonMulti.place(x=80,y=300)

    BoutonSolo=Button(ZoneJeu,text="Mode entraînement",command=Lancersolo)
    BoutonSolo.config(height=5,width=30)
    BoutonSolo.place(x=1000,y=300)

    BoutonTuto=Button(ZoneJeu,text="Tutoriel")
    BoutonTuto.config(height=5,width=30,command=Tuto)
    BoutonTuto.place(x=530,y=620)

    BoutonTraductionAnglais=Button(ZoneJeu, text=" Passer le jeu en anglais",command=TraductionAnglais)
    BoutonTraductionAnglais.config(height=5,width=30)
    BoutonTraductionAnglais.place(x=1000,y=620)

    BoutonBo3=Button(ZoneJeu,text="Match en trois manches",command=LancerBo3)
    BoutonBo3.config(height=5,width=30)
    BoutonBo3.place(x=80,y=620)

    BoutonBo5=Button(ZoneJeu,text="Match en cinq manches",command=LancerBo5)
    BoutonBo5.config(height=5,width=30)
    BoutonBo5.place(x=80,y=520)

    BoutonPantheon=Button(text="Panthéon des héros",height=5,width=30,relief=SUNKEN)
    BoutonPantheon.place(x=1000,y=520)


    if Francais==0:
        TraductionAnglais()
        print(Francais)

    if Francais==1:
        TraductionFrancais()
        print(Francais)

    Musiquefond.play()

def FermetureFenetre():

    global Comparaison,BoutonRetourSolo,Labelscore

    if Comparaison==1:

        #pygame.mixer.pause()
        Fenetre.after_cancel(ComparaisonSolo)
        BoutonRetourSolo.destroy()
        Labelscore.destroy()
        #ZoneJeu.delete("all")
        #ZoneJeu.destroy()
        Fenetre.destroy()

    if Comparaison==0:

        pygame.mixer.pause()
        Fenetre.destroy()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Fenetre.protocol('WM_DELETE_WINDOW', FermetureFenetre)

def Getpseudo1():

    global Nom1,Pseudo1

    Nom1=Pseudo1.get()
    print(Nom1)
    Pseudo1.destroy()
    BoutonPseudo1.destroy()
    fichierpseudo=open("Pseudos.txt", "a")
    fichierpseudo.write(Nom1)
    fichierpseudo.write("\n")
    fichierpseudo.close()

def Getpseudo2():

    global Nom2,Pseudo2

    Nom2=Pseudo2.get()
    print(Nom2)
    Pseudo2.destroy()
    BoutonPseudo2.destroy()
    fichierpseudo=open("Pseudos.txt", "a")
    fichierpseudo.write(Nom2)
    fichierpseudo.write("\n")
    fichierpseudo.close()
    fi=open("Pseudos.txt", "r")
    chainepseudo=fi.read()
    print(chainepseudo)
    chainepseudo=list(chainepseudo)
    print(chainepseudo)


"""Pseudo1=Entry(ZoneJeu)
Pseudo1.place(x=400,y=300)
BoutonPseudo1=Button(ZoneJeu,text="Valider",width=10,height=5,command=Getpseudo1)
BoutonPseudo1.place(x=400,y=320)

Pseudo2=Entry(ZoneJeu)
Pseudo2.place(x=600,y=300)
BoutonPseudo2=Button(ZoneJeu,text="Valider",width=10,height=5,command=Getpseudo2)
BoutonPseudo2.place(x=600,y=320)"""


Creationzonejeu()

Menu()

Fenetre.mainloop()