from re import A


Lettera= input("inserisci una lettera: ")
if (Lettera== "A"):
    print ("Hai scelto Alina!")
else: 
    print ("Hai scelto una lettera diversa da A")
    if(Lettera == "B"):
        print("Hai scelto Bruno!")
    else:
        print("Hai scelto una lettera diversa da A o B")
        if(Lettera == "C"):
            print("HAi scelto Carlo!")
        else:
            print("Hai scelto una lettera diversa da A o B o C")
            if(Lettera == "C"):
                print("Hai scelto Dario!")
            else:
                if(Lettera == "D"):
                    print("Hai scelto Dario!")
                else:
                    print("You choose ... poorly")
