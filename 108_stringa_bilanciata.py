stringa_1 = input("inserisci la prima stringa: ")
stringa_2 = input("inserisci la seconda stringa: ")
i = 0
l = len(stringa_1)
while(i < l):
    is_present = stringa_1[i] in stringa_2
    if(is_present == False):
        break
    i = i + 1
print(is_present)