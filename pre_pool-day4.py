# # -*- coding: utf-8 -*-
# #Created by Willipatafoul at 09:33 on 14/09/2023
# #
# # ---------- Conditionals Task 00 ---------- #

# print(42 > 12)
# print(12 == 12)
# print("hello" == "world") 
# print(218 >= 118)
# print("a".upper() == "A")
# print(1*2*3*4<=9)
# print("z" in "azerty")

# # ---------- Conditionals Task 01 ---------- #

# nb = input("Entrez un nombre : ")
# if nb == '42':
#     print(True)
# else:
#     print("Pas égal à 42")

# # ---------- Conditionals Task 02 ---------- #

# nb = int(input("Entrez un nombre : "))
# if nb % 2 == 0:
#     print("This integer is even")
# else:
#     print("This integer is odd")
    
# # ---------- Conditionals Task 03 ---------- #

# nb = input("Entrez une phrase pour ouvrir la porte : ")
# if nb == "open sesame":
#     print("Access granted")
# elif nb == "will you open":
#     print("Access fucking granted")
# else:
#     print("Permission denied")
    
# # ---------- Conditionals Task 04 ---------- #

# nb = int(input("Entrez un nombre : "))

# if nb == 42:
#     print("OK")
# elif nb <= 21:
#     print("OK 2")
# elif nb % 2 == 0:
#     print("OK 3")
# elif nb / 2 < 21:
#     print("OK 4")
# elif nb % 2 != 0 and nb >= 45:
#     print("OK 5")
# else:
#     print("You got wrong my poor friend!")
    
# # ---------- Conditionals Task 05 ---------- #

# a = 42
# b = 41 

# if a == b:
#     print("A and B are the sames") 
# elif b <= a:
#     print("B is equal or lower as A")
# elif b != a:
#     print("B his different from A")
    
# # ---------- Loops Task 00 ---------- #

# for nb in range(0, 1001):
#     print(nb)

# # ---------- Loops Task 01 ---------- #

# chaine = input("Entrez un mot : ")

# mot_double = ""

# for mot in chaine:
#     mot_double += mot * 2
# print(mot_double)

# # ---------- Loops Task 02 ---------- #

# for nb in range(0, 10001):
#     if nb % 7 == 0:
#         print(nb)
    
# # ---------- Loops Task 03 ---------- #

# for nb in range(-30, 31):
#     if nb % 3 == 0 and nb % 5 == 0:
#         print("FizzBuzz")
#     elif nb % 3 == 0:
#         print("Fizz")
#     elif nb % 5 == 0:
#         print("Buzz")
#     else: 
#         print(nb)

# # ---------- Loops Task 04 ---------- #
# nb = 99

# for nb in range(99, -1, -1):
#     if nb != 0:
#         print(f"{nb} bottle(s) of age appropriate bottles on the wall")
#     else:
#         print("Il y a plus de boutilles !!!!!")
        
# ---------- Loops Task 05 ---------- #

nombre = int(input("Ecrit un nombre à fractionner : "))
for i in range(2, nombre // 2 + 1):
    multiples = [j for j in range(i, nombre, i) if j < nombre]
    multiples.sort(reverse=True)
    print(multiples)