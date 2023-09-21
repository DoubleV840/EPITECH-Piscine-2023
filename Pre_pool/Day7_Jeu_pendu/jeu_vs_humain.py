# -*- coding: utf-8 -*-
#Created by Willipatafoul at 09:59 on 19/09/2023
#
import time

def choisir_mot():
    mot_choisi = input("Player 1 choose a word : ")
    for i in range(101):
        print(f"Chargement {i}%")
        time.sleep(0.05)
    time.sleep(2)
    print("Let's go to play the game is ready !")
    print()
    return mot_choisi

def afficher_mot_cache(mot, lettres_devinees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            mot_cache += lettre
        else:
            mot_cache += "_ "
    return mot_cache

def vs_humain():
    mot_a_deviner = choisir_mot()
    tentatives_restantes = 6  # Le joueur a 6 chances
    lettres_devinees = []
    
    while tentatives_restantes > 0:
        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_devinees)
        print(mot_cache)
        lettre = input("Guess a letter : ").lower()
        
        if len(lettre) == 1 and lettre.isalpha():
            if lettre in lettres_devinees:
                print("Already guessed !")
            elif lettre in mot_a_deviner:
                lettres_devinees.append(lettre)
                print(f"'{lettre}' found !")
            else:
                lettres_devinees.append(lettre)
                tentatives_restantes -= 1
                print("Wrong guess. You have", tentatives_restantes, "try.")
        else:
            print("Enter a valid letter.")
        
    
        if "_" not in afficher_mot_cache(mot_a_deviner, lettres_devinees):
            print()
            print("Congratulations ! You have guessed the word :", mot_a_deviner)
            time.sleep(2)
            break
    
    if tentatives_restantes == 0:
        print("LOST ! The word to guess was :", mot_a_deviner)