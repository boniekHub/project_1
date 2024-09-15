import math

# Funkcje dla obliczeń pól i obwodów
def pole_kwadratu(a):
    return a ** 2

def pole_prostokata(a, b):
    return a * b

def pole_rownoleglogu(a, h):
    return a * h

def pole_trapezu(a, b, h):
    return (a + b) * h / 2

def pole_trojkata(a, h):
    return (a * h) / 2

def obwod_kwadratu(a):
    return 4 * a

def obwod_prostokata(a, b):
    return 2 * (a + b)

def obwod_rownolegloboku(a, b):
    return 2 * (a + b)

def obwod_trapezu(a, b, c, d):
    return a + b + c + d

def obwod_trojkata(a, b, c):
    return a + b + c

def obwod_trojkata_rownobocznego(a):
    return 3 * a

# Funkcje dla obliczeń objętości i powierzchni
def objetosc_szescianu(a):
    return a ** 3

def objetosc_prostopadloscianu(a, b, c):
    return a * b * c

def objetosc_graniastoslupa(Pp, h):
    return Pp * h

def objetosc_ostroslupa(Pp, h):
    return (Pp * h) / 3

def pole_powierzchni_szescianu(a):
    return 6 * a ** 2

def pole_powierzchni_prostopadloscianu(a, b, c):
    return 2 * (a * b + a * c + b * c)

def pole_powierzchni_graniastoslupa(Pp, Pb):
    return 2 * Pp + Pb

def pole_powierzchni_ostroslupa(Pp, Pb):
    return Pp + Pb

# Słownik funkcji przypisany do numerów opcji
opcje = {
    "1": ("Pole kwadratu", pole_kwadratu, ['a']),
    "2": ("Pole prostokąta", pole_prostokata, ['a', 'b']),
    "3": ("Pole równoległoboku", pole_rownoleglogu, ['a', 'h']),
    "4": ("Pole trapezu", pole_trapezu, ['a', 'b', 'h']),
    "5": ("Pole trójkąta", pole_trojkata, ['a', 'h']),
    "6": ("Obwód kwadratu", obwod_kwadratu, ['a']),
    "7": ("Obwód prostokąta", obwod_prostokata, ['a', 'b']),
    "8": ("Obwód równoległoboku", obwod_rownolegloboku, ['a', 'b']),
    "9": ("Obwód trapezu", obwod_trapezu, ['a', 'b', 'c', 'd']),
    "10": ("Obwód trójkąta", obwod_trojkata, ['a', 'b', 'c']),
    "11": ("Obwód trójkąta równobocznego", obwod_trojkata_rownobocznego, ['a']),
    "12": ("Objętość sześcianu", objetosc_szescianu, ['a']),
    "13": ("Objętość prostopadłościanu", objetosc_prostopadloscianu, ['a', 'b', 'c']),
    "14": ("Objętość graniastosłupa", objetosc_graniastoslupa, ['Pp', 'h']),
    "15": ("Objętość ostrosłupa", objetosc_ostroslupa, ['Pp', 'h']),
    "16": ("Pole powierzchni sześcianu", pole_powierzchni_szescianu, ['a']),
    "17": ("Pole powierzchni prostopadłościanu", pole_powierzchni_prostopadloscianu, ['a', 'b', 'c']),
    "18": ("Pole powierzchni graniastosłupa", pole_powierzchni_graniastoslupa, ['Pp', 'Pb']),
    "19": ("Pole powierzchni ostrosłupa", pole_powierzchni_ostroslupa, ['Pp', 'Pb']),
}

def main():
    print("Kalkulator geometryczny")
    
    # Wyświetlenie opcji
    for num, (desc, _, _) in opcje.items():
        print(f"{num}. {desc}")

    # Pobranie wyboru użytkownika
    choice = input("Podaj numer opcji: ")

    # Sprawdzenie, czy opcja istnieje
    if choice in opcje:
        opis, funkcja, parametry = opcje[choice]
        wartosci = []
        
        # Pobranie parametrów od użytkownika
        for param in parametry:
            wartosci.append(float(input(f"Podaj wartość {param}: ")))
        
        # Obliczenie wyniku
        wynik = funkcja(*wartosci)
        print(f"{opis}: {wynik}")
    
    else:
        print("Nie ma takiej opcji!")

if __name__ == "__main__":
    main()
