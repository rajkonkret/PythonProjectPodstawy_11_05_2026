# napisać kalkulator
# while True
# menu z opcji
# wyświetlić ładnie wynik -> f-string
# obsłużyc wyjątki
while True:
    print("""
    1. Dodawanie
    2. Odejmowaie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj wybraną opcję:")  # str

    # if odp == 5:
    #     break
    if odp not in ['1', '2', '3', '4']:
        break

    try:
        a = float(input("Podaj pierwszą liczbę:"))
        b = float(input("Podaj drugą liczbę:"))

        if odp == "1":
            print(f"Dodawanie: {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Odejmowanie: {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Mnożenie: {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Odejmowanie: {a} / {b} = {a / b}")

        # match odp:
        #     case "1":
        #         print(f"Dodawanie: {a} + {b} = {a + b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Bład:", e)
    finally:
        print("Obliczenia zostały wykonane")

print(50 * "-")
wyr = input("Podaj wyrażenie do obliczenia:")  # 50 * 3 / 4
print(eval(wyr))
# --------------------------------------------------
# Podaj wyrażenie do obliczenia:>? 5 * 8
# 40

a = float(input("Podaj pierwszą liczbę:"))
b = float(input("Podaj drugą liczbę:"))
znak = input("Wprowadź znak: (+,-,*,/)")
wyr = f"{a} {znak} {b}"
print(eval(wyr))
# Podaj pierwszą liczbę:>? 1
# Podaj drugą liczbę:>? 2
# Wprowadź znak: (=,-,*,/)>? +
# 3.0
