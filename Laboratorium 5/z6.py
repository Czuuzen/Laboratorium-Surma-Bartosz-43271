import random
n = random.randint(1, 100)
x = 0
i = 0
print("Zgadnij liczbę z zakresu 1-100!")
while x != n and i < 3:
    x = int(input("Podaj liczbę: "))
    if x == n:
        print("Gratulacje Wygrałeś! Twoją liczbą była: ", n)
    else:
        if x > 100 or x < 1:
            print("Liczba poza zakresem!")
        if x > n:
            print("Twoja liczba jest za duża!")
            i += 1
        if n > x:
            print("Twoja liczba jest za mała!")
            i += 1
        if i == 3:
            print("GAME OVER Liczba do odgadnięcia to: ", n)