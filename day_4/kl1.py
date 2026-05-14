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

    def powitanie(self):
        print(f'Nazywam się: {self.imie}')
        # print(f'Nazywam się: {cz1.imie}')
        # self - przechowuje obiekt

    # napisac metode ruszaj()
    # w zależności od płci k-m
    # ruszyłam w drogę
    # ruszyłem w drogę


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

cz1.powitanie()  # Nazywam się: Radek

# drugi obiekt tej klasy, odmiennej płci

cz2 = Human()
cz2.imie = 'Anna'
cz2.wiek = 45
print(cz2.plec)
print(cz2.imie)
print(cz2.wiek)
# k
# Anna
# 45

cz2.powitanie()  # Nazywam się: Anna

cz1.ruszaj()
cz2.ruszaj()