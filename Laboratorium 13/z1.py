class Samochod:
    def __init__(self, marka, rodzaj, kolor, przebieg, wartosc):
        self.marka = marka
        self.rodzaj = rodzaj
        self.kolor = kolor
        self.przebieg = przebieg
        self.wartosc = wartosc
    def __del__(self):
        print(self.marka + " usunięto")
    def jedzprosto(self):
        print("Samochód " + self.marka + " jedzie prosto")
    def cofaj(self):
        print("Samochód " + self.marka + " cofa")
    def jedzlewo(self):
        print("Samochód " + self.marka + " skręca w lewo")
    def jedzprawo(self):
        print("Samochód " + self.marka + " skręca w prawo")
    def info(self):
        print("Marka samochodu to " + self.marka + ", rodzaj to " + self.rodzaj + ", jego kolor to " + self.kolor + ", ma przebieg o wartości " + self.przebieg + " km, jego koszt to " + self.wartosc + " PLN")

a1 = Samochod("Ferrari", "kabriolet", "czerwony", "72100", "60000")
a2 = Samochod("Fiat", "sedan", "biały", "52000", "13000")
a3 = Samochod("Ford", "kombi", "niebieski", "112000", "8900")
a4 = Samochod("Nissan", "coupe", "czarny", "69420", "160000")
a5 = Samochod("Mazda", "SUV", "zielony", "20000", "38000")

a1.jedzprosto()
a2.cofaj()
a3.jedzlewo()
a4.jedzprawo()
a5.info()