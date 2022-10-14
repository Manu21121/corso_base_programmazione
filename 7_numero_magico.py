NumMagico = 7
Numero = 0
tentativi = 1
while tentativi <= 10 :
    tentativi = tentativi + 1
    Numero = int(input("Prova ad indovinare il numero magico: "))
    if(Numero == NumMagico):
        print("Hai indovinato, il numero magico era 7!")
        break
else: 
    print("Game Over!")

    
