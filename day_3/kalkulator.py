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
