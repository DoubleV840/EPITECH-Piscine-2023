# # -*- coding: utf-8 -*-
# #Created by Willipatafoul at 09:44 on 18/09/2023
# #

# # ---------- Basic functions Task 00 ---------- #

# def f(x): #Dénifition de la fonction f avec en paramètre x
#     return 2 * x + 1 #Return du calcul en fonction de la valeur de x
# def g(): #Dénifition de la fonction g
#     return 7 #Return du chiffre 7

# y = f(2) #Appel de la fonction f en donnant la valeur 2 à x
# print(y) #Print de y
# y = f(5) + g() #Appel de la fonction f (en donnant la valeur 5 à x) et g
# print(y) #Print de y

# # ---------- Basic functions Task 01 ---------- #

# def bread(): 
#     print("<//////////>")
# def lettuce(): 
#     print("~~~~~~~~~~~~")
# def tomato():
#     print("O O O O O O")
# def ham(): 
#     print("============")
    
# bread()
# lettuce()
# ham()
# tomato()
# ham()
# bread()

# # ---------- Basic functions Task 02 ---------- #

# def bread(): 
#     print("<//////////>")
# def lettuce(): 
#     print("~~~~~~~~~~~~")
# def tomato():
#     print("O O O O O O")
# def ham(): 
#     print("============")
    
# for i in range(42):
#     bread()
#     lettuce()
#     ham()
#     tomato()
#     ham()
#     bread()
#     print(i+1)

# # ---------- Basic functions Task 03 ---------- #

# def bread(): 
#     print("<//////////>")
# def lettuce(): 
#     print("~~~~~~~~~~~~")
# def tomato():
#     print("O O O O O O")
# def ham(): 
#     print("============")

# nb = int(input("Combien de hamburger voulez-vous manger ? "))
# if nb >= 0:
#     for i in range(nb):
#         bread()
#         lettuce()
#         ham()
#         tomato()
#         ham()
#         bread()
#         print(i+1)
# else:
#     print("I can't do this")

# # ---------- Basic functions Task 04 ---------- #

# def bread(): 
#     print("<//////////>")
# def lettuce(): 
#     print("~~~~~~~~~~~~")
# def tomato():
#     print("O O O O O O")
# def ham(): 
#     print("============")

# nb = int(input("Combien de hamburger voulez-vous manger ? "))
# which = input("Quel type de hamburger voulez-vous manger ? (Végé: v, Normal: n) ")
# if nb >= 0:
#     if which == "v":    
#         for i in range(nb):
#             bread()
#             lettuce()
#             tomato()
#             lettuce()
#             bread()
#             print(i+1)
#     else:
#         for i in range(nb):
#             bread()
#             lettuce()
#             ham()
#             tomato()
#             ham()
#             bread()
#             print(i+1)
# else:
#     print("I can't do this")
    
# # ---------- Challenge ---------- #

# nb = int(input("Entrez un nombre : "))
# power = int(input("Entrez une puissance : "))

# print(nb ** power)

# # ---------- Recursion Task 01 ---------- #

# def is_palindrome(s):
#     s = ''.join(filter(str.isalnum, s)).lower()

#     if len(s) <= 1:
#         return True

#     if s[0] == s[-1]:
#         return is_palindrome(s[1:-1])
#     else:
#         return False

# print(is_palindrome("kayak")) 
# print(is_palindrome("never odd or even"))  
# print(is_palindrome("Was it a car or a cat I saw?"))  
# print(is_palindrome("hello"))

# # ---------- Recursion Task 02 ---------- #
# import os

# chemin = '/Users/william/Desktop/Programmation/EPITECH/EPITECH Piscine 2023'

# fichiers = os.listdir(chemin)
# chemin_fichiers = os.path.abspath(chemin)
# for item in fichiers:
#     print(chemin_fichiers)
#     print(item)
#     print()
    
# # ---------- Higher-order functions Task 00 ---------- #


# # funA checks if s contains at least n lowercase letters; 
# # funB checks if s contains at least n uppercase letters; 
# # funC checks if s contains at least n characters;
# # funD checks if s contains at least n special characters;
# # funE checks if s contains at least n numbers.

# mot = input("Entrez un mot: ")
# def funA():
    
#     count = 0

#     for char in mot:
#         if char.islower():
#             count += 1

#     if count >= 1:
#         print(f"funA checked and the string '{mot}' contains at least {count} lowercase letters.")
#     else:
#         print("funA checked and there is no lowercase letters.")
        
# def funB():
    
#     count = 0

#     for char in mot:
#         if char.isupper():
#             count += 1

#     if count >= 1:
#         print(f"funB checked and the string '{mot}' contains at least {count} uppercase letters.")
#     else:
#         print("funB checked and there is no uppercase letters.")

# def funC():
    
#     count = len(mot)

#     if count >= 1:
#         print(f"funC checked and the string '{mot}' contains at least {count} characters.")
#     else:
#         print("funB checked and there is no characaters.")
        
# def funD():
    
#     count = 0

#     for char in mot:
#         if char.isalpha() == False and char.isalnum() == False:
#             count += 1

#     if count >= 1:
#         print(f"funD checked and the string '{mot}' contains at least {count} special characters.")
#     else:
#         print("funD checked and there is no special characters.")

# def funE():
    
#     count = 0

#     for char in mot:
#         if char.isdigit():
#             count += 1

#     if count >= 1:
#         print(f"funE checked and the string '{mot}' contains at least {count} numbers.")
#     else:
#         print("funE checked and there is no numbers.")
# funA()
# funB()
# funC()
# funD()
# funE()

# ---------- Higher-order functions Task 01 ---------- #

secret_password = input("Entrez le mot de passe original (doit contenir au minimum 4 lettres minuscules et 2 caractères spéciaux) : ")
new_secret_password = input("Entrez le mot de passe à vérifier (doit contenir au minimum 4 lettres minuscules et 2 caractères spéciaux): ")

def check_password(char, nb_char, new_secret_password):
    count = 0
    for lettres_min in new_secret_password:
        if char(lettres_min):
            count += 1
    if count >= nb_char:
        return True
    
def lower(char):
    return char.islower()

def special(char):
    special_characters = "!@#$%^&*()_+{}[]:;<>,.?~/\\|"
    return char in special_characters

if new_secret_password == secret_password and check_password(lower, 4, new_secret_password) and check_password(special, 2, new_secret_password):
    print("Mot de passe valide")
else:
    print("Mot de passe invalide")
