# Zdefiniuj funkcję list_to_set, która usuwa z listy elementy powtarzające się.
# Zdefiniuj funkcję pomocniczą, sprawdzającą czy dany obiekt znajduje się na liście.
# Użyj rekurencji.

def element_in_list(lista, el):
    if len(lista) == 0:
        return False
    else:
        if lista[0] == el:
            return True
        else:
            return element_in_list(lista[1:], el)

def list_to_set(lista1, lista2 = []):
    if not lista1:
        return lista2
    else:
        if element_in_list(lista2, lista1[0]):
            return list_to_set(lista1[1:], lista2)
        else:
            return list_to_set(lista1[1:], lista2 + [lista1[0]])

if __name__ == "__main__":
    assert(list_to_set([1,1,1,1,1,1,1,2,3,4,4,4,48,0]) == [1,2,3,4,48,0])
