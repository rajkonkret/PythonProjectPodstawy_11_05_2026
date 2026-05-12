# krotka (tupla) - kolekcja tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jako stała - szcególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla_liczby = (43, 55, 22.34, 11, 200)
tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_imiona))  # <class 'tuple'>

# tupla jednoelemntowa
tupla_jeden = 45,  # (45,)
print(tupla_jeden)
print(type(tupla_jeden))  # <class 'tuple'>

# przy tuplach jedoelementowych PEP8 zaleca nawiasy ()
tupla_jeden = (45,)  # (45,)
print(tupla_jeden)
print(type(tupla_jeden))  # <class 'tuple'>

# usunięcie calej tupli
del tupla_jeden
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# tupla jest niemutowalna
# tupla_liczby[0] = 123
# TypeError: 'tuple' object does not support item assignment

print(tupla_imiona)
# ('Zenek', 'Marek', 'Radek', 'Ania')

print(tupla_imiona.index("Radek"))  # index numer 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długośc 4

tup = 1, 2
print(type(tup))

# a - pierwsza wartosc, b - druga wartość
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie tupli
a, b = tup
print(a, b)

# zamina miejscami eartości zmiennych
a, b = b, a
print(a, b)  # 2 1

print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3
# name1, name2, name3 = tupla_imiona # ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona  # * dowolna ilośc elementów
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

name1, *name2, name3 = tupla_imiona  # * dowolna ilośc elementów
print(name1, name2, name3)  # Zenek ['Marek', 'Radek'] Ania

*name1, name2, name3 = tupla_imiona  # * dowolna ilośc elementów
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania

# sorted() - sortownanie, zwraca nową listę
print(sorted(tupla_imiona))
# ['Ania', 'Marek', 'Radek', 'Zenek']
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania') - nie zmienia tupli!!!


