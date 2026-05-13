#
dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# klucz, wartość, pary

# wypize klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisze pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "<=>", v)
# imie <=> Radek
# nazwisko <=> Kowalski

# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.
# file

for k, v in dictionary.items():
    print(k, v, sep="<=>")
# imie<=>Radek
# nazwisko<=>Kowalski

for k, v in dictionary.items():
    print(k, v, sep="<=>", end=" | ")
# imie<=>Radek | nazwisko<=>Kowalski |

print("Radek")
# imie<=>Radek | nazwisko<=>Kowalski | Radek

print("Następna linia")
# imie<=>Radek | nazwisko<=>Kowalski | Radek
# Następna linia

pol_ang = {'pies': "dog", "kot": 'cat', "dach": "roof"}
#  zrobic słownik ang_pol

ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

# dict comprehensions
print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
