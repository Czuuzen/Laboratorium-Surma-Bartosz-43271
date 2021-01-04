import random
tab = []
tab2 = []
tab3 = []
num0 = 0
num1 = 0

for i in range(0, 100):
    tab.append(random.randint(0, 10))

tup_1 = tuple(tab)
print(tup_1)
print("0 jest: ", tup_1.count(0))
print("1 jest: ", tup_1.count(1))
print("2 jest: ", tup_1.count(2))

for i in tup_1:
    if i % 2 == 0:
        tab2.append(i)
    else:
        tab3.append(i)
for i in tup_1:
    if i == 0:
        num0 +=1
    elif i == 1:
        num1 += 1
print("Ilość 0:", num0)
print("Ilość 1:", num1)
print("Parzyste: ", tab2)
print("Nieparzyste: ", tab3)