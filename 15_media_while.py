media = 0
i = 0
numero = 0
while True:
    numero = int(input("Inserisci il numero: "))
    media = media + numero
    if numero == 0:
        break
    i = i + 1
media = media/i
print("La media è ",media)