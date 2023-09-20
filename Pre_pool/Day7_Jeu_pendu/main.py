# -*- coding: utf-8 -*-
#Created by Willipatafoul at 09:34 on 19/09/2023
#
import random
import time
from menu import menu_principal
from jeu_vs_ordi import vs_ordinateur
from jeu_vs_humain import vs_humain

def main():
    
    while True:
        choix = menu_principal()
        
        if choix == "1":
            vs_ordinateur()
        elif choix == "2":
            vs_humain()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Erreur veuillez entrer une valeur correcte !")
            time.sleep(1)

if __name__ == '__main__':
    
    main()