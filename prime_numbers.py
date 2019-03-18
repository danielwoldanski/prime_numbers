print("Program sprawdzi czy istnieją liczby pierwsze mniejsze od podanej przez użytkownika")

y = int(input("Podaj liczbę: "))

lista = list(range(2,y+1))
i = y - 1

while y>1:
    while i>1:
        wynik = y/i            # Or you can use: wynik = y % i     ##
        if wynik in lista:     # if wynik == 0:                    ##
            lista.remove(y)
            break
        i -= 1
    y -= 1
    i = y - 1
print("Oto lista liczb pierwszych mniejszych od podanej:")
print(lista)
