n_operazioni = int(input("Inserisci il numero di operazioni da fare: "))
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
op = int(input("Inserisci 1 per effettuare la somma, 2 per la sottrazzione, 3 per la divisione o 4 per la moltiplicazione: "))
risultato = 0
i = 1
while i == n_operazioni:
    if(op == 1 or op == 2 or op == 3 or op == 4):
        if(op == 1):
            risultato = n1 + n2
            print(risultato)
        if(op == 2):
            risultato = n1 - n2
            print(risultato)
        if(op == 3):
            risultato = n1 / n2
            print(risultato)
            if(n2 == 0):
                print("Non puoi dividere per 0!")
                break
        else: 
            risultato = n1 * n2
    else: 
        risultato = n1 + n2
        print(risultato)
        break
i = i + 1