class Ptak:
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
