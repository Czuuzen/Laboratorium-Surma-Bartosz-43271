import re
code = str(input("Wpisz kod pocztowy: "))
try:
    if re.match("^\d\d-\d\d\d$", code):
        print ("Kod pocztowy poprawny")
    else:
        print("Kod pocztowy nieporawny")
except NoString:
    print("Podaj kod!!!")