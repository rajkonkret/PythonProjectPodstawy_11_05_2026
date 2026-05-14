# stworzyc funkcję kantor
# ma mieć dwie wewnętrzne funkcje: eur, usd
# w zależności od parametru (if) zwróci jedną z funkcji (adres)
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} usd na {kwota * 3.60}")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur na {kwota * 4.2}")

    if waluta == "eur":
        return eur
    else:
        return usd


kantor_usd = kantor("usd")
kantor_eur = kantor("eur")
# Otwieram kantor
# Otwieram kantor

kantor_usd()
kantor_usd()
kantor_usd()
kantor_usd()
# Wymieniam 0 usd na 0.0
# Wymieniam 0 usd na 0.0
# Wymieniam 0 usd na 0.0
# Wymieniam 0 usd na 0.0

kantor_eur(1000)
kantor_eur(1000)
kantor_eur(1000)
kantor_eur()
# Wymieniam 1000 eur na 4200.0
# Wymieniam 1000 eur na 4200.0
# Wymieniam 1000 eur na 4200.0
# Wymieniam 0 eur na 0.0

kwota = input("Podaj kwote:")
kantor_eur(int(kwota))
# Wymieniam 0 eur na 0.0
# Podaj kwote:5678
# Wymieniam 5678 eur na 23847.600000000002
