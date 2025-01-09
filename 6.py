#Napisz program, który wypisuje wszystkie liczby Catalana mniejsze od miliona i podaje, ile jest wśród nich
#liczb parzystych i nieparzystych. Uwaga na kolejność instrukcji w pętli - może mieć znaczenie

lista = [1]
listaP = []
listaNP = []

i = 0
i = 1

while x < 1000000:
    x1 = ((4*i+2)/(i+2))*x
    if x1 < 1000000:
        if int(x1) % 2 == 0:
            listaP.append(x1)
        elif int(x1) % 2 != 0:
            listaNP.append(x1)
        lista.append(x1)
    else:
        break
    x = x1
    i = i + 1
    continue

print(lista)
print(len(lista))
print(listaP)
print(listaNP)