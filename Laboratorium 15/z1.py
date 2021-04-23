class Restaurant:
    def __init__(self, sklep):
        self.sklep = sklep
    def sklepp(self):
        print("Witaj w " + self.sklep)

class IceCreamStand(Restaurant):
    flavors = ["Śmietankowy", "Kokosowy", "Truskawkowy", "Jagodowy", "Jogurt", "Miętowy", "Guma balonowa"]
    def __init__(self):
        super().__init__("stoisku z lodami")
    def __str__(self):
        return '({},)'.format(self.flavors)
    def smaki(self):
        print("Dostępne smaki lodów:")
        print(IceCreamStand.flavors)

class CoffeeShop(Restaurant):
    coffee = ["Latte", "Americano", "Cappuccino", "Mocha", "Romano", "Caffe Latte"]
    def __init__(self):
        super().__init__("stoisku z kawą")
    def __str__(self):
        return '({},)'.format(self.coffee)
    def smaki(self):
        print("Dostępne rodzaje kawy:")
        print(CoffeeShop.coffee)

print("Witaj w restauracji, gdzie chcesz się udać?")
print("(1)Stoisko z lodami")
print("(2)Stoisko z kawą")
stoisko = input("Wybierz stoisko: ")
if stoisko == "1":
    IceCreamStand().sklepp()
    IceCreamStand().smaki()
    rodzaj = input("Jaki smak wybierasz?: ")
    if rodzaj in IceCreamStand().flavors:
        print("Przygotowywujemy twoje zamówienie!")
    else:
        print("Wybrałeś niepoprawną opcje")
elif stoisko == "2":
    CoffeeShop().sklepp()
    CoffeeShop().smaki()
    rodzaj = input("Jaki rodzaj wybierasz?: ")
    if rodzaj in CoffeeShop().coffee:
        print("Przygotowywujemy twoje zamówienie!")
    else:
        print("Wybrałeś niepoprawną opcje")
else:
    print("Wybrałeś niepoprawną opcje")