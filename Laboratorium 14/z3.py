class Figura:
    def __init__(self, nazwa):
        self.nazwa = nazwa

class kwadrat(Figura):
    def __init__(self, a):
        super().__init__(a)
        self.a = a
        self.o = 4*a
        self.p = a*a

    def obwodk(self,):
        print("Obwód kwadratu to:", self.o)

    def polek(self):
        print("Pole kwadratu to:" , self.p)

class prostokat(Figura):
    def __init__(self, a, b):
        super().__init__(a)
        self.a = a
        self.o = (2 * a) + (2 * b)
        self.p = a * b

    def obwodp(self, ):
        print("Obwód prostokąta to:", self.o)

    def polep(self):
        print("Pole prostokąta to:", self.p)

class trojkat(Figura):
    def __init__(self, a, b, c, h):
        super().__init__(a)
        self.a = a
        self.o = a + b + c
        self.p = a * h

    def obwodt(self, ):
        print("Obwód kwadratu to:", self.o)

    def polet(self):
        print("Pole kwadratu to:", self.p)

class kolo(Figura):
    def __init__(self, r):
        super().__init__(r)
        self.r = r
        self.o = 2 * r * 3.14
        self.p = r * r * 3.14

    def obwodko(self, ):
        print("Obwód koła to:", self.o)

    def poleko(self):
        print("Pole koła to:", self.p)

class romb(Figura):
    def __init__(self, a, h):
        super().__init__(a)
        self.a = a
        self.o = 4 * a
        self.p = a * h

    def obwodr(self, ):
        print("Obwód rombu to:", self.o)

    def poler(self):
        print("Pole rombu to:", self.p)

class trapez(Figura):
    def __init__(self, a, b, c, d, h):
        super().__init__(a)
        self.a = a
        self.o = a + b + c + d
        self.p = ((a + b) / 2) * h

    def obwodtra(self, ):
        print("Obwód kwadratu to:", self.o)

    def poletra(self):
        print("Pole kwadratu to:", self.p)

k1 = kwadrat(2)
p1 = prostokat(2, 4)
t1 = trojkat(3, 4, 5, 3)
ko1 = kolo(3)
r1 = romb(2, 3)
tr1 = trapez(8, 4, 3, 6, 4)

k1.obwodk()
k1.polek()
print("")
p1.obwodp()
p1.polep()
print("")
t1.obwodt()
t1.polet()
print("")
ko1.obwodko()
ko1.poleko()
print("")
r1.obwodr()
r1.poler()
print("")
tr1.obwodtra()
tr1.poletra()