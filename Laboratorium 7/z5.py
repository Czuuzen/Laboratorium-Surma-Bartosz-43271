tup1 = ("u", "ż", "y", "t", "k", "o", "w", "a", "n", "i", "e", "m")
tup2 = ("n", "i", "e", "ż", "u", "k", "o", "w", "a", "t", "y", "m")
x = sorted(tup1)
y = sorted(tup2)
if x == y:  #join po to żeby się wyrazy z tupli normalnie wyświetlały
    print("Wyrazy ", "".join([str(i[0]) for i in tup1]), " i ", "".join([str(i[0]) for i in tup2]), " są anagramami.")
else:
    print("Wyrazy ", "".join([str(i[0]) for i in tup1]), " i ", "".join([str(i[0]) for i in tup2]), " nie są anagramami.")