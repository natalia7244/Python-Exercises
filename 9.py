#Zadanie 1
# Napisz program, który poprosi użytkownika o podanie dwóch liczb, a następnie wyświetli ich sumę.

try:
    a = float(input("Podaj pierwszą liczbę : "))
    b = float(input("Podaj drugą liczbę : "))
    print("Suma podanych liczb to: ", a+b)
except ValueError:
    print("Podaj poprawną liczbę!")
