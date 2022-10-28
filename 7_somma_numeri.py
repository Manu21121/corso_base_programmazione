Somma=0
N1= int(input("inserire il primo numero: "))
N2= int(input("inserire il secondo numero: "))
N3= int(input("inserire il terzo numero: "))
Somma= int((N1 + N2 + N3))
if (Somma > 10):
    if (N1 > N2):
        if (N1 > N3):
            print("Il numero maggiore è il primo: ", N1)
        else:
            print("Il numero maggiore è il terzo: ", N3)
    else: 
        if(N2 > N3):
            print("Il numero maggiore è il secondo: ", N2)
        else:
            print("Il numero maggiore è il terzo: ", N3)
else:
    print("La somma dei tre numeri è ", Somma)
    