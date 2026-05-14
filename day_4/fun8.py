def all_params(a, b, /, c=42, d=345):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)
# a=1, b=2
# c=42, d=345
all_params(1, 2, 3)
all_params(1, 2, 3, 4)
# a=1, b=2
# c=3, d=4

all_params(1, 2, c=8)
all_params(1, 2, c=8, d=90)


# / - oddziela parametry po nazwie od parametrów pozycyjnych
# a, b - muszą zostać przekazane po pozycji !!!

# all_params(a=1, b=2, c=3, d=4)
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'

def all_params_full(name, b, /, c=42, *args, d=67, **kwargs):
    print(f"{name=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


all_params_full("Radek", 2)
all_params_full("Radek", 2, 3)
all_params_full("Radek", 2, 3, 4, 5, 6, 7, 8, 9, 10)
all_params_full("Radek", 2, 3, 4, 5, 6, 7, 8, 9, 10, d=678)
all_params_full("Radek", 2, 3, 4, 5, 6, 7, 8, 9, 10, d=678, a=90, e=90, g=90)
# kwargs={'a': 90, 'e': 90, 'g': 90}
all_params_full("Radek", 2, 3, 4, 5, 6, 7, 8, 9, 10, d=678, a=90, e=90, g=90, name="Tomek")
# kwargs={'a': 90, 'e': 90, 'g': 90, 'name': 'Tomek'}
