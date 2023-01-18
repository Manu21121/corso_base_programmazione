chek = 0
while chek == 0:
    stringa = input("Inserisci una stringa di soli numeri: ")
    l = len(stringa)
    i = 0
    output = 0
    while (i < l):
        if(stringa[i] == "0" or stringa[i] == "1" or stringa[i] == "2" or stringa[i] == "3" or stringa[i] == "4" or stringa[i] == "5" or stringa[i] == "6" or stringa[i] == "7" or stringa[i] == "8" or stringa[i] == "9"):
            output = output + int(stringa[i])
            i = i + 1
            chek = 1
        else:
            chek = 0
            break
print(output)
    