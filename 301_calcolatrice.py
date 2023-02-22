def somma(x,y):
    return x+y
def differenza(x,y):
    return x - y
def moltiplicazione(x,y):
    return x * y
def divisione(x,y):
    if y!=0:
        divisione = x / y
    else:
        divisione = "Impossibile"
    return divisione
while True:
    n_1: int = int(input("Inserisci il primo numero: "))
    operazione : str = input("Inserisci l'operazione (+,-,*,/): ")
    n_2: int = int(input("inserisci il secondo numero: "))
    if operazione == "+":
        print(somma(n_1,n_2))
    if operazione == "-":
        print(differenza(n_1,n_2))
    if operazione == "*":
        print(moltiplicazione(n_1,n_2))
    if operazione == "/":
        print(divisione(n_1,n_2))
    while True:
        continuo: str = input("Vuoi continuare? (yes/no): ")
        if continuo == "yes" or continuo == "no":
            break
    if continuo == "no":
        break