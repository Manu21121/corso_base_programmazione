output = 0
output2 = 0
magg_50 = 0
min_15 = 0
i = 1
while i <= 10:
    numero = int(input("Inserisci un numero: "))
    if(numero > 50):
        magg_50 = magg_50 + 1
        output = str(magg_50 * "*")
    if(numero < 15):
        min_15 = min_15 + 1
        output2 = str(min_15 * "#")
    i = i + 1
print(output + output2)



