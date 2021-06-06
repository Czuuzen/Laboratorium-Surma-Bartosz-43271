waga = int(input("Wprowadź wagę: "))
wzrost = int(input("Wprowadź wzrost: "))
wiek = int(input("Wprowadź wiek: "))
plec = str(input("Wybierz płeć (M/K): "))

assert plec == "M" or plec =="K", "Wybierz poprawnie płeć"

if plec =="M":
    bmr = round(66 + (13.7 * waga) + (5 * wzrost) - (6.76 * wiek))
else:
    bmr = round(655 + (9.6 * waga) + (1.8 * wzrost) - (4.7 * wiek))

print("BMR to: ", bmr)