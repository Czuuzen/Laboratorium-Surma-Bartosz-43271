import random
i = 0
z = 0
inty = 0
floaty = 0
n = random.randint(1, 10)
print('Podaj ', n,' liczb')
while i < n:
    x = float(input("Podaj liczbę całkowitą, nieujemną"))
    if x.is_integer():
        inty += 1
    else:
        floaty += 1
    z = z + x
    i += 1
    if x < 0:
            print('Liczba ujemna! Średnia nie zmienia się')
            continue
print('Średnia podanych liczb wynosi: ', z/i)
print('Podałeś ', floaty,' floatów i ', inty,' intów')
