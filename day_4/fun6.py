# napisac funkcję obliczającą średnią
# lista = []
# lista = "Radek"
# statistics - funkcje statystyczne np.: śrenia (mean)

def srednia(name=None, *cyfry):  # dowolna ilośc danych przekazynych pozycyjnie
    print(cyfry)  # (1, 2, 3, 4, 5, 6)

    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / avg
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"średnia dla ucznia: {name}, wynosi: {avg}")
        print(f"średnia dla ucznia: {name}, wynosi: {avg_p}")
    finally:
        print("Nastęny uczeń")


srednia()  # len() -> 0 avg /0
srednia(1, 2, 3, 4, 5, 6)
# ()
# Bład: division by zero
# Nastęny uczeń
# (1, 2, 3, 4, 5, 6)
# średnia wynosi: 3.5
# Nastęny uczeń

srednia("Radek", 5, 6, 7, 8, 5, 6)
# ("Radek", 5, 6, 7, 8, 5, 6)
name, *oceny = ("Radek", 5, 6, 7, 8, 5, 6)
# Bład: division by zero
# Nastęny uczeń
# (2, 3, 4, 5, 6)
# średnia dla ucznia: 1, wynosi: 4.0
# średnia dla ucznia: 1, wynosi: 5.0
# Nastęny uczeń
# (5, 6, 7, 8, 5, 6)
# średnia dla ucznia: Radek, wynosi: 6.166666666666667
# średnia dla ucznia: Radek, wynosi: 6.0
# Nastęny uczeń
