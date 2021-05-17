
cena_ziemniakow = int(input("Podaj cene za kilo ziemniakow: "))
print("cena za 5 kilo wynosi", cena_ziemniakow * 5, "zl")

cena_ziemniakow2 = float(input("Podaj cene za kilo ziemniakow:"))
ilosc = float(input("Ile kilo chcesz kupic?: "))
Do_zaplaty = cena_ziemniakow2 * ilosc
print(f"Do zaplaty : {Do_zaplaty} zl")


cena_ziemniakow3 = float(input("Podaj cene ziemniakow za kilo: "))
cena_bananow = float(input("Podaj cene za kilo bananow"))
ilosc_ziemniakow = float(input("Ile kilo ziemniakow chcesz kupic?: "))
ilosc_bananow = float(input("Ile kilo bananow chcesz kupic?: "))
za_banany = cena_bananow * ilosc_bananow
za_ziemniaki = ilosc_ziemniakow * cena_ziemniakow3
print("Kwota do zaplaty wynosi : ", za_ziemniaki + za_banany, "zl")
if za_banany > za_ziemniaki:
    print("Wiecej bedzie trzeba zaplacic za banany")
elif za_banany < za_ziemniaki:
    print("Wiecej bedzie trzeba zaplacic za ziemniaki")
else:
    print("Tyle samo zaplacisz za banany i za ziemniaki")