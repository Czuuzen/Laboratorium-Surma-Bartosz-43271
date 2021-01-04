a = float(input("podaj liczbę: "))

if a==0:
    print("Liczba jest równa 0")
elif a<0:
    print("Liczba jest ujemna")
else:
    print("Liczba jest dodatnia")
if a!=0:
    if a%2==0:
        print("Wartość jest podzielna przez 2 bez reszty")
    else:
        print("Wartość posiada resztę z dzielenia")