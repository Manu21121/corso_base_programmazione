stringa = input("Inserisci una stringa: ")
i = 0
l = len(stringa)
output = ""
while (i < l):
    if(stringa[i] != "a" and stringa[i] != "A" and stringa[i] != "e" and stringa[i] != "E" and stringa[i] != "i" and stringa[i] != "I" and stringa[i] != "o" and stringa[i] != "O" and stringa[i] != "u" and stringa[i] != "U" ):
        output = output + stringa[i]
    i = i + 1
print(output)