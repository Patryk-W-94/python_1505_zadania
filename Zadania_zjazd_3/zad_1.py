'''Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).

Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.'''

class Ogloszenie:
    def __init__(self, produkt, cena, typ, email, tele):
        self.produkt = produkt
        self.cena = cena
        self.typ = typ
        self.email = email
        self.tele = tele
    def __str__(self):
        return f'{self.ogloszenie(self.produkt, self.cena, self.typ, self.email, self.tele)}'
    def ogloszenie(self, produkt, cena, typ, email, tele):
        if typ == 1:
            return print(f'''       Kupie {produkt}
    Szukam osoby chcacej odsprzedac {produkt}.
    Osobe chetna do zawarcia transakcji zapraszam do kontaktu.
        Nr tel : {tele}
        email : {email}''')
        elif typ == 2:
            return print(f'''           "Sprzedam {produkt}"
        Chcialbym sprzedac {produkt}.
        Cena za niego wynosi {cena}.
        Po wiecej informacji zapraszam do kontaktu:
            Nr tel : {tele}
            email : {email}''')
        else:
            print("Bledny typ")

print(Ogloszenie("Kanapka", 200, 1,"Kurwitrax500@olx.tja", "500 600 700"))



