#Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. Wartość stałej
#π weź z biblioteki math. Promień nie może być ujemny. W przypadku podania liczby ujemnej, program
#powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.

import math
p = math.pi

while True:
    try:
        r = int(input("Podaj promień okręgu: "))
        if r > 0:
            print("Obwód okręgu to:", 2*p*r, ". ")
            print("Pole koła to: ", p*r*r , ".")
        else:
            print("Promień nie może być liczbą ujemną. ")
            break
    except ValueError:
        print("Musisz podać wartość liczbową. ")

