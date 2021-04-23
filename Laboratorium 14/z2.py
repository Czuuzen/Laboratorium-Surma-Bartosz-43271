class Zwierzę:
    def __init__(self, rodzaj, gatunek, wiek, waga, ubarwienie):
        self.rodzaj = rodzaj
        self.gatunek = gatunek
        self.wiek = wiek
        self.waga = waga
        self.ubarwienie = ubarwienie
    def __del__(self):
        print("Usunięto " + self.gatunek)
    def rodzajj(self):
        print("Rodzaj zwierzęcia to: " + self.rodzaj)
    def gatunekk(self):
        print("Gatunek zwierzęcia to: " + self.gatunek)
    def wiekk(self):
        print("Wiek " + self.gatunek + " to: " + self.wiek)
    def wagaa(self):
        print("Waga " + self.gatunek + " to: " + self.waga)

class kot(Zwierzę):
    def __init__(self, gatunek, wiek, waga, ubarwienie):
        super().__init__("Kot", gatunek, wiek, waga, ubarwienie)
    def ubarwieniee(self):
        print("Odcień sierści kota to: " + self.ubarwienie)

class pies(Zwierzę):
    def __init__(self, gatunek, wiek, waga, ubarwienie):
        super().__init__("Pies", gatunek, wiek, waga, ubarwienie)
    def ubarwieniee(self):
          print("Odcień sierści psa to: " + self.ubarwienie)

class ptak(Zwierzę):
    def __init__(self, gatunek, wiek, waga, ubarwienie):
        super().__init__("Ptak", gatunek, wiek, waga, ubarwienie)
    def ubarwieniee(self):
        print("Odcień piór ptaka to: " + self.ubarwienie)

class ryba(Zwierzę):
    def __init__(self, gatunek, wiek, waga, ubarwienie):
        super().__init__("Ryba", gatunek, wiek, waga, ubarwienie)
    def ubarwieniee(self):
        print("Odcień łusek ryby to: " + self.ubarwienie)

k1 = kot("Perski", "4 lata", "4 kg", "szaro-biały")
p1 = pies("Jamnik", "2 lata", "7 kg", "brązowy")
pt1 = ptak("Papuga", "6 miesięcy", "60 g", "zielono-żółta")
r1 = ryba("Okoń", "3 miesiące", "1 kg", "ciemnoszary")

k1.rodzajj()
k1.gatunekk()
print("")
p1.wiekk()
p1.wagaa()
print("")
pt1.gatunekk()
pt1.ubarwieniee()
print("")
r1.gatunekk()
r1.ubarwieniee()
print("")