import math
print ("Równanie kwadratowe : y = ax2 + bx + c")
a = int(input("Podaj wspolczynnik rowniania a: "))
b = int(input("Podaj wspolczynnik rowniania b: "))
c = int(input("Podaj wspolczynnik rowniania c: "))

delta = (b * b) - (4 * a * c)

print("Delta z równania wynosi : " , delta)

if delta > 0 :
    x1 = -b - math.sqrt(delta) / (2 * a)
    x2 = -b + math.sqrt(delta) / (2 * a)

    print("Pierwsze miejsce zerowe funkcji : x1 = ", x1)

    print("Drugie miejsce zerowe funkcji : x2 = ", x2)


else:
    if delta == 0:
        x = -b / (2 * a)
        print("Miejsce zerowe funkcji : x = ", x)

    else:
        print("Brak miejsc zerowych, delta mniejsza od 0 ")