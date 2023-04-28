import random
def selectRandom(nazioni):
    return random.choice(nazioni)

nazioni = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua & Barbuda","Arabia Saudita","Argentina","Armenia","Aruba","Australia", "Austria", "Azerbaigian", "Bahamas","Bahrein","Bangladesh","Barbados","Belgio","Belize","Benin","Bermuda","Bhutan","Bielorussia","Birmania","Bolivia","Bosnia-Erzegovina","Botswana","Brasile","Bretagna","Brunei","Bulgaria","Burkina Faso","Burundi","Cambogia","Cameroun","Canada","Capo Verde","Cayman","Ciad","Cile","Cina","Cipro","Città del Vaticano","Colombia","Comore","Corea del Nord","Corea del Sud","Costa d'Avorio","Costa Rica","Croazia","Cuba","Danimarca","Dominica","Ecuador","Egitto","El Salvador","Emirati Arabi Uniti","Eritrea","Estonia","Etiopia","Figi","Filippine","Finlandia","Francia","Gabon","Gambia","Georgia","Germania","Ghana","Giappone","Gibilterra","Gibuti","Giordania","Grecia","Grenada","Groenlandia","Guadalupa","Guatemala","Guinea","Guinea Equatoriale","Guinea-Bissau","Guyana","Haiti","Honduras","Hong Kong","India","Indonesia","Iran","Iraq","Irlanda","Islanda","Isole Vergini","Isole Vergini Britanniche","Israele","Italia","Giamaica","Kazakistan","Kenya","Kirghizstan","Kiribati","Kuwait","Laos","Lapponia","Lesotho","Lettonia","Libano","Liberia","Libia","Liechtenstein","Lituania","Lussemburgo","Macedonia del nord","Madagascar","Madeira","Malawi","Maldive","Malesia","Mali","Malta","Marocco","Marshall Islands","Martinica","Mauritania","Mauritius","Messico","Micronesia","Moldavia","Mongolia","Montenegro","Montserrat","Mozambico","Namibia","Nauru","Nepal","Nicaragua","Niger","Nigeria","Norvegia","Nuova Caledonia","Nuova Zelanda","Olanda","Oman","Pakistan","Palau","Palestina","Panama","Papua Nuova Guinea","Paraguay","Perù","Polinesia Francese","Polonia","Portogallo","Porto Rico","Monaco","Qatar","Regno Unito","Rep. Ceca","Rep. Centrafricana","Rep. Del Congo","Rep. Dominicana","Romania","Russia","Rwanda","Sahara","Saint Kitts e Nevis","Samoa","San Marino","Santa Lucia","Sao Tome & Principe","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Siria","Slovacchia","Slovenia","Solomon Islands","Somalia","Spagna","Sri Lanka","Sudafrica","Sudan","Suriname","Svezia","Svizzera","Tagikstan","Tanzania","Thailandia","Timor Est","Togo","Tonga","Trinidad & Tobago","Tunisia","Turchia","Turkmenstan","Turks e Caicos","Tuvalu","Ucraina","Uganda","Ungheria","Uruguay","USA","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

europa = ["Albania", "Andorra", "Austria","Belgio", "Bielorussia", " Bosnia-Erzegovina", "Bretagna", "Bulgaria", "Cipro", "Città del Vaticano", "Croazia", "Danimarca", "Estonia", "Finlandia", "Francia","Georgia", "Germania", "Grecia", "Irlanda", "Islanda", "Italia", "Kazakistan","Lapponia", "Lettonia", "Liechtenstein", "Lituania", "Lussemburgo", "Macedonia del nord", "Malta", "Moldavia", "Monaco", "Montenegro", "Norvegia", "Olanda", "Paesi Bassi", "Polonia", "Portogallo", "Regno Unito", "Rep. Ceca", "Romania", "Russsia", "San Marino", "Serbia", "Slovacchia", "Slovenia", "Spagna", "Svezia", "Svizzera", "Turchia", "Ucraina", "Ungheria"]

america = ["Anguilla", "Aruba", "Bermuda", "Canada", "Cayman", "Groenlandia", "Messico","Saint-Pierre e Miquelon", "USA", "Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panama", "Antigua & Barbuda", "Bahamas", "Barbados", "Cuba", "Dominica", "Rep. Dominicana", "Grenada", "Guadalupa", "Haiti", "Giamaica", "Martinica", "Montserrat", "Saint Kitts e Nevis", "Santa Lucia", " Saint Vincent e Grenadine","Trinidad & Tobago", "Turks e Caicos","Isole Vergini", "Isole Vergini Britanniche","Argentina", "Bolivia", "Brasile", "Cile", "Colombia", "Ecuador", " Georgia del Sud e Isole Sandwich Australi", "Guyana", "Isole kalkland", "Paraguay", "Perù", "Porto Rico", "Suriname", "Uruguay", "Venezuela"]

asia = ["Afghanistan", "Arabia Saudita", "Armenia", "Azerbaigian", "Bahrein", "Bangladesh", "Bhutan", "Brunei","Cambogia", "Cina", "Corea del Nord", "Corea del Sud", "Emirati Arabi Uniti", "Filippine", "Georgia", "Giappone", "Giordania", "India", "Indonesia", "Iran", "Iraq", "Israele", "Kazakistan", "Kirghizstan", "Kuwait", "Laos", "Libano", "Maldive", "Malesia", "Mongolia", "Nepal", "Oman","Palestina", "Pakistan", "Qatar", "Russia", "Singapore", "Siria", "Sri Lanka", "Tagikstan", "Thailandia", "Timor Est", "Turchia", "Turkmenstan", "Uzbekistan", "Vietnam", "Yemen" ]

africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroun", "Capo Verde", "Rep. Centrafricana", "Ciad", "Comore", "Costa d'Avorio","Rep. Del Congo", "Egitto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana","Gibuti", "Guinea", "Guinea-Bissau", "Guinea Equatoriale", "Kenya", "lesotho", "Liberia", "Libia", "Madagascar","Madeira", "Malawi", "Mali", "Mauritania", "Mauritius", "Marocco", "Mozambico", "Namibia", "Niger", "Nigeria", "Rwanda", "Sahara", "Sao Tome & Principe","Senegal", "Seychelles", "Sierra Leone", "Somalia", "Sudafrica", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe" ]

oceania = ["Australia", "Birmania", "Nuova Caledonia", "Nuova Zelanda", "Papua Nuova Guinea", "Figi", "Solomon Islands", "Vanuatu", "Micronesia", "Kiribati", "Marshall Islands","Polinesia Francese","Palau", "Nauru", "Samoa", "Tonga", "Tuvalu"]

contatore = 1
punteggio = 0
print("Modalità 1- indovina a che continente appartengono gli stati")
print("Modalità 2- chiedi al programma uno stato e lui ti dirà a che continente appartiene")
modalità = input("Scegli la modalità (1 o 2): ")
if(modalità == "1"):
    while(contatore <= 20):
        
        scelta = random.choice(nazioni)
        # una volta scelta la nazione la togliamo dalla lista così da non poterla riscegliere
        
        nazioni = [i for i in nazioni if i not in scelta]
        print("------------------------------------------------------------------")
        print("Scegli il continente tra: europa, america, asia, africa, oceania")
        print("(fai attenzione a scrivere nel modo giusto)")
        print(scelta)
        continenti = input("In che continente si trova: ")
        
        
        if (continenti == "europa"):
            if scelta in europa: 
                print("CORRETTO!")
                punteggio = punteggio + 1
            else:
                print("SBAGLIATO!")
        if(continenti == "america"):
            if scelta in america: 
                print("CORRETTO!")
                punteggio = punteggio + 1
            else:
                print("SBAGLIATO!")       
        if(continenti == "africa"):
            if scelta in africa:
                print("CORRETTO!")
                punteggio = punteggio + 1
            else:
                print("SBAGLIATO!")
        if(continenti == "asia"):
            if scelta in asia:
                print("CORRETTO!")
                punteggio = punteggio + 1
            else:
                print("SBAGLIATO!")                
        if(continenti == "oceania"):
            if scelta in oceania:
                print("CORRETTO!")
                punteggio = punteggio + 1
            else:
                print("SBAGLIATO!")
        
        contatore = contatore + 1
    print("Il tuo punteggio è: ",punteggio)
    
if(modalità == "2"):
    while True:
        print("------------------------------------------------------------------------------------------")
        print("Fai attenzione a scrivere senza errori e con la maiuscola; (per uscire inserisci 'esci')")
        stato = input("Inserisci il nome di uno stato: ")
        if(stato == "esci"):
            break
        if stato in europa: 
            print("lo stato si trova in Europa")
        
        if stato in america: 
            print("lo stato si trova in America")
            
        if stato in asia:
            print("lo stato si trova in Asia")
            
        if stato in africa:
            print("lo stato si trova in Africa")
                    
        if stato in oceania:
            print("lo stato si trova in Oceania")