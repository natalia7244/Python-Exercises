# Napisz program proszący użytkownika o podanie dwóch liczb a i b i wypisujący ich sumę, różnicę, iloczyn,
# iloraz, √a + b oraz ab i ba.

while True:
    try:
        a = int(input("Podaj liczbę: "))
        b = int(input("Podaj liczbę: "))
        print(a+b)
        print(a-b)
        print(a*b)
        print(a-b)
        print(a/b)
        print((a+b) ** 0.5)
        print(a ** b)
        print(b ** a)
        break
    except ValueError:
        print("Podaj wartość liczbową. ")
