# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcje w klasie
# obiekt - instancja klasy
# klasa musi zostac najpierw zadeklarowana
# tworzenie obiektu uruchamia  metodę inicjalizującą (konstruktor) __init__
# __del__ - destruktor
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase , UpperCamelCase
class Human:
    # pass
    """
    Klasa Human opsiująca człowieka e Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


# print(print.__doc__)
# print(Human.__doc__)  # Klasa Human opsiująca człowieka e Pythonie

# pydoc - narzędzie do dokumentacji
# cd .. - wyjscie do wyższego katalogu
#  pydoc -b - serwer dokumentacji
#  pydoc -w .\kl1.py - plik html z dokumentacją

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000002998F8F4EC0>
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
#
# None

cz1.wiek = 90
cz1.imie = "Radek"
cz1.plec = "m"
print(cz1.plec)  # m
print(cz1.imie)  # Radek
print(cz1.wiek)  # 90
