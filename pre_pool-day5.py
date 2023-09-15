# # -*- coding: utf-8 -*-
# #Created by Willipatafoul at 09:30 on 15/09/2023
# #

# # ---------- Lists creation and browsing Task 01 ---------- #

# liste = [1,2,3,4,5]
# print(liste[0])

# # ---------- Lists creation and browsing Task 02 ---------- #

# liste = [1,2,3,4,5]
# print(liste[-1])

# # ---------- Lists creation and browsing Task 03 ---------- #

# liste = [1,2,3,4,5]
# liste.append(6)
# print(liste)

# # ---------- Lists creation and browsing Task 04 ---------- #

# liste = [1,2,3,4,5]
# print(liste[::])

# # ---------- Lists creation and browsing Task 05 ---------- #

# liste = [1,2,3,4,5]
# liste.remove(liste[-1])
# print(liste[::])

# # ---------- Lists creation and browsing Task 06 ---------- #

# liste = [1,2,3,4,5]
# liste.insert(0, "patate")
# print(liste)

# # ---------- Lists creation and browsing Task 07 ---------- #

# liste = [1,2,3,4,5]
# print(liste[1:5])

# print([1,2,3,4,5][1:5])

# # ---------- Lists creation and browsing Task 08 ---------- #

# liste = [1,2,3,4,5]
# liste2 = liste[::-1]
# print(liste2)

# # ---------- Lists creation and browsing Task 09 ---------- #

# liste = [1,2,3,4,5]
# print(liste[::2])

# # ---------- Lists creation and browsing Task 10 ---------- #

# liste = [1,2,3,4,5]
# for i in range(17):
#     liste.append(i)
#     i += 1
# print(liste)

# # ---------- Lists creation and browsing Task 11 ---------- #

# my_first_list = [4, 5, 6] 
# my_second_list = [1, 2, 3] 
# my_first_list.extend(my_second_list) #Concaténation de 2 listes
# print(my_first_list)


# my_first_list = [7, 8, 9]
# my_second_list = [4, 5, 6]
# my_first_list = [*my_first_list , *my_second_list] #Concaténation de 2 listes
# print(my_first_list)

# # ---------- Opertions on lists Task 01 ---------- #

# liste = [1,2,3,4,5,6,7,8,9,10]
# multiple = 1
# for element in liste:
#     multiple *= element
# print(multiple)

# # ---------- Opertions on lists Task 02 ---------- #
 
# print([x + 10 for x in [3, 2, 6, 7, 1, 4]]) #Ajoute +10 à chaque élément de la liste

# # ---------- Opertions on lists Task 03 ---------- #

# print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))) #Viens multiplier chaque élément par lui même
# #lambda = mini fonction rapide
# #map = renvoie un itérable que l'on peut transformer comme on le souhaite (listes, tuples..)

# # ---------- Opertions on lists Task 04 ---------- #

# liste = [1,2,3,4,-6,7,8,9000,10]
# print(max(liste), min(liste))

# # ---------- Opertions on lists Task 05 ---------- #

# liste = [1,2,3,4,-6,7,8,9000,10]
# print([x for x in liste if x < 7])

# # ---------- Opertions on lists Task 06 ---------- #

# liste = [1,2,3,4,-6,7,8,9000,10]
# liste.sort(reverse=True)
# print(liste)

# # ---------- Opertions on lists Task 07 ---------- #

# print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
# #Divise par 2 si c'est un multiple de 2 sinon on le multiplie par 2

# # ---------- Opertions on lists Task 08 ---------- #

# print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))
# #Filtre et affiche tout les élément de la liste > 10 non compris

# # ---------- Opertions on lists Task 09 ---------- #

# print([*enumerate([42, 3, 4, 18, 3, 10])])
# #Donne la position de chaque élément d'une liste, ici (0, 42), (1, 3)...

# # ---------- Opertions on lists Task 10 ---------- #

# first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"] 
# last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]
# magic = [*zip(first_name, last_name[::-1])] #Combine un ou plusieurs élément de la liste et les combine ensemble

# print(magic[0]) #Affiche l'élément [0] de la première liste et l'élément [3] de la deuxième
# print(magic[3]) #Affiche l'élément [3] de la première liste et l'élément [0] de la deuxième
# print(magic[1][0]) #Affiche que l'élément [1] de la première liste avec [0], bruce
# print(magic[0][1]) #Affiche que l'élément [0] de la  liste liste avec [1], chan
# print(magic[2]) #Affiche l'élément [2] de la première liste et l'élément [2] de la deuxième

# # ---------- Challenge ---------- #
# import time

# startingTime = time.time()
# print([x for x in range(1000001)])
# duration = time.time()- startingTime
# print(f"Affichage en {duration} secondes.")

# # ---------- Dictionaries Task 01, 02, 03, 04 ---------- #

# student = {
#     "name": "William",
#     "academic_year": "2023",
#     "units": {"name": "Web Dev", "credits": "6", "grade": "A"},
#     "units": {"name": "Network and System Administration", "credits": "4", "grade": "B"},
#     "units": {"name": "Java", "credits": "3", "grade": "C"},
#     "total_credits": "13",
#     "GPA": "3"
# }

# grade_weight_mapping = {
#     "A": "4",
#     "B": "3",
#     "C": "2",
#     "D": "1",
#     "E": "0"
# }

# ---------- Let's go further Task 01---------- #

liste = []

while len(liste) != 10:
    add = input("Ajouter un ambassadeur : ")
    liste.append(add)
    choix = input("Voulez vous continuer d'ajouter des ambassadeurs ? (yes/no) ")
    while choix != "yes":
        if choix == "yes":
            quit
        else:
            break









