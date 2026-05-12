# kolekcja

# lista - przechowuje dowolną ilość danych, róznego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Anna")
lista.append("Dawid")
lista.append("Daniel")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Dawid', 'Daniel']

# długość listy
print(len(lista))  # 6 elemntów

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Dawid', 'Daniel']
#     0        1        2        3       4         5

print(lista[2])  # Zenek
print(lista[4])  # Dawid

# print(lista[10])  # IndexError: list index out of range

print(lista[5])  # Daniel
print(lista[len(lista) - 1])  # Daniel
print(lista[-1])  # Daniel
print(lista[-2])  # Dawid

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Dawid', 'Daniel']
#     0        1        2        3       4         5
#     -6       -5       -4      -3       -2        -1

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] bez indeksu 3
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # ['Zenek', 'Anna', 'Dawid', 'Daniel'], z ostatnim włacznie
print(lista[2:5])  # ['Zenek', 'Anna', 'Dawid'] , bez ostatniego

print(lista[2:10])  # ['Zenek', 'Anna', 'Dawid', 'Daniel']

print(lista[15:20])  # [] - pusta kolekcja

print(lista[:])
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Dawid', 'Daniel']
