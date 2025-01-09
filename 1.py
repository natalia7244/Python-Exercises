#Napisz program proszący użytkownika o imię i rok urodzenia, a następnie obliczający i wypisujący jego
#wiek

input("Podaj swoje imię: ")

while True:
    try:
        m = int(input("Podaj rok urodzenia: "))
        if m > 0 and m < 2024:
            n = 2024 - m
            print("Masz ", n, "lat.")
            break
        else:
            print("Podaj prawdziwy rok urodzenia. ")
    except ValueError:
        print("To nie jest wartość liczbowa. Podaj swój wiek. ")


