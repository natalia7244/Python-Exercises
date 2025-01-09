#Napisz funkcję znajdz_parzyste, która przyjmuje dwa argumenty poczatek i koniec
# i zwraca listę liczb parzystych z tego
# zakresu (włącznie z poczatek i koniec, jeśli są parzyste).


while True:
    try:
        a = int(input("Podaj liczbę, która będzie początkiem listy: "))
        b = int(input("Podaj liczbę, która będzie końcem listy: "))
        if a > b:
            print("Druga liczba musi być większa od pierwszej")
        else:
            break
    except ValueError:
        print(" Podaj wartość liczbową. ")

for i in range(a, b):
    if i % 2 == 0:
        print(i)
    else:
        continue




