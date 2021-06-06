n = input("Wpisz wyraz aby sprawdzić czy jest on palindromem: ")
assert len(n) > 0, 'Wpisz wyraz!!!'
if n == n[::-1]:
    print(n,"to palindrom.")
else:
    print(n,"nie jest palindromem.")

x = n[::-1]
print("Wyraz wpisany:",n)
print("Wyraz wspak:",x)