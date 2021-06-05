from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///filmy.db', echo = True)
meta = MetaData()

filmy = Table(
   'Oskarowe filmy', meta,
   Column('id', Integer, primary_key = True),
   Column('Tytuł', String),
   Column('Reżyser', String),
   Column('Aktorzy', String),
   Column('Gdzie_obejrzeć', String),
)
meta.create_all(engine) #utworzenie bazy danych oraz tabeli

conn = engine.connect()
#dodanie danych do tabeli
conn.execute(filmy.insert(), [
   {'Tytuł':'Ojciec Chrzestny', 'Reżyser' : 'Francis Ford Coppola', 'Aktorzy' : 'Marlon Brando, Al Pacino, James Caan, Robert Duvall, Diane Keaton', 'Gdzie_obejrzeć' : 'Netflix, HBO GO'},
   {'Tytuł':'Rocky', 'Reżyser' : 'John G. Avildsen', 'Aktorzy' : 'Sylvester Stallone, Talia Shire, Burt Young, Carl Weathers, Burgess Meredith', 'Gdzie_obejrzeć' : 'Netflix, HBO GO'},
   {'Tytuł':'Spartan', 'Reżyser' : 'Ridley Scott', 'Aktorzy' : 'Russell Crowe, Joaquin Phoenix, Connie Nielsen, Richard Harris, Djimon Hounsou', 'Gdzie_obejrzeć' : 'Netflix, HBO GO'},
   {'Tytuł': 'Infiltracja', 'Reżyser': 'Martin Scorsese', 'Aktorzy': 'Leonardo DiCaprio, Matt Damon, Jack Nicholson, Mark Wahlberg, Martin Sheen, Ray Winstone, Vera Farmiga, Alec Baldwin', 'Gdzie_obejrzeć': 'Netflix, HBO GO'},
])
#usunięcie danych
usun = filmy.delete().where(filmy.c.Tytuł == 'Rocky')
conn.execute(usun)
#aktualizacja danych
zmien=filmy.update().where(filmy.c.Tytuł=='Spartan').values(Tytuł='Gladiator')
conn.execute(zmien)
#wyświetlenie zawartości tabeli
s = filmy.select()
wyswietl = conn.execute(s)
for row in wyswietl:
   print (row)