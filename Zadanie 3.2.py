#Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.

#Logikę obliczania liczby dni wydziel do osobnej funkcji.

#**Wersja A**
#Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

#**Wersja B (trudniejsza)**
#Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.
import calendar
month = input("Podaj miesiac: ")
def ile_dni(miesiac:str):
    if miesiac.lower() == "styczen" or miesiac == "marzec" or miesiac == "maj" or miesiac == "lipiec" or miesiac == "sierpien" or miesiac == "pazdziernik" or miesiac == "grudzien":
        return print(f"Miesiac {miesiac} ma 31 dni")
    elif miesiac == "kwiecien" or miesiac == "czerwiec" or miesiac == "wrzesien" or miesiac == "listopad":
        return print(f"Miesiac {miesiac} ma 30 dni")
    elif miesiac == "luty":
        rok = int(input("Wpisz rok"))
        if calendar.isleap(rok) is True:
            return print(f"Miesiac {miesiac} ma 29 dni")
        else:
            return print(f"Miesiac {miesiac} ma 28 dni")

print (ile_dni(month))
