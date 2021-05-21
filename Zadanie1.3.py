waga = float(input("Podaj swoja wage w kg: "))
wzrost = float(input("Podaj swoj wzrost w metrach"))
bmi = waga / (wzrost ** 2)
if bmi < 16:
    print("Twoja kategoria to wyglodzenie, zalecane zwiekszenie spozycia kalorii")
elif 16 <= bmi <= 16.99:
    print("Twoja kategoria to wychudzenie, zalecane zwiekszenie spozycia kalorii")
elif 16.99 < bmi <= 18.49:
    print("Twoja kategoria to niedowaga, zalecane zwiekszenie spozycia kalorii")
elif 18.49 < bmi <= 24.99:
    print("Jestes w optymalnej kategorii wagowej!")
elif 25 < bmi <= 29.99:
    print("Twoja kategoria to nadwaga, zalecana zmiana diety")
elif 29.99 < bmi <= 34.99:
    print("Twoja kategoria wagowa to otylosc I stopnia, zalecana zmiana diety")
elif 34.99 < bmi <= 39.99:
    print("Twoja kategoria wagowa to otylosc II stopnia, zalecana zmiana diety, wysokie ryzyko chorob!")
elif bmi > 39.99:
    print("Twoja kategoria wagowa to otylosc III stopnia, zalecana konsultacja z dietetykiem, bardzo wysokie ryzyko chorob!!)")

