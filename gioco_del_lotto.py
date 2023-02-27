import random
i = 0
numero_1 = 0
numero_2 = 0
numero_3 = 0
numero_4 = 0
numero_5 = 0
while(i <= 5):
    numero = random.randint(1,90)
    if (i == 1):
        numero_1 = numero
    if (i == 2):
        numero_2 = numero
    if (i == 3):
        numero_3 = numero
    if (i == 4):
        numero_4 = numero
    if (i == 5):
        numero_5 = numero
    if (numero == numero_1 or numero == numero_2 or numero == numero_3 or numero == numero_4 or numero == numero_5):
        print(numero)
    i = i + 1