import random

count = 0
tirage = []
space = "-"

while count < 5:
    number = random.randint(1,49)
    while number in tirage:
        number = random.randint(1,49)
    tirage.append(number)
    count += 1

tirage = sorted(tirage)
chance = random.randint(1,10)

print("Vos numéros : ", tirage[0], space, tirage[1], space, tirage[2], space, tirage[3], space, tirage[4])
print("Numéro chance : ", chance)
