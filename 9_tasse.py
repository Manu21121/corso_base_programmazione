tassa = 0
tassa_1 = 22/100
tassa_2 = 33/100
reddito = int(input("Inserisci il tuo reddito: "))
if(reddito < 10000):
    tassa = 0 
if(10000 <= reddito <= 30000):
    tassa = tassa_1 * reddito
if(reddito > 30000):
    tassa_1 = (tassa_1 * 20000) 
    tassa_2 = (tassa_2 * (reddito - 30000))
    tassa = tassa_1 + tassa_2
print("Pagherai €", tassa)