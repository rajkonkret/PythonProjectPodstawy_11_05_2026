class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # storzyc metody wypisz_wiek(), wypisz_wzrost()

    def powitanie(self):
        print(f'Nazywam się: {self.imie}')
        # print(f'Nazywam się: {cz1.imie}')
        # self - przechowuje obiekt

    # napisac metode ruszaj()
    # w zależności od płci k-m
    # ruszyłam w drogę
    # ruszyłem w drogę
    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył em w drogę")
        else:
            print("Ruszył am w drogę")

    # metoda opisowa print, str
    def __str__(self):
        return f"{self.imie}, {self.wiek}, {self.wzrost}"


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'

cz1 = Human("Radek", 45, 189, "m")
print(cz1.plec)  # m
print(cz1.imie)  # Radek
print(cz1.wiek)  # 45
print(cz1.wzrost)  # 189

cz1.powitanie()
cz1.ruszaj()

print(cz1)  # <__main__.Human object at 0x000001BE73BE6120>
# po stworzeniu metody poisowej __str__
# Radek, 45, 189
