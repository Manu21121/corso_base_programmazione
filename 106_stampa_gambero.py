stringa = input("Inserisci una stringa: ")
i = len(stringa) - 1
output = ""
while i >= 0:
    output = output + stringa[i]
    i = i - 1
print(output)