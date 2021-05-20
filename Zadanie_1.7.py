produkt = input("Co chcesz kupic?: ")
cena = float(input("Jaka jest cena tego produktu za 1 kg? : "))
ilosc = float(input("Ile kg chcesz kupic?"))
print(f"Za {produkt} w takiej ilosci zaplacisz :", cena * ilosc, "zl")