# słownik - para klucz : wartość
# {'user' : 'Radek'}
# klucze nie mogą się powtarzac
# słownik jest odpowienikiem jsona
# {"name":"John", "age":30, "car":null}

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementów do słownika
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz 'wiek'
dictionary["wiek"] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 50])
# dict_items([('imie', 'Radek'), ('wiek', 50)])

# nadpisanie wartości
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 50}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ['Radek', "Tomek", "Magda"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# wypisac Tomka
print(dictionary['imie'][1])  # Tomek

print(dictionary['imie'][1].lower())  # tomek
print(dictionary['imie'][::-1])  # ['Magda', 'Tomek', 'Radek']

dictionary_radek = {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}
print(dictionary_radek)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# print(dictionary_radek['Imie'])  # KeyError: 'Imie'
print(dictionary_radek['Imie'.lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary_radek.get("Imie"))  # None
print(dictionary_radek.get("Imie", "default"))  # default

print(chr(223))  # ß
# \uXXXX - Znak Unicode o wartości czteroznakowego kodu szesnastkowego
print("\u00DF")  # ß
# \N{name} - Znak Unicode o podanej nazwie
print('\N{LATIN SMALL LETTER SHARP S}')  # ß

name1 = "GROSS"  # -> gross
name2 = "groß"

print(name1.lower())
print(name1.lower() == name2.lower())  # False
"""Return a version of the string suitable for caseless comparisons."""
print(name1.casefold() == name2.casefold())  # True

dictionary.update({'data': "12-12-2045"})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50, 'data': '12-12-2045'}

dict_small = {'x': 20}
dict_small.update([("y", 3), ("z", 67)])
print(dict_small)
# {'x': 20, 'y': 3, 'z': 67}

# input() - możliwość wprowadzania danych do komputera np.: z kalwiatury

# tekst = input("Podaj imię:")
# print(tekst)
# Podaj imię:Raddek
# Raddek

# input() zwraca str
# napisac apliakcję kalkulator
a = int(input("Podaj pierwszą liczbę:"))
b = input("Podaj drugą liczbę:")
print(int(a) + float(b))
# Podaj pierwszą liczbę:5
# Podaj drugą liczbę:6
# 11.0
