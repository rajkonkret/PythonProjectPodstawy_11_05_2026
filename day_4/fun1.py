# funkcja - wydzielony fragment kodu, można wywołac w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# żeby funkcja się uruchomiła musimy ją wywołać


a = 6
b = 8


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)  # wykonane na globalnych wartościach


def dodaj2(a, b):  # dwa obowiązkowe argumenty a, b
    print(a + b)  # wartości lokalne


# wywołąnie funkcji
dodaj()  # 14

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 9)  # 14
