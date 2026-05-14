# napisac funkcję obliczającą średnią
# lista = []
# lista = "Radek"
# statistics - funkcje statystyczne np.: śrenia (mean)

def srednia(*cyfry):  # dowolna ilośc danych przekazynych pozycyjnie
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
        print(f"średnia wynosi: {avg}")
        print(f"średnia wynosi: {avg_p}")
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
