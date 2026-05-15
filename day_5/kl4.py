from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    klaso opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca - konstroktor
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy wywołac super(), super() - klasa nadrzędna

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("kokoko koko ")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po kalsie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kier kir kir")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# nie można tworzyc obiektów klasy abstrakcyjnej Ptak
# or1 = Ptak("Orzeł", 50)
# print(or1)  # <__main__.Ptak object at 0x000001F5DD3D4EC0> -> __str__
# or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("kura zielononóżka")
kur2.latam()  # Tu kura zielononóżka Ja nie latam.

or2 = Orzel("Orzel Bielik", 60)
or2.latam()  # Tu Orzel Bielik Lecę z szybkością: 60 km/h

kur2.wydaj_odglos()
or2.wydaj_odglos()
# kokoko koko
# Kier kier kir kir
