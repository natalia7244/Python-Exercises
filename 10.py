#Zadanie 2
# Napisz program, który sprawdzi, czy podana przez użytkownika liczba jest parzysta, czy nieparzysta.

try:
    a = int(input("Podaj liczbę całkowitą: "))
    if a % 2 == 0:
        print("Ta liczba jest parzysta")
    else:
        print("Ta liczba jest nieparzysta.")
except ValueError:
    print("Mie podałeś liczby całkowitej.")