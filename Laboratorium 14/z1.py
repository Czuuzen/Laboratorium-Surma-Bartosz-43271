class pojazd:
    def __init__(self, rodzaj, marka, nrtablicy, klimatyzacja):
        self.rodzaj = rodzaj
        self.marka = marka
        self.nrtablicy = nrtablicy
        self.klimatyzacja = klimatyzacja

    def __del__(self):
        print("Usunięto " + self.marka)

    def rodzai(self):
        print("Rodzaj pojazdu to " + self.rodzaj)

    def markas(self):
        print("Marka pojazdu to " + self.marka)

    def tablica(self):
        print("Nr tablicy rejstracyjnej pojazdu to " + self.nrtablicy)

    def klima(self):
        print("Czy pojazd posiada klimatyzacje: " + self.klimatyzacja)


class samochod(pojazd):
    def __init__(self, marka, nrtablicy, klimatyzacja, predkoscmax):
        super().__init__("samochod", marka, nrtablicy, klimatyzacja)
        self.predkoscmax = predkoscmax

    def predkosc(self):
        print("Prędkość maksymalna dla samochodu " + self.marka + " wynosi " + self.predkoscmax)


class motocykl(pojazd):
    def __init__(self, marka, nrtablicy, predkoscmax, klimatyzacja):
        super().__init__("motocykl", marka, nrtablicy, klimatyzacja)
        self.predkoscmax = predkoscmax

    def predkosc(self):
        print("Prędkość maksymalna dla motocyklu " + self.marka + " wynosi " + self.predkoscmax)

    def klima(self):
        print("Klimatyzacja w motocyklu? Można powiedzieć że jest...")


s1 = samochod("Ferrari", "591DS25", "klimatyzacja zainstalowana", "260km/h")
s2 = samochod("Honda", "GS42S612", "brak klimatyzacji", "180km/h")
m1 = motocykl("Kawasaki", "SD52", "250km/h", "brak")
m2 = motocykl("Yamaha", "JD69", "290km/h", "brak")

s1.rodzai()
s1.markas()
s1.tablica()
s1.klima()
s1.predkosc()
print("")
s2.rodzai()
s2.markas()
s2.tablica()
s2.klima()
s2.predkosc()
print("")
m1.rodzai()
m1.markas()
m1.tablica()
m1.klima()
m1.predkosc()
print("")
m2.rodzai()
m2.markas()
m2.tablica()
m2.klima()
m2.predkosc()
print("")
