# zbior (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elemntów
# nie posiada indexu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbiór
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmiana kolejności

lista_sort = sorted(zbior)  # dostaniemy liste, zbior nie ma indeksu
print(lista_sort)  # [11, 22, 33, 44, 55, 66, 777]

lista_sort = list(zbior)
lista_sort.sort()
print(lista_sort)  # [11, 22, 33, 44, 55, 66, 777]

# pusty zbior
zb2 = set()  # tylko i wyłącznie słowkiem set()
print(zb2)  # set() - pusty zbiór

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(24)
zbior.add(24)
zbior.add(33)
zbior.add(25)

print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}