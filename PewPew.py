# -*- coding: utf-8 -*
from tkinter import *
import pygame.mixer
from random import*

        # Base (Fenêtre, Canvas, mixer)

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1280x720")
ZoneJeu=Canvas(Fenetre,height=720,width=1280,bg="black")                        # Création de la fenêtre, du Canvas qui servira de zone de jeu et initialisation du mixer pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

         # Images des vaisseaux joueurs 1 et 2

vaisseau2=PhotoImage(file="Images/vaisseau2.gif")
vaisseau1=PhotoImage(file="Images/vaisseau1.gif")                               # Création des variables qui correspondent aux différents coloris de vaisseaux
vaisseau3=PhotoImage(file="Images/vaisseau3.gif")

         # Fond d'écran menu, zone de jeu et tutoriel

FondEcran=PhotoImage(file="Images/etoiles.gif")
FondMenu=PhotoImage(file="Images/FondMenu.gif")                                 # Création des variables qui correspondent aux différents fonds utilisés dans les modes de jeu/menus
FondTutoFR=PhotoImage(file="Images/tuto.gif")
FondTutoENG=PhotoImage(file="Images/TutoENG.gif")

         # Images de victoire dans une partie normale

VictoireJ2FR=PhotoImage(file="Images/VictoireJoueur2.gif")
VictoireJ1FR=PhotoImage(file="Images/VictoireJoueur1.gif")
VictoireJ2ENG=PhotoImage(file="Images/VictoireJoueur2ENG.gif")                  # Création des variables qui correspondent aux images de victoire d'une partie normale
VictoireJ1ENG=PhotoImage(file="Images/VictoireJoueur1ENG.gif")

         # Images de victoire dans un Bo3

VictoireJ1Bo3FR=PhotoImage(file="Images/VictoireJoueur1Bo3.gif")
VictoireJ1Bo3ENG=PhotoImage(file="Images/VictoireJoueur1Bo3ENG.gif")
VictoireJ2Bo3FR=PhotoImage(file="Images/VictoireJoueur2Bo3.gif")                # Création des variables qui correspondent aux images de victoire d'une partie en trois manches
VictoireJ2Bo3ENG=PhotoImage(file="Images/VictoireJoueur2Bo3ENG.gif")

            # Images de victoire dans un Bo5

VictoireJ1Bo5FR=PhotoImage(file="Images/VictoireJoueur1Bo5.gif")
VictoireJ1Bo5ENG=PhotoImage(file="Images/VictoireJoueur1Bo5ENG.gif")
VictoireJ2Bo5FR=PhotoImage(file="Images/VictoireJoueur2Bo5.gif")                # Création des variables qui correspondent aux images de victoire d'une partie en cinq manches
VictoireJ2Bo5ENG=PhotoImage(file="Images/VictoireJoueur2Bo5ENG.gif")

                     # Sons et bruitages

Sontir=pygame.mixer.Sound('Musiques/Tir.wav')
Musiquefond=pygame.mixer.Sound('Musiques/Interstellar.wav')
Musiquejeu=pygame.mixer.Sound('Musiques/Bit Rush.wav')                                   # Création des variables qui correspondent aux différents sons utilisés
Victoire=pygame.mixer.Sound('Musiques/Victoire.wav')

          # Variables

Nom1="Joueur 1"
Nom2="Joueur 2"                                    # Création des variables qui correspondent aux pseudos par défaut, VariablePseudo permet de ne pas réinitialiser les pseudos une fois qu'ils ont été choisis par l'utilisateur
VariablePseudo1=0
VariablePseudo2=0

DelaiTir1=0                                                                     # Les variables DelaiTir servent à empêcher l'action de " spammer " les touches de tir, c'est à dire d'abuser de la vitesse de tir possible
DelaiTir2=0

Francais=1                                                                      # La variable Francais indique la langue du jeu, 1= Français, 0= Anglais

AncienneCollision=0
Degats1=5
Degats2=5

CompteurBo=0                                              # La variable CompteurBo sert a indiquer le mode de jeu/menu dans lequel on se trouve : 0=menu principal, 1=partie normale, 2=entrainement, 3=Bo3, 5=Bo5 et 666=tutoriel
Comparaison=0
ScoreSolo=0

Joueur1Bo3=0
Joueur2Bo3=0
                                                                                # Ces variables servent à compter les manches gagnées par les joueurs lors d'un Bo3 ou d'un Bo5
Joueur1Bo5=0
Joueur2Bo5=0

musiquematch=0                                                                  # Cette variable permet de laisser la musique de jeu activée tant que nous ne sommes pas de retour au menu principal

# # # # # # # # # # # #    Actions des joueurs   # # # # # # # # # # # #

def MouvementJoueur(Action1):
    global DelaiTir1,DelaiTir2

    Coordonees=ZoneJeu.coords("VaisseauJoueur1")
    Coordonees2=ZoneJeu.coords("VaisseauJoueur2")
    CoordoneesJoueur1=ZoneJeu.coords("Joueur1")
    CoordonneesJoueur2=ZoneJeu.coords("Joueur2")

                      # Joueur 1
    if CompteurBo!=0:

        if Action1.keysym=="Left" and Coordonees[0]>50:

            ZoneJeu.move("VaisseauJoueur1", -20,0)
            ZoneJeu.move("Joueur1", -20,0)

        elif Action1.keysym=="Right" and Coordonees[0]<890:
                                                                                # On associe la pression des flèches et de la touche Ctrl_R aux mouvements et au tir du joueur 1
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
                                                                                # Idem pour le joueur 2 avec les touches ZQSD et Ctrl_L
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
    global id1, DelaiTir1

    id1=ZoneJeu.after(12,MouvementTirJoueur1,"Laser1")
    CoordonneesLaser1=ZoneJeu.coords("Laser1")
    ZoneJeu.move(Projectile,0, -15)

    if CoordonneesLaser1[1]<20:

        ZoneJeu.after_cancel(id1)
        ZoneJeu.delete("Laser1")
        DelaiTir1=0

                  # Joueur 2                                                    # Les fonctions MouvementTirJoueur permettent de gérer le déplacement des projectiles des deux joueurs

def MouvementTirJoueur2(Projectile):
    global id2, DelaiTir2

    id2=ZoneJeu.after(12,MouvementTirJoueur2,"Laser2")
    CoordonneesLaser2=ZoneJeu.coords("Laser2")
    ZoneJeu.move(Projectile,0, 15)

    if CoordonneesLaser2[1]>650:

        ZoneJeu.after_cancel(id2)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0

# # # # # # # # # # # #    Collision/Degats/Vie    # # # # # # # # # # # #

def ComparaisonDegats():
    global Compa, AncienneCollision, Degats1, Degats2, BoutonRejouer, CompteurBo, Joueur1Bo3,Joueur2Bo3, BoutonRetour,Joueur1Bo5,Joueur2Bo5,ZoneJeu,BoutonFinBo3,DelaiTir1,DelaiTir2,LabelNom1,LabelNom2

    # Barre de vie du joueur 1

    CollisionsJoueur1=ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur1")[0],ZoneJeu.coords("Joueur1")[1],ZoneJeu.coords("Joueur1")[2],ZoneJeu.coords("Joueur1")[3])
    NombreCollisionJoueur1=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur1")[0],ZoneJeu.coords("Joueur1")[1],ZoneJeu.coords("Joueur1")[2],ZoneJeu.coords("Joueur1")[3])))

# La fonction ComparaisonDegats rend possible la présence et la destruction des barres de vie.
# La commande "find_overlapping" permet de détecter le passage d'un missile sur un vaisseau, et de par la suite détruire une barre de vie du vaisseau touché

    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==5:

        ZoneJeu.delete(VieJoueurUn5)
        ZoneJeu.after_cancel(id2)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==4:

        ZoneJeu.delete(VieJoueurUn4)
        ZoneJeu.after_cancel(id2)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==3:

        ZoneJeu.delete(VieJoueurUn3)                                            # Dans chacun des cas suivants, si un joueur est touché, une de ses barres de vie est enlevée et le laser est détruit
        ZoneJeu.after_cancel(id2)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==2:

        ZoneJeu.delete(VieJoueurUn2)
        ZoneJeu.after_cancel(id2)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    if NombreCollisionJoueur1 > 3 and AncienneCollision!=CollisionsJoueur1[3] and Degats1==1:

        ZoneJeu.delete(VieJoueurUn1)
        ZoneJeu.after_cancel(id2)
        ZoneJeu.delete("Laser2")
        DelaiTir2=0
        AncienneCollision=CollisionsJoueur1[3]
        Degats1=Degats1-1

    # Barre de vie du joueur 2

    CollisionsJoueur2=ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur2")[0],ZoneJeu.coords("Joueur2")[1],ZoneJeu.coords("Joueur2")[2],ZoneJeu.coords("Joueur2")[3])
    NombreCollisionJoueur2=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("Joueur2")[0],ZoneJeu.coords("Joueur2")[1],ZoneJeu.coords("Joueur2")[2],ZoneJeu.coords("Joueur2")[3])))

    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==5:

        ZoneJeu.delete(VieJoueurDeux5)
        ZoneJeu.after_cancel(id1)
        ZoneJeu.delete("Laser1")
        DelaiTir1=0
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==4:

        ZoneJeu.delete(VieJoueurDeux4)
        ZoneJeu.after_cancel(id1)
        ZoneJeu.delete("Laser1")
        DelaiTir1=0
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==3:

        ZoneJeu.delete(VieJoueurDeux3)
        ZoneJeu.after_cancel(id1)                                               # Dans chacun des cas suivants, si un joueur est touché, une de ses barres de vie est enlevée et le laser est détruit
        ZoneJeu.delete("Laser1")
        DelaiTir1=0
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==2:

        ZoneJeu.delete(VieJoueurDeux2)
        ZoneJeu.after_cancel(id1)
        ZoneJeu.delete("Laser1")
        DelaiTir1=0
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

    if NombreCollisionJoueur2 > 3 and AncienneCollision!=CollisionsJoueur2[3] and Degats2==1:

        ZoneJeu.delete(VieJoueurDeux1)
        ZoneJeu.after_cancel(id1)
        ZoneJeu.delete("Laser1")
        DelaiTir1=0
        AncienneCollision=CollisionsJoueur2[3]
        Degats2=Degats2-1

    Compa=Fenetre.after(1,ComparaisonDegats)

          # Conditions de victoire dans un match normal

                 # Le joueur 2 gagne une manche

    if Degats1==0 and CompteurBo==1:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")                                       # Cette partie de la fonction gère l'affichage des différents écrans de victoire en fonction du mode de jeu, du joueur gagnant ainsi que de la langue
            LabelNom2.destroy()
            LabelNom1.destroy()

            if Francais==1:

# Par exemple, ici l'écran affiché sera " Le joueur 2 remporte la partie ! " car nous sommes en partie rapide et en français

                ZoneJeu.create_image(640,360,image=VictoireJ2FR)
                BoutonRejouer=Button(ZoneJeu,text="Cliquez ici pour rejouer",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:

# Ici l'écran affiché sera " Player 2 wins the game ! " car nous sommes toujours en partie rapide mais en anglais cette fois

                ZoneJeu.create_image(640,360,image=VictoireJ2ENG)
                BoutonRejouer=Button(ZoneJeu,text="Play another game",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

                             # Le joueur 1 gagne une manche

    if Degats2==0 and CompteurBo==1:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")                                           # Et ainsi de suite pour tous les modes de jeu et les deux joueurs ....
            LabelNom2.destroy()
            LabelNom1.destroy()

            if Francais==1:

                ZoneJeu.create_image(640,360,image=VictoireJ1FR)
                BoutonRejouer=Button(ZoneJeu,text="Cliquez ici pour rejouer",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:

                ZoneJeu.create_image(640,360,image=VictoireJ1ENG)
                BoutonRejouer=Button(ZoneJeu,text="Play another game",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

     # Conditions de victoire dans un Bo3

         # Le joueur 2 gagne une manche

    if Degats1==0 and CompteurBo==3:

        Joueur2Bo3+=1
        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")
        LabelNom2.destroy()
        LabelNom1.destroy()

        if Joueur1Bo3<2 and Joueur2Bo3<2:

            if Francais==1:

                ZoneJeu.create_image(640,360,image=VictoireJ2FR)
                BoutonRejouer=Button(ZoneJeu,text="Lancer la prochaine manche",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                ZoneJeu.create_image(640,360,image=VictoireJ2ENG)
                BoutonRejouer=Button(ZoneJeu,text="Play the next game",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                    # Le joueur 2 gagne le Bo3

        if CompteurBo==3 and Joueur2Bo3==2:
            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")
            LabelNom2.destroy()
            LabelNom1.destroy()

            if Francais==1:

                pygame.mixer.pause()

                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo3FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 2 remporte la partie !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:

                pygame.mixer.pause()

                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo3ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 2 has won the Best of 3 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

                        # Le joueur 1 gagne la manche

    if Degats2==0 and CompteurBo==3:

        Joueur1Bo3+=1
        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")
        LabelNom2.destroy()
        LabelNom1.destroy()

        if Joueur1Bo3<2 and Joueur2Bo3<2:

            if Francais==1:

                ZoneJeu.create_image(640,360,image=VictoireJ1FR)
                BoutonRejouer=Button(ZoneJeu,text="Lancer la prochaine manche",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                ZoneJeu.create_image(640,360,image=VictoireJ1ENG)
                BoutonRejouer=Button(ZoneJeu,text="Play the next game ",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                   # Le joueur 1 remporte le Bo3

        if CompteurBo==3 and Joueur1Bo3==2:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")
            LabelNom2.destroy()
            LabelNom1.destroy()

            if Francais==1:

                pygame.mixer.pause()
                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo3FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 1 remporte la partie !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:

                pygame.mixer.pause()
                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo3ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 1 has just won the best of 3!",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

         # Conditions de victoire dans un Bo5

             # Joueur 2 gagne la manche

    if Degats1==0 and CompteurBo==5:

         Joueur2Bo5+=1
         Fenetre.after_cancel(Compa)
         ZoneJeu.delete("Joueur1")
         ZoneJeu.delete("Joueur2")
         LabelNom2.destroy()
         LabelNom1.destroy()

         if Joueur1Bo5<3 and Joueur2Bo5<3:

            if Francais==1:

                ZoneJeu.create_image(640,360,image=VictoireJ2FR)
                BoutonRejouer=Button(ZoneJeu,text="Lancer la prochaine manche",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                ZoneJeu.create_image(640,360,image=VictoireJ2ENG)
                BoutonRejouer=Button(ZoneJeu,text="Play the next game",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                         # Le joueur 2 remporte le Bo5

         if CompteurBo==5 and Joueur2Bo5==3:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")
            LabelNom2.destroy()
            LabelNom1.destroy()

            if Francais==1:

                pygame.mixer.pause()
                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo5FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 2 remporte le Bo5 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:

                pygame.mixer.pause()
                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ2Bo5ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 2 has won the best of 5 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

                       # Le joueur 1 gagne une manche

    if Degats2==0 and CompteurBo==5:

        Joueur1Bo5+=1
        Fenetre.after_cancel(Compa)
        ZoneJeu.delete("Joueur1")
        ZoneJeu.delete("Joueur2")
        LabelNom2.destroy()
        LabelNom1.destroy()

        if Joueur1Bo5<3 and Joueur2Bo5<3:

            if Francais==1:

                ZoneJeu.create_image(640,360,image=VictoireJ1FR)
                BoutonRejouer=Button(ZoneJeu,text="Cliquez ici pour rejouer",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

            if Francais==0:

                ZoneJeu.create_image(640,360,image=VictoireJ1ENG)
                BoutonRejouer=Button(ZoneJeu,text="Play the next game",height=5,width=30,command=Rejouer)
                BoutonRejouer.place(x=530,y=400)

                            # Le joueur 1 remporte le Bo5

        if CompteurBo==5 and Joueur1Bo5==3:

            Fenetre.after_cancel(Compa)
            ZoneJeu.delete("Joueur1")
            ZoneJeu.delete("Joueur2")
            LabelNom2.destroy()
            LabelNom1.destroy()

            if Francais==1:

                pygame.mixer.pause()
                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo5FR)

                BoutonFinBo3=Button(ZoneJeu,text="Le joueur 1 remporte la partie !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

            if Francais==0:

                pygame.mixer.pause()
                Victoire.play()
                ZoneJeu.create_image(640,360,image=VictoireJ1Bo5ENG)

                BoutonFinBo3=Button(ZoneJeu,text="Player 1 has won the best of 5 !",height=5,width=30,relief=SUNKEN)
                BoutonFinBo3.place(x=530,y=400)

                BoutonRetour=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=Retour)
                BoutonRetour.place(x=530,y=620)

# # # # # # # # # # # #    Menu de lancement    # # # # # # # # # # # #

# Bouton partie rapide

def Lancer():
        global CompteurBo, musiquematch,BoutonQuitter,Nom1,LabelNom1,LabelNom2,BoutonPseudo1,BoutonPseudp2,Pseudo1,Pseudo2,vaisseau2,vaisseau1
        global VieJoueurUn5, VieJoueurUn4, VieJoueurUn3, VieJoueurUn2, VieJoueurUn1,VieJoueurDeux5, VieJoueurDeux4, VieJoueurDeux3, VieJoueurDeux2, VieJoueurDeux1

        BoutonMulti.destroy()
        BoutonSolo.destroy()
        BoutonTuto.destroy()
        BoutonTraductionAnglais.destroy()                                       # La fonction Lancer est utilisée pour lancer n'importe quel mode de jeu
        BoutonBo3.destroy()
        BoutonBo5.destroy()
        BoutonPseudo1.destroy()
        BoutonPseudo2.destroy()                                                 # Elle détruit d'abord tous les boutons du menu principal ainsi que le fond d'écran
        Pseudo1.destroy()
        Pseudo2.destroy()

        ZoneJeu.delete("all")
        ZoneJeu.create_image(640,360,image=FondEcran)                           # On crée ensuite le nouveau fond d'écran

# Les lignes oranges crées juste en dessous correspondent à la " hitbox " des vaisseaux : nous ne pouvons pas détecter la collision d'une image et d'un laser (une forme géométrique)
# car ils sont respectivement crées avec 2 et 4 coordonnées. Pour palier à ce problème, on place des rectangles sous l'image des vaisseaux, et on détecte les collisions entre les lasers et les rectangles

        ZoneJeu.create_line(450, 611, 500, 611, width= 20, fill="orange", tag="Joueur1")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)
        ZoneJeu.create_line(460, 100, 490, 100, width= 20, fill="orange", tag="Joueur2")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)

        ZoneJeu.create_image(475,120,image=vaisseau2,tag="VaisseauJoueur2")
        ZoneJeu.create_image(475,600,image=vaisseau1,tag="VaisseauJoueur1")     # On crée les images de vaisseaux par dessus les rectangles

        LabelNom1=Label(ZoneJeu, text=Nom1, height=2, width=12, bg="black", fg="blue", font=("Courrier", 26))
        LabelNom1.place(x=980,y=600)
                                                                                # Les LabelNom permettent d'afficher les pseudos des deux joueurs
        LabelNom2=Label(ZoneJeu, text=Nom2, height=2, width=12, bg="black", fg="red", font=("Courrier", 26))
        LabelNom2.place(x=980,y=10)

        VieJoueurUn1= ZoneJeu.create_rectangle (1015+(30*1),550,1035+(30*1),587, fill="blue")
        VieJoueurUn2= ZoneJeu.create_rectangle (1007+(30*2),550,1027+(30*2),587, fill="blue")
        VieJoueurUn3= ZoneJeu.create_rectangle (999+(30*3),550,1019+(30*3),587, fill="blue")           # Les variables VieJoueur correspondent aux rectangles qui représentent les barres de vie des joueurs
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
            pygame.mixer.pause()                                                # On permet à la musique de rester active jusqu'à ce qu'on revienne au menu principal tout en lançant la musique de jeu
            Musiquejeu.play()
            musiquematch=1

# Bouton traduction anglais

def TraductionAnglais():
    global Francais,Nom1,Nom2,VariablePseudo1,VariablePseudo2

    Francais=0

    BoutonMulti.config(text="Multiplayer : Quick game")
    BoutonSolo.config(text="Training")
    BoutonTuto.config(text="Tutorial")
    BoutonTraductionAnglais.config(text="Passer le jeu en français",command=TraductionFrancais)    # La fonction TraductionAnglais permet de passer le texte des boutons ainsi que les pseudos par défaut en Anglais
    BoutonBo3.config(text="Best of 3")
    BoutonBo5.config(text="Best of 5")
    BoutonPseudo1.config(text="Player 1's pseudo")
    BoutonPseudo2.config(text="Player 2's pseudo")

    if VariablePseudo1==0:
        Nom1="Player 1"
    if VariablePseudo2==0:
        Nom2="Player 2"                                                         # Si nous sommes en anglais, les pseudos par défaut sont Player 1 et Player 2

# Bouton traduction français

def TraductionFrancais():
    global Francais,BoutonPseudo1,BoutonPseudo2,Nom1,Nom2,VariablePseudo1,VariablePseudo2

    Francais=1

    BoutonMulti.config(text="Multijoueur : Partie rapide")
    BoutonSolo.config(text="Mode entraînement")
    BoutonTuto.config(text="Tutoriel")
    BoutonTraductionAnglais.config(text="Switch to the english version",command=TraductionAnglais) # Le bouton de traduction est en anglais de base car un joueur anglais ne saurait pas comment traduire le jeu sinon !
    BoutonBo3.config(text="Match en trois manches")
    BoutonBo5.config(text="Match en cinq manches")                              # La fonction TraductionAnglais permet de passer le texte des boutons ainsi que les pseudos par défaut en Français
    BoutonPseudo1.config(text="Valider pseudo joueur 1")
    BoutonPseudo2.config(text="Valider pseudo joueur 2")

    if VariablePseudo1==0:
        Nom1="Joueur 1"
    if VariablePseudo2==0:                                                        # Si nous sommes en Français, les pseudos par défaut sont Joueur 1 et Joueur 2
        Nom2="Joueur 2"

# Bouton tutoriel

def Tuto():
    global CompteurBo,BoutonPseudo1,BoutonPseudo2,Pseudo1,Pseudo2

    BoutonMulti.destroy()
    BoutonSolo.destroy()
    BoutonTraductionAnglais.destroy()
    BoutonBo3.destroy()
    BoutonBo5.destroy()
    BoutonPseudo1.destroy()                                                     # La fonction Tuto permet de lancer le tutoriel, en détruisant les boutons du menu et en créant le fond d'écran du tutoriel
    BoutonPseudo2.destroy()
    Pseudo1.destroy()
    Pseudo2.destroy()
    CompteurBo=666

    if Francais==1:

     ZoneJeu.create_image(640,360,image=FondTutoFR)
     BoutonTuto.config(text="Revenir au menu principal", command=Retour)
     BoutonTuto.place(x=120,y=620)

    if Francais==0:

     ZoneJeu.create_image(640,360,image=FondTutoENG)
     BoutonTuto.config(text="Go back to main menu", command=Retour)
     BoutonTuto.place(x=120,y=620)

# Bouton rejouer partie normale

def Rejouer():
    global BoutonRejouer, AncienneCollision, Degats1, Degats2,BoutonRetour,CompteurBo

    BoutonRejouer.destroy()

    if CompteurBo==1:

        BoutonRetour.destroy()                                                  # La fonction Rejouer permet simplement de relancer une partie en détruisant l'écran de fin de partie puis en réinitialisant les conditions du match

    ZoneJeu.delete("all")
    AncienneCollision=0
    Degats1=5
    Degats2=5
    Lancer()

# Bouton retour

def Retour():
    global ZoneJeu,BoutonRejouer,BoutonRetour,Degats1,Degats2,CompteurBo,BoutonFinBo3,Joueur1Bo3,Joueur1Bo5,Joueur2Bo3,Joueur2Bo5,musiquematch

    pygame.mixer.pause()
    musiquematch=0

    if CompteurBo==3 or CompteurBo==5:

        BoutonFinBo3.destroy()
        BoutonRetour.destroy()

    if CompteurBo==1:

        BoutonRejouer.destroy()     # La fonction retour permet de revenir au menu principal. En fonction du mode de jeu, elle détruit les boutons présents
        BoutonRetour.destroy()

    if CompteurBo==666:

        CompteurBo=0
        BoutonTuto.destroy()

    ZoneJeu.delete("all")
    Degats2=5
    Degats1=5                    # Elle réinitialise ensuite toutes les variables, efface tous les Labels, images ... puis utilise la fonction Menu afin de récreer ce dernier
    AncienneCollision=0
    Joueur1Bo3=0
    Joueur2Bo3=0
    Joueur1Bo5=0
    Joueur2Bo5=0
    CompteurBo=0

    ZoneJeu.create_image(640,360,image=FondMenu)
    ZoneJeu.pack()
    Menu()

# Fonction pour lancer le Bo3

def LancerBo3():
    global CompteurBo   # La fonction LancerBo3 fixe la valeur de CompteurBo à 3 afin de passer dans la configuration de Bo3, puis lance simplement une partie grâce à la fonction Lancer

    Comparaison=0
    CompteurBo=3
    Lancer()

# Fonction pour lancer le Bo5

def LancerBo5():
    global CompteurBo

    Comparaison=0       # Idem pour la fonction LancerBo5 pour lancer le Bo5
    CompteurBo=5
    Lancer()

def LancerBo1():
    global CompteurBo   # Idem pour la fonction LancerBo1 pour lancer une partie rapide

    CompteurBo=1
    Comparaison=0
    Lancer()

# Fonction pour créer le fond d'écran du menu

def Creationzonejeu():
    global ZoneJeu

    ZoneJeu.create_image(640,360,image=FondMenu) # Cette fonction sert simplement à créer le fond d'écran du menu
    ZoneJeu.pack()

# Fonction qui lance le mode entraînement

def Lancersolo():
        global Comparaison,Labelscore,BoutonRetourSolo,Score,AffichageScore,ScoreSolo,ScoreAff,Pseudo1,Pseudo2,BoutonPseudo1,BoutonPseudo2,CompteurBo

        pygame.mixer.pause()
        Musiquejeu.play()

# La fonction Lancersolo a le même rôle que la fonction lancer mais elle est adaptée au mode entraînement : un seul vaisseau peut être contrôlé par le joueur

        Comparaison=1
        CompteurBo=2

        BoutonMulti.destroy()
        BoutonSolo.destroy()
        BoutonTuto.destroy()
        BoutonTraductionAnglais.destroy()
        BoutonBo3.destroy()
        BoutonBo5.destroy()                  # La fonction détruit d'abord tous les boutons du menu, et crée un nouveau fond d'écran ainsi que les labels pour afficher le score
        Pseudo1.destroy()
        Pseudo2.destroy()
        BoutonPseudo1.destroy()
        BoutonPseudo2.destroy()

        ZoneJeu.delete("all")
        ZoneJeu.create_image(640,360,image=FondEcran)
        ZoneJeu.create_line(450, 611, 500, 611, width= 20, fill="orange", tag="Joueur1")
        ZoneJeu.bind_all("<Key>", MouvementJoueur)
        ZoneJeu.create_image(475,600,image=vaisseau1,tag="VaisseauJoueur1")

        ScoreAff=Label(ZoneJeu, text="Score:", height=5, width=5, bg="black", fg="blue", font=("Courrier", 50))
        ScoreAff.place(x=1000, y=50)
        Score=Label(ZoneJeu, text=ScoreSolo, height=2, width=2, bg="black", fg="blue", font=("Courrier", 84))
        Score.place(x=1025, y=300)

        if Francais==1:

            BoutonRetourSolo=Button(ZoneJeu,text="Retour au menu principal",width=30,height=5,command=RetourSolo)
            BoutonRetourSolo.place(x=1000,y=620)

        if Francais==0:

            BoutonRetourSolo=Button(ZoneJeu,text="Go back to main menu",width=30,height=5,command=RetourSolo)
            BoutonRetourSolo.place(x=1000,y=620)

        ZoneJeu.pack()

        CreationVaisseauSolo()                                         # Elle fait ensuite appel à la fonction CreationVaisseauSolo qui permet de créer le premier vaisseau
        CompaSolo()                                                    # Puis elle utilise la fonction CompaSolo, qui comme la fonction Comparaison dégât, permet de détecter les collisions entre le laser et le vaisseau ennemi

# Fonction permettant le retour au menu depuis le mode entraînement

def RetourSolo():

        global ZoneJeu,ComparaisonSolo,ScoreSolo,musiquematch,Musiquefond,Comparaison,Score,ScoreAff,CompteurBo

        ZoneJeu.after_cancel(ComparaisonSolo)
        ScoreSolo=0
        Comparaison=0
        Score.destroy()
        ScoreAff.destroy()
        BoutonRetourSolo.destroy()  # Comme la fonction Retour, la fonction RetourSolo permet de revenir au menu principal en réinitialisant toutes les variables utilisées, les scores, en détruisant les labels et boutons ...
        CompteurBo=0

        ZoneJeu.delete("all")

        Creationzonejeu()
        Menu()                      # Puis elle recrée le menu grâce à la fonction Menu
        musiquematch=0
        pygame.mixer.pause()
        Musiquefond.play()

# Fonction qui crée les vaisseaux IA

def CreationVaisseauSolo():
    global VaisseauIA

    x1=randint(100,800)                                                         # La fonction CreationVaisseauSolo permet de créer un vaisseau à partir de coordonnées aléatoire à l'aide de la commande randint
    ZoneJeu.create_line(x1,100,x1+30,100,fill="orange",width=20,tag="VaisseauSolo")
    ZoneJeu.create_image(x1+15,120,image=vaisseau3,tag="VaisseauJoueur3")
    ZoneJeu.pack()

# Fonction de comparaison des dégats subis par les vaisseaux IA

def CompaSolo():
    global ComparaisonSolo,ScoreSolo,Score

    ComparaisonSolo=ZoneJeu.after(1,CompaSolo) # la fonction CompaSolo détecte les collisions entre le laser et le vaisseau ennemi en utilisant la fonction " find over_lapping"

    NombreCollisionSolo=(len(ZoneJeu.find_overlapping(ZoneJeu.coords("VaisseauSolo")[0],ZoneJeu.coords("VaisseauSolo")[1],ZoneJeu.coords("VaisseauSolo")[2],ZoneJeu.coords("VaisseauSolo")[3])))

    if NombreCollisionSolo!=3:

        ScoreSolo+=1
        Score.config(text=ScoreSolo)  # Lorsque le laser atteint le vaisseau, le score est actualisé, le vaisseau est détruit et le un autre est recréé

        ZoneJeu.delete("VaisseauSolo")
        ZoneJeu.delete("VaisseauJoueur3")

        ZoneJeu.after_cancel(ComparaisonSolo) # A chaque fois qu'un vaisseau est détruit, l'after permettant la détection des collisions est arrêté puis relancé à la création du vaisseau suivant afin d'éviter des problèmes de fermeture de fenêtre
        CreationVaisseauSolo()
        ComparaisonSolo=ZoneJeu.after(1,CompaSolo)

# Fonction menu principal

def Menu():
    global BoutonMulti, BoutonSolo, BoutonTuto, BoutonTraductionAnglais, BoutonBo3, BoutonBo5, ZoneJeu,BoutonPantheon, Francais,Comparaison,BoutonQuitter,Fenetre,Pseudo1,Pseudo2,BoutonPseudo1,BoutonPseudo2

    Comparaison=0

    BoutonMulti=Button(ZoneJeu,text="Multijoueur : Partie rapide",command=LancerBo1,height=5,width=30)
    BoutonMulti.place(x=80,y=420)

    BoutonSolo=Button(ZoneJeu,text="Mode entraînement",command=Lancersolo,height=5,width=30)
    BoutonSolo.place(x=1000,y=420)

    BoutonTuto=Button(ZoneJeu,text="Tutoriel",height=5,width=30,command=Tuto)  # La fonction Menu sert  à créer les boutons permettant de lancer les différents modes de jeu, de placer le fond d'écran et de lancer la musique principale
    BoutonTuto.place(x=1000,y=520)

    BoutonTraductionAnglais=Button(ZoneJeu, text=" Passer le jeu en anglais",command=TraductionAnglais,height=5,width=30)
    BoutonTraductionAnglais.place(x=1000,y=620)

    BoutonBo3=Button(ZoneJeu,text="Match en trois manches",command=LancerBo3,height=5,width=30)
    BoutonBo3.place(x=80,y=520)

    BoutonBo5=Button(ZoneJeu,text="Match en cinq manches",command=LancerBo5,height=5,width=30)
    BoutonBo5.place(x=80,y=620)

    Pseudo1=Entry(ZoneJeu,width=21)
    Pseudo1.place(x=400,y=630)
    BoutonPseudo1=Button(ZoneJeu,text="Valider pseudo joueur 1",width=17,height=3,command=Getpseudo1)
    BoutonPseudo1.place(x=400,y=650)
                                      # Elle sert également à créer les Entry où les joueurs pourront rentrer leurs pseudos
    Pseudo2=Entry(ZoneJeu,width=21)
    Pseudo2.place(x=800,y=630)
    BoutonPseudo2=Button(ZoneJeu,text="Valider pseudo joueur 2",width=17,height=3,command=Getpseudo2)
    BoutonPseudo2.place(x=800,y=650)

    if Francais==0:
        TraductionAnglais()  # Lorsque le jeu est dans sa configuration anglaise (Français==0),le menu se recrée directement en anglais

    if Francais==1:
        TraductionFrancais() # De même pour le français lorsque Français==1

    Musiquefond.play()

# Fonction reliée à la fermeture de la fenêtre

def FermetureFenetre():
    global ComparaisonSolo,Compa

# En associant Tkinter pour les graphismes à pygame pour la musique, nous rencontrons un problème : lors de la fermeture du programme ( par la croix windows); la musique ne s'arrête pas !
# Pour résoudre ce problème, on crée une fonction qui, associée à la croix Windows, ferme le programme tout en arrêtant le mixer pygame

    if  CompteurBo==3 or CompteurBo==5:
        ZoneJeu.after_cancel(Compa)      # En fonction du mode de jeu, la fonction arrête également l'after en cours afin d'éviter tout problème lié à la fermeture de la fenêtre
                                         # Par exemple, des erreurs qui défileraient à l'infini ou l'obligation de cliquer deux fois sur la croix pour fermer le programme
    if CompteurBo==2:
        ZoneJeu.after_cancel(ComparaisonSolo)

    pygame.mixer.pause()
    Fenetre.destroy()

Fenetre.protocol('WM_DELETE_WINDOW', FermetureFenetre) # La commande .protocol permet d'associer une fonction à un "outil" externe au programme, par exemple ici la croix windows

def Getpseudo1():
    global Nom1,Pseudo1,VariablePseudo1

    Nom1=Pseudo1.get()  # Les fonctions Getpseudo permettent de récupérer la chaîne de caractère inscrite dans les Entry correspondant aux pseudos rentrés par les joueurs et les associent à des variables Nom1 et Nom2
    for i in range(len(Nom1)): # Cette boucle for permet d'effacer le pseudo entré quand on clique sur le bouton valider
        Pseudo1.delete(0,None)
    VariablePseudo1=1

def Getpseudo2():
    global Nom2,Pseudo2,VariablePseudo2

    Nom2=Pseudo2.get()
    for i in range(len(Nom2)):
        Pseudo2.delete(0,None)
    VariablePseudo2=1

Creationzonejeu()
Menu()                       # Quand le programme se lance, il crée d'abord le fond d'écran du menu, puis utilise la fonction Menu afin de créer tous les boutons nécessaires au jeu

Fenetre.mainloop()   # Et enfin, la commande indispensable .mainloop permet de faire afficher "en boucle" la fenêtre Tkinter