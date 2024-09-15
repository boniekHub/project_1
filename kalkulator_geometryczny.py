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
print("11. Objętość sześcianu")
print("12. Objętość prostopadłościanu")
print("13. Pole powierzchni sześcianu")
print("14. Pole powierzchni prostopadłościanu")

choice = input("Podaj numer opcji: ")

if choice == "1":
    a = float(input("Podaj bok kwadratu: "))
    print("Pole kwadratu wynosi:", a * a)

elif choice == "2":
    a = float(input("Podaj pierwszy bok prostokąta: "))
    b = float(input("Podaj drugi bok prostokąta: "))
    print("Pole prostokąta wynosi:", a * b)

elif choice == "3":
    a = float(input("Podaj podstawę równoległoboku: "))
    h = float(input("Podaj wysokość równoległoboku: "))
    print("Pole równoległoboku wynosi:", a * h)

elif choice == "4":
    a = float(input("Podaj długość pierwszej podstawy trapezu: "))
    b = float(input("Podaj długość drugiej podstawy trapezu: "))
    h = float(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi:", (a + b) * h / 2)

elif choice == "5":
    a = float(input("Podaj długość podstawy trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi:", (a * h) / 2)

elif choice == "6":
    a = float(input("Podaj bok kwadratu: "))
    print("Obwód kwadratu wynosi:", 4 * a)

elif choice == "7":
    a = float(input("Podaj pierwszy bok prostokąta: "))
    b = float(input("Podaj drugi bok prostokąta: "))
    print("Obwód prostokąta wynosi:", 2 * (a + b))

elif choice == "8":
    a = float(input("Podaj pierwszy bok równoległoboku: "))
    b = float(input("Podaj drugi bok równoległoboku: "))
    print("Obwód równoległoboku wynosi:", 2 * (a + b))

elif choice == "9":
    a = float(input("Podaj pierwszą podstawę trapezu: "))
    b = float(input("Podaj drugą podstawę trapezu: "))
    c = float(input("Podaj pierwszy bok trapezu: "))
    d = float(input("Podaj drugi bok trapezu: "))
    print("Obwód trapezu wynosi:", a + b + c + d)

elif choice == "10":
    a = float(input("Podaj pierwszy bok trójkąta: "))
    b = float(input("Podaj drugi bok trójkąta: "))
    c = float(input("Podaj trzeci bok trójkąta: "))
    print("Obwód trójkąta wynosi:", a + b + c)

elif choice == "11":
    a = float(input("Podaj bok sześcianu: "))
    print("Objętość sześcianu wynosi:", a ** 3)

elif choice == "12":
    a = float(input("Podaj pierwszy bok prostopadłościanu: "))
    b = float(input("Podaj drugi bok prostopadłościanu: "))
    c = float(input("Podaj trzeci bok prostopadłościanu: "))
    print("Objętość prostopadłościanu wynosi:", a * b * c)

elif choice == "13":
    a = float(input("Podaj bok sześcianu: "))
    print("Pole powierzchni sześcianu wynosi:", 6 * a ** 2)

elif choice == "14":
    a = float(input("Podaj pierwszy bok prostopadłościanu: "))
    b = float(input("Podaj drugi bok prostopadłościanu: "))
    c = float(input("Podaj trzeci bok prostopadłościanu: "))
    print("Pole powierzchni prostopadłościanu wynosi:", 2 * (a * b + a * c + b * c))

else:
    print("Nie ma takiej opcji!")