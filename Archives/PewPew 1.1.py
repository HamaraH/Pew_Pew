from tkinter import *

# Fenetre

Fenetre= Tk()
Fenetre.title("Pew Pew")
Fenetre.geometry("1920x1080")

# Zone de jeu

ZoneJeu=Canvas(Fenetre, bg="black")
ZoneJeu.pack(fill=BOTH, expand=1)
ZoneJeu.create_rectangle(0, 800, 800, 0, fill="black", width=10, outline="white", tag="border")

# Fonctions principales

def Mouvement(Action):
    global ZoneJeu
    Coordonees=ZoneJeu.coords("Joueur")
    if Action.keysym=="Left" and Coordonees[0]>20:
        ZoneJeu.move("Joueur", -20,0)
    elif Action.keysym=="Right" and Coordonees[2]<780:
        ZoneJeu.move("Joueur", 20, 0)
    elif Action.keysym=="Up" and Coordonees[1]>650:
        ZoneJeu.move("Joueur", 0, -20)
    elif Action.keysym=="Down" and Coordonees[3]<740:
        ZoneJeu.move("Joueur", 0, 20)

# Vaisseau du joueur

ZoneJeu.create_line(380, 750, 380, 700, width= 20, fill="orange",tag="Joueur")
ZoneJeu.bind_all("<Key>", Mouvement)



Fenetre.mainloop()