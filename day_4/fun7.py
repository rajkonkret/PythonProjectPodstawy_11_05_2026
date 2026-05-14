def connect(**opcje):  # dowolna liczba argumentów po nazwie (keywords)
    print(opcje)  # {} słownik


connect()
connect(a=10)  # {'a': 10}
connect(a=10, b=90, c=78, name="Radek")  # {'a': 10}


# {'a': 10, 'b': 90, 'c': 78, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()
all_args(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5) {}
all_args(a=10, b=30)  # () {'a': 10, 'b': 30}
all_args(5, 6, 5, 6, 75, 6, name="Radek")
# (5, 6, 5, 6, 75, 6) {'name': 'Radek'}

# all_args(a=10, 1,2,3,4) # SyntaxError: positional argument follows keyword argument
