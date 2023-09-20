# -*- coding: utf-8 -*-
#Created by Willipatafoul at 09:56 on 19/09/2023
#
import random

def vs_ordinateur():
    liste_mots = ["Tuesdayaa"]
    mot_choisi = random.choice(liste_mots).upper()
    
    taille_mot_choisi = int(len(mot_choisi))
    
    mot_de_stockage = []
    
    count = 0
    
    for i in range(taille_mot_choisi):
        print("_ ", end='')
        
    while True:        
        count_lettres_trouvees = 0
        
        if count <= 1:
            print("/", count, "point")
        else:
            print("/", count, "points")
        print()

        choix = input("Choisissez une lettre ou un mot : ").upper()
          
        if i == choix:
            count_lettres_trouvees += 1
            count += 1
        print(f"Found {count_lettres_trouvees} '{choix}'")
        
        for i in mot_choisi:
            if i == choix:
                mot_de_stockage.append(choix)
                print(mot_de_stockage)
        for i in range(taille_mot_choisi) and mot_choisi:
            if i == choix:
                print(choix,"", end='')
            else:
                print("_ ", end='')
                