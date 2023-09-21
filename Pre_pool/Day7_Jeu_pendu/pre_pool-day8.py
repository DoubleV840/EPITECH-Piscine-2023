# # -*- coding: utf-8 -*-
# #Created by Willipatafoul at 11:02 on 20/09/2023
# #

# # ---------- matplotlib and numpy Task 01 ---------- #

# import numpy as np
# x_min = 10
# x_max = 20
# x_values = np.linspace(x_min, x_max, 100)
# print(x_values)

# # ---------- matplotlib and numpy Task 02 ---------- #

# #(0; 12), (1; 32), (2; 42) and (3; 52)

# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot([0, 1, 2, 3], [12, 32, 42, 52], 'r.:')
# plt.show()

# # ---------- matplotlib and numpy Task 03 ---------- #

# import numpy as np
# import matplotlib.pyplot as plt

# liste_abssisses = []
# liste_ordonnees = []
# i = 1
# for i in range(4):
#     abssisses = float(input(f"Entrez le point {i+1} en abssisses : "))
#     liste_abssisses.append(abssisses)
# for i in range(4):
#     ordonnees = float(input(f"Entrez le point {i+1} en ordonnees : "))
#     liste_ordonnees.append(ordonnees)

# plt.plot(liste_abssisses, liste_ordonnees, 'r.:')
# plt.show()

# # ---------- matplotlib and numpy Task 04 ---------- #

# import numpy as np
# import matplotlib.pyplot as plt
# import math

# def plot_fct(func, x_min, x_max):
#     x = np.linspace(x_min, x_max, 1000) 
#     y = func(x)
#     plt.plot(x, y)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Function Plot')
#     plt.grid(True)
#     plt.show()

# def f(x):
#     return x**2 + x*3 + 2

# plot_fct(math.sin, 0, 50) 
# plot_fct(f, -100, 200) 
# plot_fct(lambda x: x**2, -10, 10) 
# plot_fct(lambda x: 1/x, -100, 100)

# ---------- Tkinter ---------- #

import tkinter as tk
from tkinter import *
def pendu():
        
    window = tk.Tk() #Initialisation de la fenêtre

    window.title("Ma fenetreeeeeeeeeeeeeeeeeeeee") #Défini le titre de la fenetre

    #window.minsize(640, 480) #Défini la taille min et max de la fenetre 
    #window.maxsize(1280, 720)

    #window.resizable(width=False, height=True) #Autoriser la modification ou non de la taille de la fenetre
    #window.positionfrom("user") #Affichage de la fenetre dans la position de base

    #window.geometry("800x600") #Définir la taille de la fenetre
    #window.geometry("800x600+10+10") #Définir la position exacte de la fenetre dans l'ecran

    #Centrer la fenetre
    screen_X = int(window.winfo_screenwidth())
    screen_Y = int(window.winfo_screenheight())
    window_X = 800
    window_Y = 600

    position_X = (screen_X // 2) - (window_X // 2) #(largeur_ecran // 2) - (largeur_fenetre // 2)
    position_Y = (screen_Y // 2) - (window_Y // 2) #(hauteur_ecran // 2) - (hauteur_fenetre // 2)

    geo = "{}x{}+{}+{}".format(window_X, window_Y, position_X, position_Y) #Définir la position exacte de la fenetre dans l'ecran
    window.geometry(geo)

    canvas = Canvas(window, width=300, height=400, bg="white")
    canvas.pack()
    # dessine deux lignes du point 10,10 au point 40,100
    # de couleur bleue, d'épaisseur 2
    canvas.create_line(150, 125, 150, 250, fill = "blue", width = 3) #Corps
    canvas.create_line(150, 250, 100, 300, fill = "blue", width = 3) #Jambe gauche
    canvas.create_line(150, 250, 200, 300, fill = "blue", width = 3) #jJambe droite
    canvas.create_line(100, 175, 150, 150, fill = "blue", width = 3) #Bras gauche
    canvas.create_line(150, 150, 200, 175, fill = "blue", width = 3) #Bras droit
    canvas.create_line(150, 40, 150, 75, fill = "black", width = 5) #Corde cou
    canvas.create_line(50, 40, 160, 40, fill = "black", width = 8) #Bois vers corde cou
    canvas.create_line(50, 35, 50, 350, fill = "black", width = 8) #Bois long support
    canvas.create_line(50, 347, 120, 310, fill = "black", width = 8) #Bois petit support droit
    canvas.create_line(50, 347, 120, 390, fill = "black", width = 8) #Bois petit support droit

    canvas.create_line (140,115, 150,100, 160,115, smooth=1, fill = "blue", width = 2) #Bouche

    def dessiner_points():
        rayon = 2  # Définissez la taille du rayon du cercle
        x, y = 140, 95  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="blue", width=3) #Oeil gauche
        
        rayon = 2  # Définissez la taille du rayon du cercle
        x, y = 160, 95  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="blue", width=3) #Oeil droit
        
        #Noeuds corde cou
        rayon = 4  # Définissez la taille du rayon du cercle
        x, y = 150, 55  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=3)
        
        rayon = 4  # Définissez la taille du rayon du cercle
        x, y = 150, 60  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=3)
        
        rayon = 4  # Définissez la taille du rayon du cercle
        x, y = 150, 65  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=3)
        
        rayon = 4  # Définissez la taille du rayon du cercle
        x, y = 150, 70  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=3)
    
    dessiner_points()

    #Tête
    def dessiner_cercle():
        rayon = 25  # Définissez la taille du rayon du cercle
        x, y = 150, 100  # Coordonnées du centre du cercle
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="blue", width=3)
    dessiner_cercle()
pendu()
tk.mainloop() #Affichage constant de la fenêtre

