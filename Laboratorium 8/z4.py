import webbrowser
mail = {
    'adam':'adam@gmail.com',
}

a = (input("Podaj swoje imię: "))
b = (input("Podaj swój adres email: "))

mail[a] = b
print("Lista e-mail")
for imie, adres in mail.items():
    print(imie, adres)
    webbrowser.open("mailto:?to=", mail.values(), "&subject=mysubject")