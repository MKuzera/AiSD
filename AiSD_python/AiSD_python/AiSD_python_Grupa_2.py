
#ZADANIE GRUPA 2 zrobione: 16;53 24.10.20202

#-----------------------------------BAZA----------------------------------
#baza: klasy


class Jezyk:
    
        def __init__(self,nazwa,ilosc):
            self.nazwa = nazwa
            self.ilosc = ilosc
       

        def print(self):
            print(self.nazwa + " " + self.ilosc)



class struktura:
    

    def __init__(self, rok, kraj, tytul,autor,jezyk):
        self.rok = rok
        self.kraj = kraj
        self.tytul = tytul
        self.autor= autor
        self.jezyk = jezyk


    def return_rok(self):
        return int(self.rok)

    def return_kraj(self):
        return self.kraj


    def return_jezyk(self):
        return self.jezyk


    def print(self):

        print(self.rok + " " + self.kraj + " " + self.tytul + " " + self.autor + " " +self.jezyk +"\n")

    
#---------------------------------------------pre-main-------------------------------------------
#Pobierz dane z pliku i zamien tekst na liste klas z poszczegolnymi atrybutami


dane = open("dane.txt", "r")
dane2 = dane.readlines()
lista = [] #lista linijek
count = 0
for line in dane2: #przetwarza linijki do listy
    count += 1
    lista.append(line.strip()) 
lista_class = [] #lista klass
for line in lista: #splituje
    line2 = line.split(", ")
    x = struktura(line2[0],line2[1],line2[2],line2[3],line2[4])
    lista_class.append(x) #lista_class -> pelna lista z klasami oraz wszytskimi danymi o linijce



#---------------------------------FUNCTIONS-------------------------------------------------


def jezyki_w_turnieju(lista): # Zwraca liste z: Danym jezykiem (nie powtarzaja sie) oraz iloscia wystapien w liscie
    #Oraz wyswietla w konsoli

    lista3 = [] #lista robocza 
   
    for each in lista:
       
        lista3.append(each.return_jezyk()) #do listy3 przypisuje wszytskie jezyki

    lista_jezykow = list(dict.fromkeys(lista3)).copy() #usuwa duplikaty
    lista_koniec = [] #lista robocza

    for each in lista_jezykow:
        lista_koniec.append((each,lista3.count(each)))# do listy koncowe wypisuje jezyk (z listy jezykow bez 
                                                      # duplikatow) oraz ilosc wystapien (danego jezyka) w liscie3


    print("Zad 1. \n" ) # Wypisuje
    for nazwa,numer in lista_koniec:
        print("{} : {}".format(nazwa,numer) )

    return lista_koniec # zwraca ta liste 

   

def wygrani_ponad_2_razy(lista):

    lista2 = [] #lista robocza 
   
    for each in lista:
        lista2.append(each.return_kraj()) #do listy3 przypisuje wszytskie kraje

    lista_krajow = list(dict.fromkeys(lista2)).copy() #usuwa duplikaty
    lista_koniec = [] #lista robocza

    for each in lista_krajow:
        if(lista2.count(each)>2): # jesli wiecej niz 2 zwyciestwa to wykonaj >
             lista_koniec.append((each,lista2.count(each)))# do listy koncowej wypisuje kraj (z listy jezykow bez 
                                                      # duplikatow) oraz ilosc wystapien (danego kraju) w liscie3

    print("\nZad 2. \n" ) # Wypisuje
    for nazwa,numer in lista_koniec:
        print("{} : {}".format(nazwa,numer) )

    return lista_koniec # zwraca ta liste 
  

def usun_przed_2000(lista): #usuwa 
    lista2 = lista.copy() #uzuwam copi aby zebrac informacje na temat pozycji do usuniecia (iterowanie oraz usuwanie naraz po tej samej liscie nie dziala)
    i =0
    for each in lista2:
        
        if(int(each.return_rok())< 2000): # i - zbiera informacje na ktorej pozycji teraz sie znajduje 
            #print(each.return_rok())
            #print(" ")
            #print(i)
            lista.pop(i)
            i-=1
        i+=1
  
   
    return


#----------------------------------MAIN-----------------------------------------------------

#ZAD 1
lista_jezykow_w_turnieju = []
lista_jezykow_w_turnieju = jezyki_w_turnieju(lista_class).copy()
#ZAD 2
lista_wygranych_krajow= []
lista_wygranych_krajow=wygrani_ponad_2_razy(lista_class).copy()
#ZAD 3
usun_przed_2000(lista_class)
print("\n Zad 3. \n")
for each in lista_class:
    each.print()

