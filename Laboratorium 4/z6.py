num = float(input("Podaja liczbe"))
i = 0
suma = 0
while num % 2 == 0 or num % 3 == 0:
    i += 1
    if num % i == 0:
        if i == num:
            break
        suma += i
        print(suma)
    else:
        if i == num:
            break
        continue