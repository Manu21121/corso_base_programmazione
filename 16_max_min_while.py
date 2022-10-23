max = float("-inf")
min = float("inf")
while True: 
    numero = int(input("inserisci un numero: "))
    if(numero > 0):
        if(numero > max):
            max = numero
        if(numero < min):
            min = numero
        else: 
            min = min
    if(numero == 0):
        print("Il numero massimo è ", max)
        print("Il numero minimo è ", min)
        break
    