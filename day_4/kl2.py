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

# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'

cz1 = Human("Radek", 45, 189, "m")
print(cz1.plec)  # m
print(cz1.imie)  # Radek
print(cz1.wiek)  # 45
print(cz1.wzrost)  # 189

cz1.powitanie()
cz1.ruszaj()