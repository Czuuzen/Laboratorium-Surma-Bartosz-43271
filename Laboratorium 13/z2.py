from operator import attrgetter
class Ksiazka:
    def __init__(self, tytul, rodzaj, wydawnictwo, autor, wartosc):
        self.tytul = tytul
        self.rodzaj = rodzaj
        self.wydawnictwo = wydawnictwo
        self.autor = autor
        self.wartosc = wartosc
    def __del__(self):
        print(self.tytul + " usunięto")
    def __repr__(self):
        return '({}, {})'.format(self.tytul, self.wartosc)

    def czytaj(self):
        print("Czytasz książke " + self.tytul + " której autorem jest " + self.autor)
    def zakup(self):
        print("Kupujesz książke " +self.tytul + " która kosztuje " + self.wartosc + " PLN")
    def zakupaudio(self):
        print("Kupujesz audiobooka " + self.tytul + " który kosztuje " + self.wartosc + " PLN")
    def rzut(self):
        print("Rzucasz " + self.tytul + " w kąt i nie czytasz jej więcej")
    def info(self):
        print("Tytuł książki to " + self.tytul + ", autor to " + self.autor + ", rodzaj książki to " + self.rodzaj + ", wydawnictwo to " + self.wydawnictwo + ", a jej koszt to " + self.wartosc + " PLN")

a1 = Ksiazka("Garry Porter", "Fantasy", "Pod dzewem", "J.F.K. Rolling", "21")
a2 = Ksiazka("Władca Pierścieniów", "Biografia", "Na drzewie", "R.J.J. Talkien", "32")
a3 = Ksiazka("49 Szarych twarzy", "Psychologiczna", "W drzewie", "L.J. Jones", "49")
a4 = Ksiazka("Fizyka dla szkół wyższych", "Horror fiction", "Otchłań", "anonim", "66,6")
a5 = Ksiazka("Unser Gulag", "Komedia romantyczna", "Polskie Państwo Podziemne", "Józef Stalin", "35")

a1.czytaj()
a2.zakup()
a3.zakupaudio()
a4.rzut()
a5.info()

ksiazki=[a1, a2, a3, a4, a5]
print(sorted(ksiazki, key= attrgetter('wartosc')))
