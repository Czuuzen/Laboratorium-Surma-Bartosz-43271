a = input("Podaj liczbe: ")
while float(a) != 0:
    b = input("Podaj druga liczbe: ")
    if float(b) != 0:
        a = (float(a)*float(b)) / 2
        print(a)
    else: print("Wpisales zero")
    break
