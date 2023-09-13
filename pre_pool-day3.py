# -*- coding: utf-8 -*-
#Created by Willipatafoul at 09:34 on 13/09/2023
#

# ---------- Strings Task 00 ---------- #

chaine = "La machine à café"
print(chaine)

# ---------- Strings Task 01 ---------- #

chaine = "BONJOUR"
print(chaine[0], chaine[4])

# ---------- Strings Task 02 ---------- #

chaine = "Rends pas fou les chaines de caractères c'est facilE"
print(chaine[-1])

# ---------- Strings Task 03 ---------- #

chaine = "OrDiNaTeuR"
print(chaine[4:9])

# ---------- String Methods Task 00 ---------- #

chaine = "OrDiNaTeuR"
print(chaine.lower())

# ---------- String Methods Task 01 ---------- #

chaine = "tutu on the tuki-kata"
print(chaine.replace("tu","ta"))

# ---------- String Methods Task 02 ---------- #

string = "hello world" #Application de la chaine de caractère "hello world" à la variable "string"
position = string.find("a") #Recherche et application du caractère 'a' à la variable "position"
print(position) #Affichage de la variable position, ici affichage de "-1" car il n'y a pas de 'a' dans la chaine

# ---------- String Methods Task 03 ---------- #

p = "abcdefghij"
print(p[::-2][:5][::-1][3:])

#Etape 1 : [::-2] -> jhfdb
#Etape 2 : [:5] -> jhfdb
#Etape 3 : [::-1] -> bdfhj
#Etape 4 : [3:] -> hj

# ---------- String Methods Task 04 ---------- #

p = "abcdefghij"
print(p[::-2][::-1][3:]) #On supprime le [:5] qui est inutile

# ---------- String Methods Task 05 ---------- #
chaine = "Raton laveur"

for i in range(10):
    print(chaine)
    
# ---------- String Methods Task 06 ---------- #

print("Raton laveur\n" * 10)

# ---------- String Methods Task 07 ---------- #

s1 = "Hello"
s2 = str(42) #Ajout de str() pour passer '42' d'entier en string
concat = s1 + s2 
print(concat)

# ---------- String Methods Task 08 ---------- #

string1 = "42"
string2 = "is"
string3 = "the answer"
concat = string1 + " " + string2 + " " + string3
size = len(concat)
print(f"The string", concat, "contains", size, "characters).")