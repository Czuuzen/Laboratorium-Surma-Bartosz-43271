a = int(input("podaj 1 liczbę: "))
b = int(input("podaj 2 liczbę: "))
c = int(input("podaj 3 liczbę: "))

if a==b==c:
    print("Liczby są identyczne")
elif a>=b:
    if a==b & a>c:
        print("Liczby A i B są sobie równe i są największe")
    elif a>c:
        print("Liczba A jest największa")
elif b>=c:
    if b==c:
        print("Liczby B i C są sobie równe i są największe")
    else:
        print("Liczba B jest największa")
else:
    print("Liczba C jest największa") #ni działa