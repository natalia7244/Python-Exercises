#Napisz program, który wylosuje dowolną liczbę całkowitą od zera do 10 (do losowania liczb użyj np. funk-
#cji randint z biblioteki random https://docs.python.org/3/library/random.html), a następnie prosi
#użytkownika o jej zgadnięcie tak długo, aż ten poda poprawną wartość. Gdy program działa, rozszerz go
#np. o podawanie informacji za którym razem udało się zgadnąć lub o wskazówki typu ”Podana przez ciebie
#liczba jest większa/mniejsza od wylosowanej”.

import random

while True:
    try:
        a = int(input("Podaj liczbę całkowitą z przedziału od 0 do 10: "))
        if a < 0:
             print(" Wybierz liczbę większą od 0. ")

        elif a > 10:
            print("Wybierz liczbę mniejszą od 10. ")
        else:
            break
    except ValueError:
        print("Podaj poprawną liczbę. ")


x = random.randint(0,10)

while a != x:
        if a < x:
            print(" Twoja liczba jest mniejsza od wylosowanej. ")
            #a = int(input(" Spróbuj ponownie: "))
        if a > x:
            print(" Twoja liczba jest większa od wylosowanej. ")
            #a = int(input(" Spróbuj ponownie: "))
        try:
            a = int(input("Może teraz Ci się uda. Podaj kolejną liczbę: "))
        except ValueError:
            print("Podaj poprawną liczbę. ")
print("Barwo, udało Ci się. ")








