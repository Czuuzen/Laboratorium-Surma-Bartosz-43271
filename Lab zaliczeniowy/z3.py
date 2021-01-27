def inp(x):
    if len(x) == 0:
        return True
    else:
        return False

def pytanie(x, y):
    global pkt
    if inp(x) is True:
        pkt += 0
    elif (x).lower() in (y):
        pkt += 1
    return 0

wybor = input("Dzień dobry uczniu! Czy chcesz rozpocząć test z wiedzy informatycznej?(Tak): ")
if inp(wybor) is True:
    print("Przerwałeś test")
else:
    if wybor.lower() in ('tak'):
        pkt = 0

        print("Jaki jest najlepszy język programowania?")
        print("A) Java")
        print("B) PHP")
        print("C) Python")
        print("D) C#")
        pyt1 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt1, "c")
        print()

        print("Który z programów jest programem graficznym?")
        print("A) MS Excel")
        print("B) Paint")
        print("C) Kalkulator")
        print("D) Notepad")
        pyt2 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt2, "b")
        print()

        print("WAV to format plików:")
        print("A) Dokumentu")
        print("B) Prezentacji")
        print("C) Dźwięku")
        print("D) Grafiki")
        pyt3 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt3, "c")
        print()

        print("Popularny arkusz kalkulacyjny to:")
        print("A) MS Excel")
        print("B) MS Word")
        print("C) MS PowerPoint")
        print("D) MS Outlook")
        pyt4 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt4, "a")
        print()

        print("Urządzeniem wejścia jest/są:")
        print("A) Monitor")
        print("B) Głośniki")
        print("C) Słuchawki")
        print("D) Klawiatura")
        pyt5 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt5, "d")
        print()

        print("Co oznacza skrót HDD?")
        print("A) Karte graficzną")
        print("B) Pamięć procesora")
        print("C) Dysk twardy")
        print("D) Oprogramowanie komputerowe")
        pyt6 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt6, "c")
        print()

        print("Mózgiem komputera jest:")
        print("A) Procesor")
        print("B) Zasilacz")
        print("C) Pamięć RAM")
        print("D) Dysk twardy")
        pyt7 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt7, "a")
        print()

        print("Linux to:")
        print("A) Hardware")
        print("B) System operacyjny")
        print("C) Gra wideo")
        print("D) Antywirus")
        pyt8 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt8, "b")
        print()

        print("Sieć lokalna to inaczej:")
        print("A) WAN")
        print("B) LAN")
        print("C) MAN")
        print("D) PAN")
        pyt9 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt9, "b")
        print()

        print("Z ilu warstw składa się model ISO/OSI?")
        print("A) Trzech")
        print("B) Pięciu")
        print("C) Siedmiu")
        print("D) Dziewięciu")
        pyt10 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt10, "c")
        print()

        if pkt > 4 or pkt == 0:
            print("Otrzymałes: ", pkt, "punktów")
        elif pkt >= 2:
            print("Otrzymałes: ", pkt, "punkty")
        elif pkt >= 1:
            print("Otrzymałes: ", pkt, "punkt")

        if pkt == 10:
            print("Jesteś najlepszy! Ocena celująca (100%)")
        elif pkt >=9:
            print("Gratulacje! Ocena bardzo dobra (90% - 99%)")
        elif pkt >=7:
            print("Nieźle Ci poszło! Ocena dobra (70% - 89%)")
        elif pkt >=5:
            print("Stać Cię na więcej! Ocena dostateczna (50% - 69%)")
        elif pkt >=3:
            print("Strzelałeś? Ocena dopuszczająca (30% - 49%)")
        else:
            print("Nie udało się! Ocena niedostateczna (<30%)")
    else:
        print("Przerwałeś test")