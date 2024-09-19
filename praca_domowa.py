liczba = int(input("Podaj liczbę: "))
liczba = (liczba - 5) * 2
print("Ostateczna wynik po zmniejszeniu o 5 i pomnożeniu przez 2 wynosi:", liczba)

wartosc_logiczna = input("Podaj wartość logiczną (True/False): ").capitalize() == "True"
wartosc_logiczna = not wartosc_logiczna
print("wynik negacji wartości logicznej to:", wartosc_logiczna)

liczba_cal = int(input("Podaj liczbę całkowitą: "))
liczba_zmiennoprzecinkowa = float(input("Podaj liczbę zmiennoprzecinkową: "))
wynik_3 = float(liczba_cal) + liczba_zmiennoprzecinkowa
print("wynik dodania:", wynik_3)

celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
farenheit = celsius * 1.8 + 32
print("Temperatura w stopniach Farenheita wynosi:", farenheit)

ciag_znakow = input("Podaj ciąg znaków: ")
pierwsza_litera = ciag_znakow[0]
ostatnia_litera = ciag_znakow[-1]
print(f"Pierwsza litera ciągu znaków to: {pierwsza_litera}, a ostatnia litera to: {ostatnia_litera}")