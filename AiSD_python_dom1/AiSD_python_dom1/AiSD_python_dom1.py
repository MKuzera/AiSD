#-------------------------classes------------------------
def combine(lista): #laczy stringi w jedne (popawic aby w finkcji nizej moglo wiecej pobierac (naprawic jakw ychodzi poza indexy))
    word = ""
    for x in lista:
        word = word +" " + x
    
    return word

class president:
     def __init__(self,imie_nazwisko,lata,partia):

        self.imie_nazwisko = imie_nazwisko.replace("  ","")
        self.lata= lata.replace("  ","")
        self.partia=partia.replace("  ","")

     def czas_panowania_jego(self):
        lata = self.lata
        lata = lata.split("-")
        czas_panowania = int(lata[1]) - int(lata[0])
        return czas_panowania

     def print(self):
         print("\t\t{}\t\t{}\t\t{}\t\t \n".format(self.imie_nazwisko, self.lata, self.partia))




#--------------------baza---------------------------------
dane = open("presidents.txt", "r")
dane2 = dane.readlines()
lista = [] #lista linijek
count = 0
for line in dane2: #przetwarza linijki do listy
    count += 1
    lista.append(line.strip())  

lista_class = [] #lista klass
for line in lista: #splituje
    line2 = line.split(" ")
    line2.reverse()
   # print(line2)
    part = line2[0]
    lat = line2[1]

    imie = combine(line2[2:])


   
    #print(line2)
    x = president(imie,lat,part) # przypisuje fragmenty lini do klasy
    #x.print()
    lista_class.append(x)

#-----------------------------funkcje------------------------------------------

def krotki_czas(lista):
    czas = 100
    lista_prezydentow = []
    
    for each in lista:
        
        if(czas > each.czas_panowania_jego()):
           
            lista_prezydentow.clear()
            lista_prezydentow.append(each)
            czas = each.czas_panowania_jego()
        elif(czas == each.czas_panowania_jego()):
            lista_prezydentow.append(each)


    print("\n\nZad. 1\n\n")
    for each in lista_prezydentow:
        each.print()
        





def daj_parti(lista,partia):
    #lista2= []
    #for each in lista:
    #    lista2.append(each.partia) # tworzy liste partii
    #lista_partii = list(dict.fromkeys(lista2)).copy()

    lista3 = []

    for each in lista:
        if each.partia==partia:
            lista3.append(each)
            each.print()

    return lista3


def kto_rzadzi(lista,rok):
    for each in lista:
        lata = each.lata
        lata = lata.split("-")
        #print("Lata: {} {} - {} {}".format(lata[0],type(lata[0]),lata[1],type(lata[1])))

        if(rok >= int(lata[0]) and rok <= int(lata[1])):
            
            print("\nZad 3.\nszukana osoba to: {}".format(each.imie_nazwisko))
            return each.imie_nazwisko

#--------------------------------main-------------------------
#Zad 1
krotki_czas(lista_class)
#zad 2
print("\n\n\nZad. 2")
daj_parti(lista_class,"Democratic")
#zad 3
kto_rzadzi(lista_class,1884)