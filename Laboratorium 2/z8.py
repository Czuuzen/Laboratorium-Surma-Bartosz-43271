print ("Sprawdzamy czy trójkąt abc jest prostokątny ")
a = int(input("Podaj pierwszy bok trójkąta a: "))
b = int(input("Podaj  drugi bok  trójkąta b: "))
c = int(input("Podaj trzeci bok  trójkąta c: "))

if(c*c==a*a+b*b or a*a==b*b+c*c or b*b==a*a+c*c) :
     print ("Trójkąt abc jest prostokątny")

else:
     print("Trójkąt abc nie jest prostokątny")