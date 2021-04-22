class smartfon:
    def __init__(self, marka, rokprodukcji, pojemnosc, wartosc):
        self.marka = marka
        self.rokprodukcji = rokprodukcji
        self.pojemnosc = pojemnosc
        self.wartosc = wartosc
    def __del__(self):
        print(self.marka + " usunięto")

    def uruchom(self):
        print("Smartfon " + self.marka + " uruchamia się")
    def wylacz(self):
        print("Smartfon " + self.marka + " wyłącza się")
    def restart(self):
        print("Smartfon " + self.marka + " restartuje się")
    def informacje(self):
        print("Smartfon to " + self.marka + " został wydany w " + self.rokprodukcji + " ma pojemność " + self.pojemnosc, "GB jego cena wynosi " + self.wartosc + " PLN")

s1 = smartfon("Huehuewei", "2019", "32", "1600")
s2 = smartfon("Xajomi", "2018", "64", "1400")
s3 = smartfon("Samsung", "2020", "256", "2800")
s4 = smartfon("AJPhon", "2021", "8", "16000")

s1.uruchom()
s2.wylacz()
s3.restart()
s4.informacje()