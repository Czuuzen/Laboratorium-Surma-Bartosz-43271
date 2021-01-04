import random
n = int(input("Podaj długość ciągu: "))
x = int(input("Podaj zakres min: "))
z = int(input("Podaj zakres max: "))
i = 0
j = 0
y = 0
tab = []
tabx = []
while i<n:
    a = random.randint(x, z)
    tab.append(a)
    i += 1
print(tab)
print("Trzeci od końca indeks to: ",tab[-3])
k = int(input("Podaj element do usunięcia od końca: "))
tab.pop(-k)
while j<n:
    a = random.randint(x, z)
    tab.append(a)
    j += 1
tab.extend(tabx)
tab.sort()
print("Długość tablicy: ",len(tab))
while y<len(tab):
    z = tab.count(tab[y])
    print("Liczba", tab[y] ,"powtarza się", z ,"raz/y")
    y +=z