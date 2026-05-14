# funkcja - wydzielony fragment kodu, można wywołac w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# żeby funkcja się uruchomiła musimy ją wywołać


a = 6
b = 8


# te funkcje nie zwracają wyniku
# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)  # wykonane na globalnych wartościach
    # wypisz wynik dodawania


def dodaj2(a, b):  # dwa obowiązkowe argumenty a, b
    print(a + b)  # wartości lokalne


# omninięcie problemu braku przeciązania funkcji liczbą argumentów
def odejmij(a, b, c=0):  # argument c o wartości domyslnej
    print(a - b - c)


# wywołąnie funkcji
dodaj()  # 14

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 9)  # 14

# argumenty pozycyjne
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# argumenty po nazwie
odejmij(b=90, a=87)
odejmij(b=90, c=87, a=76)
# -3
# -101

# mieszane
odejmij(1, 2, c=89)
dodaj2(1, b=90)
# -90
# 91

# argumenty pozycyjne musza byc przed nazwanymi
# odejmij(a=10, 1, 2) # SyntaxError: positional argument follows keyword argument

# print(dodaj() + dodaj2(6, 90))
#      None   +   None bo kończy się komendą print()
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
