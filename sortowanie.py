# Sortowanie

# 1a. Zdefinuj funkcję, która sortuje listę liczb - użyj rekurencji.
# Jeśli jest to potrzebne zdefiniuj funkcje pomocnicze.
def recursivesort(lista):
    if lista:
        b = lista[0]
        a = [i for i in lista[1:] if i <= b] # a zawiera ewentualne powtórki b
        c = [i for i in lista[1:] if i > b] # iteracja w mojej rekurencji? 🙅
        a2 = recursivesort(a)
        c2 = recursivesort(c)
        return a2 + [b] + c2
    else:
        return lista

# 1b. Zdefinuj funkcję, które sortuje listę liczb - użyj iteracji.
def bubblesort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                (lista[j], lista[j+1]) = (lista[j+1], lista[j])
    return lista

# 2a. Zdefiniuj funkcję, która wstawi daną liczbę w odpowiednie miejsce posortowanej listy - użyj rekurencji.
def insert_recursive(lista, el=None, res=[]):
    if lista:
        if el == None:
            return insert_recursive(lista[1:], el, res + [lista[0]])
        else:
            if el >= lista[0]:
                return insert_recursive(lista[1:], el, res + [lista[0]])
            else:
                return insert_recursive(lista[1:], None, res + [el] + [lista[0]])
    else:
        if el == None:
            return res
        else:
            return res + [el]

# 2b. Zdefiniuj funkcję, która wstawi daną liczbę w odpowiednie miejsce posortowanej listy - użyj iteracji.
def insert_iterative(lista, el):
    for i in range(len(lista)):
        if lista[i] > el:
            lista.insert(i, el)
            break
    return lista

# 3a. Zdefiniuj funkcję, która sprawdzi ile razy dany element występuje na danej liście - użyj rekurencji.
def countrec(lista, el, count=0):
    if not lista:
        return count
    else:
        return countrec(lista[1:], el, (count + 1 if lista[0] == el else count))


# 3b. Zdefiniuj funkcję, która sprawdzi ile razy dany element występuje na danej liście - użyj iteracji.
def countiter(lista, el):
    count = 0
    for item in lista:
        if item == el:
            count += 1
    return count

# 4. Trójkąt Pacala. Zdefinuj funkcję, która dostaje dwa argumenty: numer kolumny i numer wiersza,
# zwraca zaś liczbą Pascala która na danej współrzędnej występuje.
def pascalrec(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascalrec(row-1, col-1) + pascalrec(row-1, col)
#1:             1                   #1:    1
#2:            1 1                  #2:    1  1
#3:           1 2 1                 #3:    1  2   1
#4:          1 3 3 1                #4:    1  3   3   1
#5:         1 4 6 4 1               #5:    1  4   6   4   1
#6:        1 5 10. 5 1              #6:    1  5  10   5   1
#7:       1 6 15 15 6 1             #7:    1  6  15  15   6  1
#8:     1 7 21 30. 21 7 1           #8:    1  7  21  30  21  7  1

# 5. Zdefiniuj funkcję "balance", która sprawdza, czy w danym Stringu nawiasy są ustawione w prawidłowy
# sposób, tj. czy każde lewy nawias ma swój prawy nawias do pary i czy są one dobrze ustawione.
def balance(input):
    lewe = []
    prawe = []
    for znak in input:
        if znak in ['(', '[', '{']:
            lewe.append(znak)
        elif znak in [')', ']', '}']:
            prawe.append(znak)
    if len(lewe) != len(prawe):
        return False
    for i in range(len(lewe)):
        l = lewe[i]
        p = prawe[len(prawe)-1-i]
        if l == '(' and p != ')':
            return False
        if l == '[' and p != ']':
            return False
        if l == '{' and p != '}':
            return False
    return True


if __name__ == "__main__":
    assert(bubblesort([5,4,3,3,3,2,1])          == recursivesort([5,4,3,3,3,2,1])           == [1,2,3,3,3,4,5])
    assert(bubblesort([5,15,10,167,1,2,3,2,4])  == recursivesort([5,15,10,167,1,2,3,2,4])   == [1,2,2,3,4,5,10,15,167])
    assert(insert_iterative([1,2,6,7], 4)       == insert_recursive([1,2,6,7], 4)           == [1,2,4,6,7])
    assert(insert_iterative([1,2,3,4,5], 3)     == insert_recursive([1,2,3,4,5], 3)         == [1,2,3,3,4,5])
    assert(countiter([1,1,1,2,3,1], 1)          == countrec([1,1,1,2,3,1], 1)               == 4)

    assert(pascalrec(1, 1) == pascalrec(2, 1) == pascalrec(2, 2) == pascalrec(3, 1) == pascalrec(3, 3) == 1)
    assert(pascalrec(3, 2) == 2)
    assert(pascalrec(4, 2) == pascalrec(4, 3) == 3)
    assert(pascalrec(5, 2) == pascalrec(5, 4) == 4 and pascalrec(5,3) == 6)

    assert(balance("(({[([({{({[]})}})])]}))") == True)
    assert(balance("(({[([({{({({[]}))})])]}))") == False)
