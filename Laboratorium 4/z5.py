suma= 0
j = 0
while True:
    i = input("Podaj liczbę")
    suma = int(i) + int(suma)
    j += 1
    if suma > 100:
        break
    else:
        continue