#Napisz program, który prosi o podanie współczynników równania kwadratowego ax2 + bx + c = 0 i wypisuje
#rozwiązania równania (lub informację o braku rozwiązań).

a = int(input("Podaj współczynnik a równania kwadratowego: "))
if a == 0:
    print(" To nie jest równanie kwadratowe. Podaj a różne od zera. ")
b = int(input("Podaj współczynnik b równania kwadratowego: "))
c = int(input("Podaj współczynnik c równania kwadratowego: "))


while True:
    try:
        delta = (b * b) - (4 * a * c)
        if a == 0:
            print(" To nie jest równanie kwadratowe. Podaj a różne od zera. ")
            break
        if delta > 0:
            x1 = (-b + delta * 1/2) / 2*a
            x2 = (-b - delta * 1 / 2) / 2*a
            print("Równanie kwadratowe ma dwa rozwiązania. Oto one: ", x1, x2, ".")
            break
        if delta == 0 :
            x = -b  / 2*a
            print("Równanie kwadratowe ma jedno rozwiązanie, które wynosi ", x, ".")
            break
        else:
            print("Brak rozwiązań równania kwadratowego. ")
            break

    except ValueError:
        print("Podaj wartość liczbową.")