def ftemp():
    global temp
    try:
        temp = float(input("Podaj wartość temperatury do przeliczenia: "))
    except ValueError:
        print("Nie podałeś wartości temperatury lub błędny zapis!")
        exit()

def ctf(x):
    f = x * 1.8 + 32
    if f <= 32:
        return print(x, "°C to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze zamarza")
    elif f >= 212:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(f, 2), "°F")

def ftc(x):
    c = (x - 32) / 1.8
    if c <= 0:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze zamarza")
    elif c >= 100:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(c, 2), "°C")

def ktf(x):
    f = x * 1.8 - 459.67
    if f <= 32:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze zamarza")
    elif f >= 212:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(f, 2), "°F")

def ftk(x):
    k = (x + 459.67) * 5 / 9
    if k <= 273.15:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze zamarza")
    elif k >= 373.15:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(k, 2), "K")

def ktc(x):
    c = x - 273.15
    if c <= 0:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze zamarza")
    elif c >= 100:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(c, 2), "°C")

def ctk(x):
    k = x + 273.15
    if k <= 273.15:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze zamarza")
    elif k >= 373.15:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(k, 2), "K")

def ctra(x):
    r = (x + 273.15) * 9 / 5
    if r <= 491.67:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(r, 2), "°R, woda w tej temperaturze zamarza")
    elif r >= 671.67:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(r, 2), "°R, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(r, 2), "°R")

def ctr(x):
    r = x * 21 / 40 + 7.5
    if r <= 7:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(r, 2), "°Rø, woda w tej temperaturze zamarza")
    elif r >= 60:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(r, 2), "°Rø, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(r, 2), "°Rø")


print("Przelicznik temperatur")
print("\nWybierz sposób zamiany")
print("1)Celsjusze na Farenheity")
print("2)Farenheity na Celsjusze")
print("3)Kelwiny na Farenheity")
print("4)Farenheity na Kelwiny")
print("5)Kelwiny na Celsjusze")
print("6)Celsjusze na Kelwiny")
print("7)Celsjusze na stopnie Rankine’a")
print("8)Celsjusze na stopnie Rømera")

opcja = input("\nWybierz sposób: ")
if opcja in ('1', '2', '3', '4', '5', '6', '7', '8'):
    temp = 0
    if opcja == '1':
        ftemp()
        ctf(temp)
    elif opcja == '2':
        ftemp()
        ftc(temp)
    elif opcja == '3':
        ftemp()
        ktf(temp)
    elif opcja == '4':
        ftemp()
        ftk(temp)
    elif opcja == '5':
        ftemp()
        ktc(temp)
    elif opcja == '6':
        ftemp()
        ctk(temp)
    elif opcja == '7':
        ftemp()
        ctra(temp)
    elif opcja == '8':
        ftemp()
        ctr(temp)
else:
    print("Wybrałeś złą opcje")