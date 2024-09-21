print("Kalkulator geometryczny")
print("Wybierz opcję:")
print("1. Pole kwadratu")
print("2. Pole prostokąta")
print("3. Pole równoległoboku")
print("4. Pole trapezu")
print("5. Pole trójkąta")
print("6. Obwód kwadratu")
print("7. Obwód prostokąta")
print("8. Obwód równoległoboku")
print("9. Obwód trapezu")
print("10. Obwód trójkąta")
print("11. Obwód trójkąta równobocznego")
print("12. Objętość sześcianu")
print("13. Objętość prostopadłościanu")
print("14. Objętość graniastosłupa")
print("15. Objętość ostrosłupa")
print("16. Pole powierzchni sześcianu")
print("17. Pole powierzchni prostopadłościanu")
print("18. Pole powierzchni graniastosłupa")
print("19. Pole powierzchni ostrosłupa")

choice = int(input("Podaj numer opcji: "))

def get_positive_float(prompt):
    value = float(input(prompt))
    while value <= 0:
        print("Wartość musi być dodatnia. Spróbuj ponownie.")
        value = float(input(prompt))
    return value

if choice == 1:
    a = get_positive_float("Podaj bok kwadratu: ")
    pole_kwadratu = a * a
    print("Pole kwadratu wynosi:", pole_kwadratu)

elif choice == 2:
    a = get_positive_float("Podaj pierwszy bok prostokąta: ")
    b = get_positive_float("Podaj drugi bok prostokąta: ")
    pole_prostokata = a * b
    print("Pole prostokąta wynosi:", pole_prostokata)

elif choice == 3:
    a = get_positive_float("Podaj podstawę równoległoboku: ")
    h = get_positive_float("Podaj wysokość równoległoboku: ")
    pole_rownoleglogu = a * h
    print("Pole równoległoboku wynosi:", pole_rownoleglogu)

elif choice == 4:
    a = get_positive_float("Podaj długość pierwszej podstawy trapezu: ")
    b = get_positive_float("Podaj długość drugiej podstawy trapezu: ")
    h = get_positive_float("Podaj wysokość trapezu: ")
    pole_trapezu = (a + b) * h / 2
    print("Pole trapezu wynosi:", pole_trapezu)

elif choice == 5:
    a = float(input("Podaj długość podstawy trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    pole_trojkata = (a * h) / 2
    print("Pole trójkąta wynosi:", pole_trojkata)

elif choice == 6:
    a = float(input("Podaj bok kwadratu: "))
    obwod_kwadratu = 4 * a
    print("Obwód kwadratu wynosi:", obwod_kwadratu)

elif choice == 7:
    a = float(input("Podaj pierwszy bok prostokąta: "))
    b = float(input("Podaj drugi bok prostokąta: "))
    obwod_prostokata = 2 * (a + b)
    print("Obwód prostokąta wynosi:", obwod_prostokata)

elif choice == 8:
    a = float(input("Podaj pierwszy bok równoległoboku: "))
    b = float(input("Podaj drugi bok równoległoboku: "))
    obwod_rownoleglogu = 2 * (a + b)
    print("Obwód równoległoboku wynosi:", obwod_rownoleglogu)

elif choice == 9:
    a = float(input("Podaj pierwszą podstawę trapezu: "))
    b = float(input("Podaj drugą podstawę trapezu: "))
    c = float(input("Podaj pierwszy bok trapezu: "))
    d = float(input("Podaj drugi bok trapezu: "))
    obwod_trapezu = a + b + c + d
    print("Obwód trapezu wynosi:", obwod_trapezu)

elif choice == 10:
    a = float(input("Podaj pierwszy bok trójkąta: "))
    b = float(input("Podaj drugi bok trójkąta: "))
    c = float(input("Podaj trzeci bok trójkąta: "))
    obwod_trojkata = a + b + c
    print("Obwód trójkąta wynosi:", obwod_trojkata)

elif choice == 11:
    a = float(input("Podaj bok trójkąta równobocznego: "))
    obwod_trojkata_rownobocznego = 3 * a
    print("Obwód trójkąta równobocznego wynosi:", obwod_trojkata_rownobocznego)

elif choice == 12:
    a = float(input("Podaj bok sześcianu: "))
    objetosc_szescianu = a ** 3
    print("Objętość sześcianu wynosi:", objetosc_szescianu)

elif choice == 13:
    a = float(input("Podaj pierwszy bok prostopadłościanu: "))
    b = float(input("Podaj drugi bok prostopadłościanu: "))
    c = float(input("Podaj trzeci bok prostopadłościanu: "))
    objetosc_prostopadloscianu = a * b * c
    print("Objętość prostopadłościanu wynosi:", objetosc_prostopadloscianu)

elif choice == 14:
    Pp = float(input("Podaj pole podstawy graniastosłupa: "))
    h = float(input("Podaj wysokość graniastosłupa: "))
    objetosc_graniastoslupa = Pp * h
    print("Objętość graniastosłupa wynosi:", objetosc_graniastoslupa)

elif choice == 15:
    Pp = float(input("Podaj pole podstawy ostrosłupa: "))
    h = float(input("Podaj wysokość ostrosłupa: "))
    objetosc_ostroslupa = (Pp * h) / 3
    print("Objętość ostrosłupa wynosi:", objetosc_ostroslupa)

elif choice == 16:
    a = float(input("Podaj bok sześcianu: "))
    pole_szescianu = 6 * a ** 2
    print("Pole powierzchni sześcianu wynosi:", pole_szescianu)

elif choice == 17:
    a = float(input("Podaj pierwszy bok prostopadłościanu: "))
    b = float(input("Podaj drugi bok prostopadłościanu: "))
    c = float(input("Podaj trzeci bok prostopadłościanu: "))
    pole_prostopadloscianu = 2 * (a * b + a * c + b * c)
    print("Pole powierzchni prostopadłościanu wynosi:", pole_prostopadloscianu)

elif choice == 18:
    Pp = float(input("Podaj pole podstawy graniastosłupa: "))
    Pb = float(input("Podaj pole powierzchni bocznej graniastosłupa: "))
    pole_graniastoslupa = 2 * Pp + Pb
    print("Pole powierzchni graniastosłupa wynosi:", pole_graniastoslupa)

elif choice == 19:
    Pp = float(input("Podaj pole podstawy ostrosłupa: "))
    Pb = float(input("Podaj pole powierzchni bocznej ostrosłupa: "))
    pole_ostroslupa = Pp + Pb
    print("Pole powierzchni ostrosłupa wynosi:", pole_ostroslupa)

else:
    print("Nie ma takiej opcji!")