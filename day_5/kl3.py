# hermetyzacja

class Car:
    """
    Klasa opisująca samochód w Pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca - konstruktor
        :param model:
        :param year:
        """
        self.model = model
        self.year = year

        # name mangling
        # pole prywatne - widoczne tylko wewnątrz klasy
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car = Car("Skoda", 2026)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()

# po oznaczeniu pola jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)

car.licznik()  # Prędkość wynosi: 50 km/h
car.__predkosc = 0  # gdy pole prywatne to  nie zmieni wartości pola w tym obiekcie
# pędkośc obiektu nadal wynosi 50 !!!
car.hamuj()  #
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkość wynosi: -50 km/h, gdy pole prywatne: Prędkość wynosi: 0 km/h

# enkapsulacja- hermetyzowanie (pola prywatne) i wystawienie metod do zapisu i odczytu tzw: gettery, settery
