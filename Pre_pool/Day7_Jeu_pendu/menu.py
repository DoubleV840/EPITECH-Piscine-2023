# -*- coding: utf-8 -*-
#Created by Willipatafoul at 09:54 on 19/09/2023
#
import time

def menu_principal():
    print("\n_-_-_-_- JEU DU PENDU -_-_-_-_\n")
    time.sleep(0.2)
    print("1. Jouer contre l'ordinateur")
    time.sleep(0.2)
    print("2. Jouer contre un humain")
    time.sleep(0.2)
    print("3. Quitter le jeu\n")
    time.sleep(0.2)
    choix_menu = input("Votre choix : ")
    return choix_menu