numero_magico = 7
numero = 0
i = 1
while i <= 10 :
    numero = int(input("Prova ad indovinare il numero magico: "))
    if(numero == numero_magico):
        print("Complimenti, hai indovinato!")
        break
    else: 
        i = i + 1
        if(i == 11):
            print("Game Over!")

    
