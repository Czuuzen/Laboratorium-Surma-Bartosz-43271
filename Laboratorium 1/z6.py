s = float(input("Podaj dystans(w km): "))
t = float(input("Podaj czas(w min): "))
h = t/60                                                #zamiana minut na godziny
srednia = s/h                                           #liczenie średniej prędkości
print("Średnia prędkość wynosi: " , srednia , "km/h")
x = s+30
y = t+12
h2 = y/60
srednia2 = x/h2
print("Po dodaniu 30km i 12 minut średnia prędkość wynosi: " , srednia2 , "km/h")
