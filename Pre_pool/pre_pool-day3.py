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
print(f"The string" + " \"" + concat + "\" " + "contains", size, "characters).")

# ---------- CHALLENGE ---------- #

liste = ["Cat","Garden","Mice"]
chaine = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()

for i in chaine:
    nb1 = chaine.count(i.lower())
for i in chaine:
    nb2 = chaine[::-1].count(i.lower())

print(nb1+nb2)

# ---------- User input Task 00 ---------- #

name = input("What is your name ? ")
print(f"Hello {name}")

# ---------- User input Task 01 ---------- #

name = input("What is your name ? ").capitalize()
print(f"Hello {name}")

# ---------- User input Task 02 ---------- #

nb1 = int(input("Choose a first number : "))
nb2 = int(input("Choose a second number : "))
sum = nb1 + nb2

print(f"The sum of the two provided numbers is {sum}")

# ---------- User input Task 03 ---------- #

nb = int(input("Choose a number : "))
print(type(nb))

# ---------- User input Task 04 ---------- #

input = "This is a test. is it possible to fly? Good things come to those who never give up."
sentences = input.replace('?', '.').split('. ')
s1, s2, s3 = [sentence.split()[0] for sentence in sentences[:3]]
print(s1, s2, s3)

# ---------- Exo bonus 1 ---------- #

# Bonjour1a1tous21je1suis1Albert1Nestor21le1castor31En1janvier1de1l4année1dernière21plus1de1dix5mille1personnes1m4ont1voués1un1culte31C4était1marrant21mais1un1peu1bizarre31En1tout1cas1plus1que1de1s4appeler1Albert1Nestor1en1étant1un1castor.

# Remplacer les 1 par des espaces, les 2 par des virgules, les 3 par des points, les 4 par des apostrophes, les 5 par des tirets.
# Trouver le nombre d'itération du mot castor
# Remplacer la première lettre de chaque mot castor par une majuscule

input = "Bonjour1a1tous21je1suis1Albert1Nestor21le1castor31En1janvier1de1l4année1dernière21plus1de1dix5mille1personnes1m4ont1voués1un1culte31C4était1marrant21mais1un1peu1bizarre31En1tout1cas1plus1que1de1s4appeler1Albert1Nestor1en1étant1un1castor."

print(input.replace("1", " ")
      .replace("2", ",")
      .replace("3", ".")
      .replace("4", "'")
      .replace("5", "-")
      .replace("castor", "Castor"))
print(int(input.count("castor")))

# ---------- Exo bonus 2 ---------- #

# racecarbananaappleleveldeifiedcivicnoonradarrotorreferkayakmadamtenetwowbobpoppeepredderrepaperrotatorlevelerreviverredividerdetartratedmalayalam

# Palindromes : Mot ou groupe de mots qui peut se lire indifféremment de gauche à droite ou de droite à gauche en gardant le même sens (ex. la mariée ira mal ; Roma Amor).

# L'objectif de l'exercice est de retrouver la liste de tous les palindromes dans le texte ci dessus. Pour ça, vous devez créer une fonction find_palindromic_substring, avec un paramètre str, et afficher chaque palindrome que vous trouvez. (Vous pouvez aussi retourner une liste de chaque palindrome qu'on affichera dans une autre fonction)
# La longueur d'un palindrome doit être d'au minimum 2 caractère

chaine = "racecar banana apple level deified civic noon radar rotor refer kayak madam tenet wow bob pop peep redder repaper rotator leveler reviver redivider detartrated malayalam"

def palindromes_operation(mot):
    return mot == mot[::-1]

def find_palindromic_substring(chaine):
    
    mots = chaine.split()
    
    palindromes = []
    
    for mot in mots:
        if palindromes_operation:
            palindromes.append(mot)
    return palindromes

palindrome_liste = find_palindromic_substring(chaine)
for palindrome in palindrome_liste:
    print(palindrome)
            