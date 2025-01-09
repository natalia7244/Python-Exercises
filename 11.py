# Napisz program, który prosi użytkownika o podanie dwóch liczb, a następnie sprawdza:
# Czy pierwsza liczba jest większa od drugiej.
# Czy obie liczby są równe.
# W przeciwnym razie informuje, że druga liczba jest większa.

try:
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    if a > b:
        print("Liczba", a, "jest większa od liczby", b,".")
    if a < b:
        print("Liczba", a, "jest mniejsza od", b, ".")
    else:
        print("Liczby są równe.")
except ValueError:
    print("Nie podałeś liczby.")
