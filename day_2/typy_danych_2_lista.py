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


# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Dawid', 'Daniel']
#     0        1        2        3       4         5
#     -6       -5       -4      -3       -2        -1

print(lista[-2:0])  # [4:0] -> []
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Anna']

# 0 do 14
# lisat_15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok] ->  [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [start:stop:krok] ->  [0, 3, 6, 9, 12]

# wyswietlanie listę w odwrotnej kolejności
print(lista_15[::-1])
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(0, 15, 2)))  # (start, stop, krok)
# [0, 2, 4, 6, 8, 10, 12, 14]

# python nie ma typu array (tablic)
tablica = [[1, 2], [3, 4]]
print(tablica)  # [[1, 2], [3, 4]]
# numpy - biblioteka do pracy z tablicami/macierzami

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Dawid', 'Daniel']

# nadpisanie alementu na wskazanym miejscu (indeksie)
lista[2] = 'Asia'
print(lista)
# ['Radek', 'Tomek', 'Asia', 'Anna', 'Dawid', 'Daniel']

# dopisanie elementu we wskazanym miejscu (indeksie)
lista.insert(1, 'Ola')
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Asia', 'Anna', 'Dawid', 'Daniel']

lista_darek = []
lista_darek.insert(1, "Darek")
print(lista_darek)  # ['Darek']

# sprawdzenie indeksu
print(lista_darek.index("Darek"))  # index 0

# usunięcie elementu z listy po elemencie
lista.remove("Tomek")
print(lista)  # ['Radek', 'Ola', 'Asia', 'Anna', 'Dawid', 'Daniel']

# dodac element do listy taki jaki juz na niej jest
# usunąc taki element

lista.append('Asia')
print(lista)
# ['Radek', 'Ola', 'Asia', 'Anna', 'Dawid', 'Daniel', 'Asia']

lista.remove("Asia")
print(lista)  # ['Radek', 'Ola', 'Anna', 'Dawid', 'Daniel', 'Asia']

# usunięcie po indeksie
# pop() - usunie lement po indeksi i zwróci usunięty element
print(lista.pop(2))  # Anna
print(lista)
# ['Radek', 'Ola', 'Dawid', 'Daniel', 'Asia']
zmienna = lista.pop(-1)
print(zmienna)  # Asia
print(lista)  # ['Radek', 'Ola', 'Dawid', 'Daniel']

print(lista.pop())  # Daniel, usunie ostatni element

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3

b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # kopia referencji, adresu
print(lista)  # ['Radek', 'Ola', 'Dawid']
print(lista2)  # ['Radek', 'Ola', 'Dawid']

lista_copy = lista.copy()

lista.clear()  # usuniecie wszystkich elementów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Radek', 'Ola', 'Dawid']

# id() - pokazuje referencje
print(id(lista))  # 1994572615616
print(id(lista2))  # 1994572615616
print(id(lista_copy))  # 1994575496064

lista2 = lista_copy
print(lista)  # []
print(lista2)  # ['Radek', 'Ola', 'Dawid']
