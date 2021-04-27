import sqlite3
con = sqlite3.connect("Workers")
con.row_factory = sqlite3.Row

cur = con.cursor()

def tabela():
    cur.executescript("""
    DROP TABLE IF EXISTS pracownicy;
    CREATE TABLE IF NOT EXISTS pracownicy (
    id INTEGER PRIMARY KEY ASC,
    imie varchar(250) NOT NULL,
    nazwisko varchar(250) NOT NULL,
    miejscowosc varchar(250) NOT NULL,
    zarobki INTEGER NOT NULL
)""")

def wyswietl():
    with con:
        cur.execute('SELECT * FROM pracownicy')
        wynik_prac=cur.fetchall()
        print('\nPracownicy:')
        for x in wynik_prac:
            print(x['id'],x['imie'],x['nazwisko'],x['miejscowosc'],x['zarobki'])


def wyswietlsort():
    with con:
        cur.execute('SELECT * FROM pracownicy ORDER BY imie ASC')
        wynik_prac = cur.fetchall()
        print('\nPracownicy:')
        for x in wynik_prac:
            print(x['id'], x['imie'], x['nazwisko'], x['miejscowosc'], x['zarobki'])

def dodaj(imie, nazwisko, miejscowosc, zarobki):
    with con:
        cur.execute('INSERT INTO pracownicy VALUES(NULL, ?, ?, ?, ?)', (imie, nazwisko, miejscowosc, zarobki))
        print('\nDodano pracownika')

def usun(id):
    with con:
        cur.execute('DELETE FROM pracownicy WHERE id=?', (id,))
        print('\nUsunięto pracownika')

def zmien(id, msc):
    with con:
        cur.execute('UPDATE pracownicy SET miejscowosc=? WHERE id=?', (msc, id))
        print('\nZaktualizowano miejsce zamieszkania.')

def znajdz(num):
    with con:
        cur.execute('SELECT * FROM pracownicy WHERE miejscowosc=?', (num,))
        y = cur.fetchall()
        print('\nPracownik:')
        for x in y:
            print(x['id'], x['imie'], x['nazwisko'], x['miejscowosc'], x['zarobki'])

def znajdzmax():
    with con:
        cur.execute('SELECT * FROM pracownicy WHERE zarobki = (SELECT MAX(zarobki) FROM pracownicy)', ())
        y = cur.fetchall()
        print('\nNajwiększy darmozjad:')
        for x in y:
            print(x['id'], x['imie'], x['nazwisko'], x['miejscowosc'], x['zarobki'])

def znajdzmin():
    with con:
        cur.execute('SELECT * FROM pracownicy WHERE zarobki = (SELECT MIN(zarobki) FROM pracownicy)', ())
        y = cur.fetchall()
        print('\nNajmniejszy darmozjad:')
        for x in y:
            print(x['id'], x['imie'], x['nazwisko'], x['miejscowosc'], x['zarobki'])
def menu():
    print("Witaj, co chcesz zrobić?")
    print("(1) Utwórz bazę / zastąp obecną")
    print("(2) Wyświetl bazę")
    print("(2.2) Wyświetl bazę (z sortowaniem alfabetycznym po imieniu)")
    print("(3) Dodaj pracownika")
    print("(4) Zlikwiduj pracownika")
    print("(5) Zaktualizuj miejsce zamieszkania pracownika")
    print("(6) Znajdz pracownika")
    print("(6.1) Znajdz największego darmozjada")
    print("(6.2) Znajdz najmniejszego darmozjada")
    print("(7) Zakończ program")

menu()
opcja = input("Jaką opcje wybierasz: ")
if opcja == "1":
    tabela()
    print("Utworzono bazę")
elif opcja == "2":
    wyswietl()
elif opcja == "2.2":
    wyswietlsort()
elif opcja == "3":
    imi = input("Podaj imie: ")
    naz = input("Podaj nazwisko: ")
    msc = input("Podaj miejsce zamieszkania: ")
    zar = input("Podaj zarobki: ")
    dodaj(imi, naz, msc, zar)
elif opcja == "4":
    ID = input("Podaj ID do usunięcia z listy: ")
    usun(ID)
elif opcja == "5":
    ID = input("Podaj ID do edycji miejsca zamieszkania: ")
    msc = input("Podaj nowe miejsce zamieszkania: ")
    zmien(ID, msc)
elif opcja == "6":
    msc = input("Podaj miejscowość osoby której chcesz znaleść: ")
    znajdz(msc)
elif opcja == "6.1":
    znajdzmax()
elif opcja == "6.2":
    znajdzmin()
else:
    print("Koniec programu")

con.close()
