numero = int(input("inserisci un numero: "))
max = numero
min = numero
while numero != 0: 
    if(numero > max):
        max = numero
    if(numero < min):
        min = numero
    numero = int(input("inserisci un numero: "))
print("Il numero massimo è ", max)
print("Il numero minimo è ", min)