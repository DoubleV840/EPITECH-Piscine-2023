# -*- coding: utf-8 -*-
#Created by Willipatafoul at 09:18 on 12/09/2023
#


print(1+1)
print(30+12)
print(777+(-735))
print(1+2+3+5+7+11+13)

# ----------------------------------------------- #

print(84-42)
print(0-(-42))
print(2*21)
print((-6)*(-7))
print(2+5*8)
print((3+(3*4-2*2)*3-2)*2-3)

# ----------------------------------------------- #

print(84/2) #Division qui affiche les décimales
print(84//2) #Division qui n'affiche pas les décimales

# ----------------------------------------------- #

#print(84/(8 + (-3) + (-7) + 2)) #Indivisible par 0

# ----------------------------------------------- #

addition = 0
nombre = 1
n = 10

multiplicateur = int(input("Entrez un mutliplicateur : "))
for i in range(multiplicateur):
    # print(nombre)
    addition += nombre
    nombre += n
    n *= 10

power = int(input("Entrez une puissance : "))

resultat = addition**power

# print(addition)
print(resultat)

# ----------------------------------------------- #

print(17**1024)

# ----------------------------------------------- #

print(42/4, 42//4, 42%4, sep='\n')

# ----------------------------------------------- #

nb_pair = int(input("Entrez un nombre pour voir sa parité : "))

if nb_pair % 2 == 0:
    print("Votre nombre est pair !")
else:
    print("Votre nombre est impair")
    
# ----------------------------------------------- # 
    
number = 123434565
digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number //= 10

print("Sum of digits:", round(digit_sum)) #% 1 pour récuperer que les decimales

# ----------------------------------------------- #

incr = 1
pi = 0
i = 0

while i < 1000000:
    pi += ((-1) ** i)/(2 * i + 1)
    i += 1
    
pi *= 4
print(f"{pi:.6f}")

# ----------------------------------------------- #

def calculer_pi():
    somme = 0
    n = 0

    while True:
        terme = ((-1) ** n) / ((2 * n) + 1)
        somme += terme
        n += 1

        if n >= 1000000:  
            break
    pi_estime = 4 * somme
    
    return round(pi_estime, 6)
pi_calculé = calculer_pi()
print(f"La valeur estimée de pi avec la formule donnée est : {pi_calculé}")