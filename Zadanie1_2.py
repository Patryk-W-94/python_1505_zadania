print("Dni tygodnia : poniedzialek, wtorek, sroda, czwartek, piatek, sobota, niedziela")
dni_tygodnia = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
oddanie = input("W jaki dzien tygodnia oddales buty?: ").lower()
czas_naprawy = int(input("Ile dni potrwa naprawa?"))
if oddanie in dni_tygodnia:
    dzien_oddania = int(dni_tygodnia.index(oddanie))
    if (dzien_oddania + czas_naprawy) < 7:
        zwrot = dni_tygodnia[int(dzien_oddania + czas_naprawy)]
        print(f"Dzien zwrotu butow wypada w {zwrot}")
    elif dzien_oddania + czas_naprawy == 7:
        zwrot = dni_tygodnia[(int(dzien_oddania+czas_naprawy)-7)]
        print(f"Dzien oddania butow wypada w {zwrot}")
    elif dzien_oddania + czas_naprawy > 7:
        zwrot = dni_tygodnia[int(dzien_oddania + (czas_naprawy % 7))]
        print(f"Dzien oddania butow wypada w {zwrot}")
else:
        print("Wpisales zly dzien tygodnia!")


