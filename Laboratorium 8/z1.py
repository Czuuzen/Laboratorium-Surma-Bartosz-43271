menu = {
    "pizza Margarita" : 18.50,
    "pizza peperoni" : 20.50,
    "pizza wegetarianska" : 23.50,
    "pizza wiejska" : 26.50,
    "pizza z szynkom" : 21.50,
    "pizza diablo" : 26.50,
    "pizza cztery sery" : 25.50,
}
print("Menu")
for danie, cena in menu.items():
    print(danie, cena)
max = max(menu, key=menu.get)
min = min(menu, key=menu.get)

print(max)
print(min)

del menu[max]
del menu[min]

print(menu)

a = (input("Podaj nazwę nowej pizzy: "))
b = (input("Podaj cenę nowej pizzy: "))

menu[a] = b
print("Nowe Menu")
for danie, cena in menu.items():
    print(danie, cena)