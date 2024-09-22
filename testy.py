import time

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Wartość musi być dodatnia.")
        except ValueError:
            print("Niepoprawna wartość. Wprowadź liczbę.")

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_area_square():
    side = get_positive_float("Podaj bok kwadratu: ")
    return side * side

def calculate_area_rectangle():
    a = get_positive_float("Podaj pierwszy bok prostokąta: ")
    b = get_positive_float("Podaj drugi bok prostokąta: ")
    return a * b

def calculate_area_parallelogram():
    base = get_positive_float("Podaj podstawę równoległoboku: ")
    height = get_positive_float("Podaj wysokość równoległoboku: ")
    return base * height

def calculate_area_trapezoid():
    a = get_positive_float("Podaj długość pierwszej podstawy trapezu: ")
    b = get_positive_float("Podaj długość drugiej podstawy trapezu: ")
    h = get_positive_float("Podaj wysokość trapezu: ")
    return (a + b) * h / 2

def calculate_area_triangle():
    base = get_positive_float("Podaj długość podstawy trójkąta: ")
    height = get_positive_float("Podaj wysokość trójkąta: ")
    return (base * height) / 2

def calculate_perimeter_square():
    side = get_positive_float("Podaj bok kwadratu: ")
    return 4 * side

def calculate_perimeter_rectangle():
    a = get_positive_float("Podaj pierwszy bok prostokąta: ")
    b = get_positive_float("Podaj drugi bok prostokąta: ")
    return 2 * (a + b)

def calculate_perimeter_parallelogram():
    a = get_positive_float("Podaj pierwszy bok równoległoboku: ")
    b = get_positive_float("Podaj drugi bok równoległoboku: ")
    return 2 * (a + b)

def calculate_perimeter_trapezoid():
    a = get_positive_float("Podaj pierwszą podstawę trapezu: ")
    b = get_positive_float("Podaj drugą podstawę trapezu: ")
    c = get_positive_float("Podaj pierwszy bok trapezu: ")
    d = get_positive_float("Podaj drugi bok trapezu: ")
    return a + b + c + d

def calculate_perimeter_triangle():
    a = get_positive_float("Podaj pierwszy bok trójkąta: ")
    b = get_positive_float("Podaj drugi bok trójkąta: ")
    c = get_positive_float("Podaj trzeci bok trójkąta: ")
    if is_valid_triangle(a, b, c):
        return a + b + c
    else:
        print("Boki nie tworzą prawidłowego trójkąta.")
        return None

def calculate_volume_cube():
    side = get_positive_float("Podaj bok sześcianu: ")
    return side ** 3

def calculate_volume_rectangular_prism():
    a = get_positive_float("Podaj pierwszy bok prostopadłościanu: ")
    b = get_positive_float("Podaj drugi bok prostopadłościanu: ")
    c = get_positive_float("Podaj trzeci bok prostopadłościanu: ")
    return a * b * c

def calculate_area_cube():
    side = get_positive_float("Podaj bok sześcianu: ")
    return 6 * side ** 2

def display_menu():
    print("\nKalkulator geometryczny")
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
    print("14. Wyjście")

def handle_choice(choice):
    operations = {
        1: ("Pole kwadratu", calculate_area_square),
        2: ("Pole prostokąta", calculate_area_rectangle),
        3: ("Pole równoległoboku", calculate_area_parallelogram),
        4: ("Pole trapezu", calculate_area_trapezoid),
        5: ("Pole trójkąta", calculate_area_triangle),
        6: ("Obwód kwadratu", calculate_perimeter_square),
        7: ("Obwód prostokąta", calculate_perimeter_rectangle),
        8: ("Obwód równoległoboku", calculate_perimeter_parallelogram),
        9: ("Obwód trapezu", calculate_perimeter_trapezoid),
        10: ("Obwód trójkąta", calculate_perimeter_triangle),
        11: ("Objętość sześcianu", calculate_volume_cube),
        12: ("Objętość prostopadłościanu", calculate_volume_rectangular_prism),
        13: ("Pole powierzchni sześcianu", calculate_area_cube)
    }

    if choice in operations:
        name, func = operations[choice]
        result = func()
        if result is not None:
            print(f"{name} wynosi: {result}")
    elif choice == 14:
        print("Koniec programu.")
        return False
    else:
        print("Nie ma takiej opcji!")

    return True

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Podaj numer opcji: "))
        except ValueError:
            print("Niepoprawna opcja. Podaj numer.")
            continue

        if not handle_choice(choice):
            break

        time.sleep(3)

if __name__ == "__main__":
    main()