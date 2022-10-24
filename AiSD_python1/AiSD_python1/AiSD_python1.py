
#-----------------------------------Klasy---------------------------------------


def combine(*args): #laczy stringi w jedne (popawic aby w finkcji nizej moglo wiecej pobierac (naprawic jakw ychodzi poza indexy))
    word = ""
    for x in args:
        word = word + " " + x
    
    return word


class struktura:

   def __init__(self,imie_nazwisko,kraj,wynik,rok):
        self.imie_nazwisko = imie_nazwisko 
        self.kraj=kraj
        self.wynik=wynik
        self.rok =rok

   def __lt__(self,other):
       return int(self.wynik) < int(self.wynik)

   def return_kraj(self):
       return self.kraj

   def return_rok(self):
       return int(self.rok)

   def return_ranking(self):
       return int(self.wynik)

   def print(self):
       print("{} {} {} {}".format(self.imie_nazwisko,self.kraj,self.wynik,self.rok))




#----------------------------------------Baza----------------------------

dane = open("dane.txt", "r")
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
    x = struktura(combine(line2[4],line2[3]),line2[2],line2[1],line2[0]) # przypisuje fragmenty lini do klasy
    
    lista_class.append(x)


#----------------------------------------funkcje-----------------------------------


def ranking_lista_return(lista,prog):
    lista2 = []
    for each in lista:
        if(each.return_ranking() > prog): # sprawdza czy przekracza prog
            lista2.append(each)

    lista2.sort() # poprzez funkcje wbudowana __lt__ pozwala okreslic nam sposob w jaki program ma posortowc liste
                  
    print("\n Zad. 1 \n")
    for each in lista2: # wysweitla
        each.print()
    return lista2

def najlepszy_z_kraju(lista):
    lista2 = [] 
    for each in lista:
        lista2.append(each.return_kraj()) # tworzy liste krajow

    lista_krajow = list(dict.fromkeys(lista2)).copy() #usuwa duplikaty
    ranking = []
    #print(lista_krajow)
    for each in lista_krajow:
        maxi = 0
        #persona=struktura("","","","")
        for person in lista:
            if(person.return_ranking() > maxi and person.return_kraj()==each):
                #print("{} > {} and {} == {}".format(person.return_ranking() , maxi , person.return_kraj(),each))
                maxi = person.return_ranking()
                persona = person
        ranking.append(persona)
    print("\nZad. 2\n")
    for each in ranking:
        each.print()
  

def usun_przed_30(lista): #usuwa 
    lista2 = lista.copy() #uzuwam copi aby zebrac informacje na temat pozycji do usuniecia (iterowanie oraz usuwanie naraz po tej samej liscie nie dziala)
    i =0
    for each in lista2:
        
        if(int(each.return_rok())< 2022-30): # i - zbiera informacje na ktorej pozycji teraz sie znajduje 
            #print(each.return_rok())
            #print(" ")
            #print(i)
            lista.pop(i)
            i-=1
        i+=1
    print("\nZad. 3\n")
    for each in lista:
        each.print()

    return
        




#------------------------------------------main--------------------------

#Zad 1.
table = ranking_lista_return(lista_class,2750) 

#Zad 2.
najlepszy_z_kraju(lista_class)
#Zad 3.
usun_przed_30(lista_class)