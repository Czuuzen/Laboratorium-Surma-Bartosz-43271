import random

a = []
b = []
los = []

for c in range(6):
    a.append(input("Podaj 6 cyfr"))
for d in range(6):
    x = random.randint(0,99)
    b.append(x)

a.sort()
b.sort()
b2 = 0
a2 = 0
for sib in range(6):
    if a[a2] == b[b2]:
        a2 += 1
        b2 += 1
    else:
        continue
if a2 == 6:
    print("Wygrałeś 10 milonów")
elif a2 == 5:
    print("Wygrałeś półmiliona")
elif a2== 4:
    print("Wygrałeś 10 tysięcy")
elif a2 ==3:
    print("Wygrałeś 100zł")
else:
    print("Nic nie wygrałeś")

print("Liczba trafionych liczb")
print(a2)
print(a)
print(b)

if a == b:
    print("Wygrałeś jestes milionerem")
else:
    print("Maybe next time")