stringa = input("Inserisci una stringa: ")
i = 0
l = len(stringa)
output = ""
while (i < l):
    if(stringa[i] != "A" and stringa[i] != "a" and stringa[i] != "E" and stringa[i] != "e" and stringa[i] != "I" and stringa[i] != "i" and stringa[i] != "O" and stringa[i] != "o" and stringa[i] != "U" and stringa[i] != "u" ):
        output = output + stringa[i]
    i = i + 1
print(output)