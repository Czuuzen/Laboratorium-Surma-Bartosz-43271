tekst = open("pan tadzio.txt", encoding="UTF-8").readlines()
linijki = [8, 12, 60, 98, 104]
for a, b in enumerate(tekst):
    if a in linijki:
        print(b)
#działa jakoś?
count = len(open("pan tadzio.txt", encoding="UTF-8").readlines())
print("Ilość wierszy: ", count)