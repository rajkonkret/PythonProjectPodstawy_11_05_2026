a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne, widoczne tylko wewnątrz funkcji
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # działa na globalnych


def dodaj3():
    global a  # użyj zmiennej globalnej
    a = 7  # zmieniamy wartość zmiennej globalnej
    b = 90
    print(a + b)


def dodaj5():
    a = 10  # lokalne a
    b = 9
    c = a + b
    print(c)  # c - zmienna lokalna


print("Wartość a z góry (globalne)", a)  # Wartość a z góry (globalne) 10
dodaj()  # 15
print("Wartość a z góry (globalne)", a)  # Wartość a z góry (globalne) 10
dodaj2()  # 20
print("Wartość a z góry (globalne)", a)  # Wartość a z góry (globalne) 10
dodaj3()  # 97
print("Wartość a z góry (globalne)", a)  # Wartość a z góry (globalne) 7
dodaj2()  # 7 + 10
print("Wartość a z góry (globalne)", a)  # Wartość a z góry (globalne) 7
dodaj5()  # 19
print("Wartość a z góry (globalne)", a)  # Wartość a z góry (globalne) 7
# print(c)  # NameError: name 'c' is not defined
