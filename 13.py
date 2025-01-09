#Napisz program, który pyta użytkownika o zdobyte punkty (0–100) i na podstawie tych punktów przydziela ocenę według poniższej skali:
    #0–39: ocena 1 (niedostateczny)
    #40–59: ocena 2 (dopuszczający)
    #60–74: ocena 3 (dostateczny)
    #75–89: ocena 4 (dobry)
    #90–100: ocena 5 (bardzo dobry)
#Jeśli użytkownik poda liczbę spoza zakresu (np. -10 lub 105),
#program powinien wypisać komunikat: "Nieprawidłowa liczba punktów."


a = int(input("Podaj liczę uzyskanych punktów na egzaminie: "))
if a >= 0 and a <= 39:
    print("Niedostateczny")
elif a >= 40 and a <= 59:
    print("Dopuszczajacy")
elif a >= 60 and a <= 74:
    print("Dostateczny")
elif a >= 75 and a <= 89:
    print("Dobry")
elif a >= 90 and a <= 100:
    print("Bardzo dobry")
else:
    print("Nieprawidłowa liczba punktów")

