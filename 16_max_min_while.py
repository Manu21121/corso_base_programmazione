max = float("-inf")
min = float("inf")
numero = 0
while True: 
    numero = int(input("inserisci un numero: "))
    if(numero == 0):
        break
    if(numero >= max):
        max = numero
    if(numero <= min):
        min = numero
print("Il numero massimo è ", max)
print("Il numero minimo è ", min)