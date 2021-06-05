'''Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).

Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.'''

class Ogloszenie():
    def __init__(self, przedmiot, cena):
        self.przedmiot = przedmiot
        self.cena = cena

        self.forma = input("""Jakie ogloszenie chcesz wystawic?
                 1 - Kupna 
                 2- Sprzedazy: """)

        self.email = input("Podaj email")
        self.telefon = input("Podaj nr telefonu")

    def print_info(self):
        print(self.get_info())

    def get_info(self):
        return f'{self.tytul(self.przedmiot, self.forma)} + {self.opis(self.forma, self.cena, self.forma, self.telefon, self.email)}'
    def __str__(self):
        return f'{self.get_info()}'


    def tytul(self, przedmiot, forma):
        if forma == 1:
            return print(f"Kupie {przedmiot}")
        elif forma == 2:
            return print(f"Sprzedam {przedmiot}")
        if not isinstance(przedmiot, str):
            raise TypeError("Zla nazwa przedmiotu")

    def opis(self, przedmiot, cena, forma, telefon, email):

        if not isinstance(przedmiot, str) or not isinstance(cena, float):
            raise TypeError('Zly typ')
        if forma == 1:
            return f'''Chcialbym kupic {przedmiot}. Cena jaka moge zaoferowac za w/w przedmiot wynosi {cena} zl.
                Chetnych na zawarcie transakcji zapraszam do kontaktu na  dane kontaktowe - tel : {telefon}, email : {email}.'''
        elif forma == 2:
            return f'''Chcialbym sprzedac {przedmiot}. Cena za dany przedmiot wynosi {cena} zl.
                Chetnych lub po wiecej informacji zapraszam do kontaktu nadane kontaktowe tel : {telefon}, email : {email} .'''


print(Ogloszenie(przedmiot="kupa", cena=10.0))
