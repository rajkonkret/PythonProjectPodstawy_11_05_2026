user = "Tomek"  # str
wiek = 39  # int
liczba = 8901234321235678098  # int

wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczba zmiennoprzecinkowa

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.
# %s - string
# %d - digit

# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

# f-string -> Witaj Tomek, masz teraz 39 lat.
print(f'Witaj {user}, masz teraz {wiek} lat.')
# Witaj Tomek, masz teraz 39 lat.

# %i - liczba całkowita (integer)
# %f: formatowanie liczb zmiennoprzecinkowych

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
# zaokrągla przy wyświetlaniu
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4

x = 3.8769
print(x)
y = round(x)
print(y)  # 4
print(type(y))  # <class 'int'>

z = round(x, 2)
print(f"{z=}")  # z=3.88
print(type(z))  # <class 'float'>

print(f'Używamy wersji Pythona {wersja}')  # Używamy wersji Pythona 3.90001
print(f'Używamy wersji Pythona {wersja:.2f}')  # Używamy wersji Pythona 3.90
print(f'Używamy wersji Pythona {wersja:.1f}')  # Używamy wersji Pythona 3.9
print(f'Używamy wersji Pythona {wersja:.0f}')  # Używamy wersji Pythona 4
# print(f'Używamy wersji Pythona {wersja:.f}') # ValueError: Format specifier missing precision
