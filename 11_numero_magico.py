NumMagico = 7
Numero = 0
tentativi = 1
while tentativi <= 10 :
    Numero = int(input("Prova ad indovinare il numero magico: "))
    if(Numero == NumMagico):
        print("Complimenti, hai indovinato!")
        break
    else: 
        tentativi = tentativi + 1
        if(tentativi == 11):
            print("Game Over!")

    
