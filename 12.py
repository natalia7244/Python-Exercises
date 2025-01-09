#Napisz program, który pyta użytkownika o wiek, a następnie wyświetla odpowiedni komunikat:
    #Jeśli użytkownik ma mniej niż 18 lat, wypisz: "Jesteś niepełnoletni."
    #Jeśli użytkownik ma dokładnie 18 lat, wypisz: "Masz dokładnie 18 lat!"
    #Jeśli użytkownik ma więcej niż 18 lat, wypisz: "Jesteś pełnoletni."

try:
    w = int(input("Ile masz lat?"))
    if w > 18:
        print("Jesteś pełnoletni")
    if w == 18:
        print("Masz dokładnie 18 lat")
    if w < 18 and w > 0:
        print("Nie jesteś pełnoletni")
    else:
        print("Podaj prawdziwy wiek")
except ValueError:
    print("Podaj liczbę naturalną dodatią")