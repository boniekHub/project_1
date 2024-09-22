import time

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Wartość musi być dodatnia. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def get_choice():
    while True:
        try:
            choice = int(input("Podaj numer opcji: "))
            if 1 <= choice <= 20:
                return choice
            else:
                print("Wybierz opcję od 1 do 20.")
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj ponownie.")

while True:
    print("\nKalkulator geometryczny")
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
    print("20. Wyjście")

    choice = get_choice()

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
        if a <= 0 or b <= 0 or h <= 0 or a + b <= h:
            print("Podane wartości nie tworzą prawidłowego trapezu. Spróbuj ponownie.")
        else:
            pole_trapezu = (a + b) * h / 2
            print("Pole trapezu wynosi:", pole_trapezu)

    elif choice == 5:
        while True:
            a = get_positive_float("Podaj pierwszy bok trójkąta: ")
            b = get_positive_float("Podaj drugi bok trójkąta: ")
            c = get_positive_float("Podaj trzeci bok trójkąta: ")
            if is_valid_triangle(a, b, c):
                s = (a + b + c) / 2
                pole_trojkata = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                print("Pole trójkąta wynosi:", pole_trojkata)
                break
            else:
                print("Podane wartości nie tworzą prawidłowego trójkąta. Spróbuj ponownie.")

    elif choice == 6:
        a = get_positive_float("Podaj bok kwadratu: ")
        obwod_kwadratu = 4 * a
        print("Obwód kwadratu wynosi:", obwod_kwadratu)

    elif choice == 7:
        a = get_positive_float("Podaj pierwszy bok prostokąta: ")
        b = get_positive_float("Podaj drugi bok prostokąta: ")
        obwod_prostokata = 2 * (a + b)
        print("Obwód prostokąta wynosi:", obwod_prostokata)

    elif choice == 8:
        a = get_positive_float("Podaj pierwszy bok równoległoboku: ")
        b = get_positive_float("Podaj drugi bok równoległoboku: ")
        obwod_rownoleglogu = 2 * (a + b)
        print("Obwód równoległoboku wynosi:", obwod_rownoleglogu)

    elif choice == 9:
        a = get_positive_float("Podaj pierwszą podstawę trapezu: ")
        b = get_positive_float("Podaj drugą podstawę trapezu: ")
        c = get_positive_float("Podaj pierwszy bok trapezu: ")
        d = get_positive_float("Podaj drugi bok trapezu: ")
        if a + b <= c + d:
            print("Podane wartości nie tworzą prawidłowego trapezu. Spróbuj ponownie.")
        else:
            obwod_trapezu = a + b + c + d
            print("Obwód trapezu wynosi:", obwod_trapezu)

    elif choice == 10:
        a = get_positive_float("Podaj pierwszy bok trójkąta: ")
        b = get_positive_float("Podaj drugi bok trójkąta: ")
        c = get_positive_float("Podaj trzeci bok trójkąta: ")
        if not is_valid_triangle(a, b, c):
            print("Podane wartości nie tworzą prawidłowego trójkąta. Spróbuj ponownie.")
        else:
            obwod_trojkata = a + b + c
            print("Obwód trójkąta wynosi:", obwod_trojkata)

    elif choice == 11:
        a = get_positive_float("Podaj bok trójkąta równobocznego: ")
        obwod_trojkata_rownobocznego = 3 * a
        print("Obwód trójkąta równobocznego wynosi:", obwod_trojkata_rownobocznego)

    elif choice == 12:
        a = get_positive_float("Podaj bok sześcianu: ")
        objetosc_szescianu = a ** 3
        print("Objętość sześcianu wynosi:", objetosc_szescianu)

    elif choice == 13:
        a = get_positive_float("Podaj pierwszy bok prostopadłościanu: ")
        b = get_positive_float("Podaj drugi bok prostopadłościanu: ")
        c = get_positive_float("Podaj trzeci bok prostopadłościanu: ")
        objetosc_prostopadloscianu = a * b * c
        print("Objętość prostopadłościanu wynosi:", objetosc_prostopadloscianu)

    elif choice == 14:
        Pp = get_positive_float("Podaj pole podstawy graniastosłupa: ")
        h = get_positive_float("Podaj wysokość graniastosłupa: ")
        objetosc_graniastoslupa = Pp * h
        print("Objętość graniastosłupa wynosi:", objetosc_graniastoslupa)

    elif choice == 15:
        Pp = get_positive_float("Podaj pole podstawy ostrosłupa: ")
        h = get_positive_float("Podaj wysokość ostrosłupa: ")
        objetosc_ostroslupa = (Pp * h) / 3
        print("Objętość ostrosłupa wynosi:", objetosc_ostroslupa)

    elif choice == 16:
        a = get_positive_float("Podaj bok sześcianu: ")
        pole_szescianu = 6 * a ** 2
        print("Pole powierzchni sześcianu wynosi:", pole_szescianu)

    elif choice == 17:
        a = get_positive_float("Podaj pierwszy bok prostopadłościanu: ")
        b = get_positive_float("Podaj drugi bok prostopadłościanu: ")
        c = get_positive_float("Podaj trzeci bok prostopadłościanu: ")
        pole_prostopadloscianu = 2 * (a * b + a * c + b * c)
        print("Pole powierzchni prostopadłościanu wynosi:", pole_prostopadloscianu)

    elif choice == 18:
        Pp = get_positive_float("Podaj pole podstawy graniastosłupa: ")
        Pb = get_positive_float("Podaj pole powierzchni bocznej graniastosłupa: ")
        pole_graniastoslupa = 2 * Pp + Pb
        print("Pole powierzchni graniastosłupa wynosi:", pole_graniastoslupa)

    elif choice == 19:
        Pp = get_positive_float("Podaj pole podstawy ostrosłupa: ")
        Pb = get_positive_float("Podaj pole powierzchni bocznej ostrosłupa: ")
        pole_ostroslupa = Pp + Pb
        print("Pole powierzchni ostrosłupa wynosi:", pole_ostroslupa)

    elif choice == 20:
        print("Koniec programu.")
        break

    else:
        print("Nie ma takiej opcji!")

    time.sleep(3)