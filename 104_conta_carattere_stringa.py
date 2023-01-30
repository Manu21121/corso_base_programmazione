stringa = input("Inserisci una stringa: ")
carattere = input("Inserisci il carattere da cercare: ")
conta_carattere = 0
i = 0
l = len(stringa)
while (i < l):
    if(stringa[i] == carattere):
        conta_carattere = conta_carattere + 1
    i = i + 1
print(conta_carattere)