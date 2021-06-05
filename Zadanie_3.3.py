'''Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```

- `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma'''
import pytest
liczbyy = [2, 4, 6,10, 50.25, 37.12,[30,50], 8, "radom"]
def suma(liczby:list):
    suma2 = 0
    for i in liczby:
        if isinstance(i, int) or isinstance(i, float):
            suma2 += i
        else:
            continue
    return suma2

print(suma(liczbyy))

liczbyy1 = [2,4,6.0]

def srednia(liczby:list):
    suma2 = 0
    for i in liczby:
        if isinstance(i,int) or isinstance(i, float):
            suma2 += i
        else:
            continue
    if len(liczby) > 0:
        return suma2 / len(liczby)
    else: return print("Twoja lista jest pusta")

print(srednia(liczbyy1))

def maks(lista:list):
    maximum = 0
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            if i > maximum:
                maximum = i
    return maximum

print(maks(liczbyy))


x = [4.0, 2, 4, 8, 10]


def roznica_min_max(lista:list):
    maximum = 0
    minimum = lista[0]
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            if i > maximum:
                maximum = i
        else:
            print("Bledne dane")
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            if i < minimum:
                minimum = i
        else:
            print("Bledne dane")

    return maximum - minimum


print(roznica_min_max(x))

def wieksze_niz_x(lista:list, x:float):
    wieksze = []
    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            if i > x:
                wieksze.append(i)
            else:
                continue
    return wieksze
print(wieksze_niz_x(liczbyy,7.0))

def pierwsza_wieksza(lista:list, x:float):
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            if i > x:
                return i
            else:
                print("nie ma w tej liscie liczby wiekszej niz podana")

print(pierwsza_wieksza(liczbyy, 10))

def pierwsza_wieksza_test():
    assert pierwsza_wieksza([20, 40, 50.25, 40, 90], 50) == 50.25

def suma_wiekszych(lista:list, x):
    wieksze = []
    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            if i > x:
                wieksze.append(i)
            else:
                continue
    return sum(wieksze)

def suma_wiekszych_test():
    assert suma_wiekszych([10, 20, 50, 70, 90.0], 50.0) == 160.0

def ile_wiekszych(lista:list, x):
    wieksze = []
    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            if i > x:
                wieksze.append(i)
            else:
                continue
    return len(wieksze)
def ile_wiekszych_test():
    assert ile_wiekszych([4,5,6,7,8,9,10,2,3,4], 5) == 5

def podzielne_przez(lista:list, x):
    podzielne = []
    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            if i % x == 0:
                podzielne.append(i)
            else:
                continue
    return podzielne
def podzielne_przez_test():
    assert podzielne_przez([25,50,15,27,18], 5) == [25,50,15]

def pierwsza_podzielna(lista, x):
    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            if i % x == 0:
                return i
            else:
                continue

def pierwsza_podzielna_test():
    assert pierwsza_podzielna([], 5) == None

def znajdz_wspolny(lista1, lista2):
    lista3 = lista1 + lista2
    wspolne = []
    for i in lista3:
        if isinstance(i, int) or isinstance(i, float):
            if i in lista1 and i in lista2:
                if i not in wspolne:
                    wspolne.append(i)
            else:
                continue
    if len(wspolne)== 0:
        return None
    else:
        return wspolne
def znajdz_wspolny_test():
    assert znajdz_wspolny([2,4,5,5.5,"fresh"],[5.5, 17.25,2,"komputer"]) == [2, 5.5]

    print(znajdz_wspolny([2,4],[5,6]))