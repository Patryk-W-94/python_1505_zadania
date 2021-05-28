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


def bmi(masa:int, wzrost:int):
    if isinstance(masa,int) and isinstance(wzrost, int):
        return masa / ((wzrost/100) ** 2)

def bmi_tes():
    assert bmi(79,179) == 24.65590961580475

def pole_trojkata(a:float, b:float, c:float):
    if isinstance(a,float) and isinstance(b,float) and isinstance(c, float):
        p = (a+b+c)/2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return print("Podano zla wartosc")

def pole_trojkata_test():
    assert(pole_trojkata(2.0,3.5,4.5)) == 3.3541019662496847


def ile_mil(kilometry:float):
    if isinstance(kilometry, float):
        return kilometry * 0.62
    else:
        return print("Podana bledna wartosc")

def ile_mil_test():
    assert ile_mil(100) == 62


def ile_kilometrow(mile: float):
    if isinstance(mile, float):
        return mile * 1.6
    else:
        return print("Podana bledna wartosc")


def ile_kilometrow_test():
    assert ile_kilometrow(100) == 160

print("""Kalkulator mile - kilometry. Wybierz co chcesz przeliczyc:
      mile na kilometry: wpisz 1
      kilometry na mile: wpisz 2""")
co_liczyc = int(input("Twoj wybor to: "))

if co_liczyc == 1:
    print("Podaj liczbe mil stosujac liczbe zmiennoprzecinkowa, np: 10.0 lub 12.45")
    mile = float(input("Ilosc mil: "))
    print("Podana wartosc w milach to ", ile_kilometrow(mile), "kilometrow.")
elif co_liczyc == 2:
    print("Podaj liczbe mil stosujac liczbe zmiennoprzecinkowa, np: 10.0 lub 12.45")
    kilometry = float(input("Ilosc kilometrow: "))
    print("Podana wartosc w kilometrach to ", ile_mil(kilometry), "mil.")
else:
    print("Podano bledna wartosc!")