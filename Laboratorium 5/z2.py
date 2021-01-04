x = int(input("Podaj liczbę całkowitą"))
n = int(input("Podaj liczbę całkowitą"))
z = x
y = n
s = 0
i = 0
while x - n >= 5 or n - x >= 5:
    if x < n and i <6:
        print(z)
        i += 1
        s += z
        z += 1
    else:
        if x > n and i <6:
            print(y)
            i += 1
            s += y
            y += 1
        else:
            if x < n:
                print("Wartość minimalna: ", x,", wartość maksymalna: ", x + 5,"Średnia: ", s / 6, "Mediana : ", (x + x + 5)/2)
            else:
                if x > n:
                    print("Wartość minimalna: ", n, ", wartość maksymalna: ", n + 5,"Średnia: ", s / 6, "Mediana : ", (n + n + 5)/2)
            break

