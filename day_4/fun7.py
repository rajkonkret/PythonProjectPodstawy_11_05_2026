def connect(**opcje):  # dowolna liczba argumentów po nazwie (keywords)
    print(opcje)  # {} słownik


connect()
connect(a=10)  # {'a': 10}
connect(a=10, b=90, c=78, name="Radek")  # {'a': 10}


# {'a': 10, 'b': 90, 'c': 78, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)

