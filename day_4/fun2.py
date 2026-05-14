# funkcje zwracające wynik
# końćzy się komendą return

a = 9
b = 98


def dodaj():
    return a + b
    # zwróć wynik dodawania


# odejmij z trzema argumentami domyslnymi, zwracającą wynik
def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj())  # 107
wynik = dodaj()
print("wynik:", wynik)  # wynik: 107

print(odejmij(1, 2, 3))
print(odejmij(1, 2, c=3))
print(odejmij(1, b=2, c=3))
print(odejmij())
print(odejmij(a, b))
