i = 1
somma = 0
media = 0
while True: 
    numero = int(input("Inserisci un numero: "))
    somma = somma + numero 
    if(i == 1): 
        media = somma / i
    else: 
        media = somma / (i -1)
    if(numero == 0):
        print(media)
        break
    i = i + 1