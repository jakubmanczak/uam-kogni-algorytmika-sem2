# 1a. Zdefiniuj funkcję silnia, używając standardowej rekurencji.
def silnia_rs(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia_rs(liczba-1)

# 1b. Zdefiniuj funkcję silnia, używając rekurencji ogonowej.
def silnia_ro(liczba, temp):
    if liczba == 0:
        return temp
    else:
        return silnia_ro(liczba - 1, liczba*temp)

# 1c. Zdefiniuj funkcję silnia, używając iteracji (pętli).
def silnia_it(liczba):
    wynik = 1
    for i in range(1, liczba+1):
        wynik *= i
    return wynik

# 2a. Zdefiniuj funkcję zwracającą największy element w liście - wersja iteracyjna.
def najw_it(lista):
    najw = lista[0]
    for el in lista:
        if el > najw:
            najw = el
    return najw

# 2b. Zdefiniuj funkcję zwracającą największy element w liście - wersja rekurencyjna.
def najw_rk(lista):
    if len(lista) != 1 and najw_rk(lista[1:]) > lista[0]:
        return najw_rk(lista[1:])
    else:
        return lista[0]

# 3a. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja rekurencyjna.
def odwr_rk(lista, temp):
    if len(lista) == 0:
        return temp
    else:
        temp.insert(0, lista[0])
        return odwr_rk(lista[1:], temp)
# [1, 2, 3, 4] []
# [2, 3, 4] [1]
# [3, 4] [2, 1]
# [4] [3, 2, 1]
# [] [4, 3, 2, 1]

# 3b. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja iteracyjna.
def odwr_it(lista):
    nowa = []
    for el in lista:
        nowa.insert(0, el)
    return nowa

# 4a. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja rekurencyjna.
def konk_rk(lista, lista2):
    if not lista2:
        return lista
    else:
        lista.append(lista2[0])
        return konk_rk(lista, lista2[1:])

# 4b. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja iteracyjna.
def konk_it(lista, lista2):
    for el in lista2:
        lista.append(el)
    return lista

# 5a. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja rekurencyjna.

# 5b. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja iteracyjna.

# 6a. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja rekurencyjna.

# 6b. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja iteracyjna.

if __name__ == "__main__":
    assert(silnia_rs(5) == silnia_ro(5, 1) == silnia_it(5) == 120)
    assert(silnia_rs(4) == silnia_ro(4, 1) == silnia_it(4) ==  24)
    assert(silnia_rs(3) == silnia_ro(3, 1) == silnia_it(3) ==   6)

    assert(najw_it([0, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == najw_rk([0, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5)
    assert(najw_it([0, 1, 2, 3, 4, 5, 4, 3, 2, 7]) == najw_rk([0, 1, 2, 3, 4, 5, 4, 3, 2, 7]) == 7)
    assert(najw_it([8, 1, 2, 3, 4, 5, 4, 3, 2, 7]) == najw_rk([8, 1, 2, 3, 4, 5, 4, 3, 2, 7]) == 8)

    assert(odwr_rk([1,2,3,4], []) == odwr_it([1,2,3,4]) == [4,3,2,1])
    assert(odwr_rk([1], []) == odwr_it([1]) == [1])
    assert(odwr_rk([], []) == odwr_it([]) == [])

    assert(konk_rk([1,2,3,4], [5,6,7]) == konk_it([1,2,3,4], [5,6,7]) == [1,2,3,4,5,6,7])
