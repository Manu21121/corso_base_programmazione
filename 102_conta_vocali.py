stringa = input("Inserisci una stringa: ")
l = len(stringa)
i = 0
output = 0
while (i < l):
    if stringa[i] =="a" or stringa[i] =="e" or stringa[i] =="i" or stringa[i] =="o" or stringa[i] =="u" or stringa[i] =="A" or stringa[i] =="E" or stringa[i] =="I" or stringa[i] =="O" or stringa[i] =="U":
        output=output+1
    i=i+1
print(output)