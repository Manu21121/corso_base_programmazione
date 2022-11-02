i = 1
n_op = int(input("Inserisci il numero di operazioni da effettuare: "))
while (i == n_op):
    if n_op == 1:
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        op = int(input("Inserisci 1 per effettuare la somma, 2 per la sottrazzione, 3 per la divisione o 4 per la moltiplicazione: "))   
        if(op > 4):
            op = 1
        if(op < 1):
            op = 1
        if(op == 1):
            risultato = n1 + n2
        if(op == 2):
            risultato = n1 - n2
        if(op == 3):
            if(n2 == 0):
                risultato = str("Non puoi dividere per 0!")
            else:
                risultato = n1 / n2
        if(op == 4):
            risultato = n1 * n2
            print(risultato)
            break
    if (n_op > 1):
        n = int(input("inserisci un numero"))
        op = int(input("Inserisci l'operazione da effettuare: "))
        if(op > 4):
            op = 1
        if(op < 1):
            op = 1
        if(op == 1):
            risultato = n + risultato
        if(op == 2):
            risultato = n - risultato
        if(op == 3):
            if(risultato == 0):
                risultato = str("Non puoi dividere per 0!")
            else:
                risultato = n / risultato
        if(op == 4):
            risultato = n * risultato
        print(risultato)
i = i + 1