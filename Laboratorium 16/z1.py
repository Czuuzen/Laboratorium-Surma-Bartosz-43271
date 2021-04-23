import sqlite3
con = sqlite3.connect("Kontakty")
con.row_factory = sqlite3.Row

cur = con.cursor()

def tabela():
    cur.executescript("""
    DROP TABLE IF EXISTS numery;
    CREATE TABLE IF NOT EXISTS numery (
    id INTEGER PRIMARY KEY ASC,
    imie varchar(250) NOT NULL,
    nazwisko varchar(250) NOT NULL,
    numer INTEGER NOT NULL
)""")

def wyswietl():
    with con:
        cur.execute('SELECT * FROM numery')
        wynik_kontakty=cur.fetchall()
        print('\nKontakty:')
        for x in wynik_kontakty:
            print(x['id'],x['imie'],x['nazwisko'],x['numer'])

def dodaj(imie, nazwisko, numer):
    with con:
        cur.execute('INSERT INTO numery VALUES(NULL, ?, ?, ?)', (imie, nazwisko, numer))
        print('\nDodano kontakt')

def usun(id):
    with con:
        cur.execute('DELETE FROM numery WHERE id=?', (id,))
        print('\nUsunięto kontakt')

def zmien(id, num):
    with con:
        cur.execute('UPDATE numery SET numer=? WHERE id=?', (num, id))
        print('\nZaktualizowano numer')

def znajdz(num):
    with con:
        cur.execute('SELECT * FROM numery WHERE numer=?', (num,))
        y = cur.fetchall()
        print('\nKontakt:')
        for x in y:
            print(x['id'],x['imie'],x['nazwisko'],x['numer'])
def menu():
    print("Witaj, co chcesz zrobić?")
    print("(1) Utwórz bazę / zastąp obecną")
    print("(2) Wyświetl bazę")
    print("(3) Dodaj kontakt")
    print("(4) Usuń kontakt")
    print("(5) Zaktualizuj kontakt")
    print("(6) Znajdz kontakt")
    print("(7) Zakończ program")

menu()
opcja = input("Jaką opcje wybierasz: ")
if opcja == "1":
    tabela()
    print("Utworzono bazę")
elif opcja == "2":
    wyswietl()
elif opcja == "3":
    imi = input("Podaj imie: ")
    naz = input("Podaj nazwisko: ")
    num = input("Podaj numer: ")
    dodaj(imi, naz, num)
elif opcja == "4":
    ID = input("Podaj ID do usunięcia z listy: ")
    usun(ID)
elif opcja == "5":
    ID = input("Podaj ID do edycji numeru: ")
    num = input("Podaj nowy numer: ")
    zmien(ID, num)
elif opcja == "6":
    num = input("Podaj numer osoby której chcesz znaleść: ")
    znajdz(num)
else:
    print("Koniec programu")

con.close()