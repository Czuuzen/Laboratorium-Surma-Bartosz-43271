tab = []
print("Lista zawiera 5 el.")
for i in range(0, 5):
    a = int(input("Podaj liczbę z zakresu (0-10) dla tab1: "))
    if 0 <= a <= 10:
        tab.append(a)
        i += 1
    else:
        a = int(input("Musi być liczba z przedziału (0 - 10): "))
        tab.append(a)
        continue
print(tab)
x = max(tab)
print("liczba max z tej listy to", x)
print("występuje", tab.count(x), "razy")