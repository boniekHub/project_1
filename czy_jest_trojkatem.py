a = float(input())
b = float(input())
c = float(input())
if a + b > c:
    if b + c > a:
        if c + a > b:
            print("to jest tr")
        else:
            print("to nie jest tr")
    else:
        print("to nie jest tr")
else:
    print("to nie jest tr")

# Druga (lepsza) wersja programu
#               |
#               |
#               |
#               ▼
if a + b > c and b + c > a and c + a > b:
    print("to jest tr")
else:
    print("to nie jest tr")