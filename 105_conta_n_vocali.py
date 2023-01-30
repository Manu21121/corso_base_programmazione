stringa = input("Inserisci una stringa: ")
l = len(stringa)
counter = 0
output = 0
a = 0
e = 0
i = 0
o = 0
u = 0
while(counter < l):
    if(stringa[counter] == "a" or stringa[counter] == "A"):
        a = a + 1
    if(stringa[counter] == "e" or stringa[counter] == "E"):
        e = e + 1
    if(stringa[counter] == "i" or stringa[counter] == "I"):
        i = i + 1
    if(stringa[counter] == "o" or stringa[counter] == "O"):
        o = o + 1
    if(stringa[counter] == "u" or stringa[counter] == "U"):
        u = u + 1
    counter = counter + 1
print("a = ", a)
print("e = ", e)
print("i = ", i)
print("o = ", o)
print("u = ", u)