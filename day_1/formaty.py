user = "Tomek"  # str
wiek = 39  # int
liczba = 8901234321235678098  # int

wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczba zmiennoprzecinkowa

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.
# %s - string
# %d - digit
print("Witaj %d, masz teraz %s lat." % (user, wiek))
