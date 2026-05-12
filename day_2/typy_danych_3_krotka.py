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

