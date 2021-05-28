''' Zadanie 3.1 Funkcje liczbowe
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.'''
import math
def stopy_na_metry (ilosc):
    dystans = ilosc * 0.30480
    return dystans

def test_stopy_na_metry():
    assert stopy_na_metry(10) == 3.0480

def maximum(liczba_1:float, liczba_2:float):
    if isinstance (liczba_1, float) and isinstance(liczba_2, float):
        if liczba_1 > liczba_2:
            return liczba_1
        elif liczba_2 > liczba_1:
            return liczba_2
        elif liczba_1 == liczba_2:
            return liczba_1
    else:
        return print("Podales bledne dane")


def test_maximum():
    assert test_maximum(10,10) == 10


def srednia(liczba1: float, liczba2 : float):
    if isinstance(liczba1, float) and isinstance(liczba2, float):
        return (liczba1 + liczba2) / 2
    else:
        return print("Podales bledne wartosci")

def srednia_test():
    assert srednia(2,4) == 3


def pole_kola(promien:int):
    if isinstance(promien,int):
        return math.pi * (promien ** 2)
    else:
        return print("Podales bledna wartosc!")

def pole_kola_test():
    assert pole_kola(6) == 113.09733552923255