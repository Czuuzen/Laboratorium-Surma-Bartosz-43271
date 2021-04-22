class student:
    def __init__(self, imie, nazwisko, wiek, sredniaocen, zaliczenie, stan):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.sredniaocen = sredniaocen
        self.zaliczenie = zaliczenie
        self.stan = stan
    def __del__(self):
        print(self.imie + " usunięto")

    def kto(self):
        print("Student to: " + self.imie + " " + self.nazwisko + " ma " + self.wiek + " lat")
    def oceny(self):
        print("Średnia ocen dla " + self.imie + " " + self.nazwisko + " to " + self.sredniaocen)
    def zaliczeniesemestru(self):
        print("Czy " + self.imie + " " + self.nazwisko + " zaliczy semestr: " + self.zaliczenie)
    def umysł(self):
        print("Obecny stan studenta " + self.imie + " " + self.nazwisko + " to: " +self.stan)

s1 = student("Adam", "Nowak", "21", "4", "tak", "depresja")
s2 = student("Jacek", "Kowalski", "22", "3", "tak", "depresja")
s3 = student("Tomasz", "Koń", "22", "2", "nie", "depresja")
s4 = student("Jarosław", "Polskezbaw", "69", "6", "tak", "depresja")

s1.kto()
s2.oceny()
s3.zaliczeniesemestru()
s4.umysł()

