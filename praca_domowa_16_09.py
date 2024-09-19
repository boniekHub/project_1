# Zadanie 1
liczba = int(input("Podaj liczbę: "))  # Użytkownik podaje liczbę
liczba = (liczba - 5) * 2
print("Ostateczny wynik po zmniejszeniu o 5 i pomnożeniu przez 2:", liczba)

# Zadanie 2
wartosc_logiczna = input("Podaj wartość logiczną (True/False): ").capitalize() == 'True'
wartosc_logiczna = not wartosc_logiczna
print("Wynik po negacji wartości logicznej:", wartosc_logiczna)

# Zadanie 3
liczba_calkowita = int(input("Podaj liczbę całkowitą: "))
liczba_zmiennoprzecinkowa = float(input("Podaj liczbę zmiennoprzecinkową: "))
wynik = float(liczba_calkowita) + liczba_zmiennoprzecinkowa
print("Wynik dodania:", wynik)

# Zadanie 4
celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura w stopniach Fahrenheita: {fahrenheit}")

# Zadanie 5
ciag_znakow = input("Podaj dowolny ciąg znaków: ")
pierwsza_litera = ciag_znakow[0]
ostatnia_litera = ciag_znakow[-1]
print(f"Pierwsza litera: {pierwsza_litera}, Ostatnia litera: {ostatnia_litera}")