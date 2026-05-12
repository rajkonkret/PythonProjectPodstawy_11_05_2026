# instrukcje warunkowe
# instrukcje sterowania przepływem programu

# if
# w zależnosci od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwrócic typ bool

odp = True

if odp: print("test")  # test

if odp:
    # blok programu wykonywany gdy warunek True
    print("Test")  # Test

# debugger - narzędzie do wykonywania kodu krok po kroku
# pułapka - miejsce gdzie program się zatrzyma
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"
if odp:
    print("Dane zostały wczytane")
    # Dane zostały wczytane

if odp == "Radek":  # == porównanie
    print("Jestem Radek")
# Jestem Radek

odp = 0
if odp:
    print("Działa")
else:  # w innym przypadku, wartość domyślna
    print("Zero -> False")
# Zero -> False

a = "Radek"
# jeżeli długośc tekstu jest większa niż 3 wypisac:
# Długośc wynosi: wartość, więcej niz 3

if len(a) > 3:
    print(f"Długośc wynosi: {len(a)}, więcej niż 3")

n = len(a)
if n > 3:
    print(f"Długośc wynosi: {n}, więcej niż 3")

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długośc wynosi: {n}, więcej niż 3")
# Długośc wynosi: 5, więcej niż 3

# pobrac zarobki
# jesli zarobki mniejsze do 10000 podatek 0
# dla pozostałych podatek 90% (0.9)
# wypisac obliczony podatek
# zarobki = int(input("Podaj zarobki:"))
#
# # kolejność ma znaczenie
# podatek = 0
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.6
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# Podaj zarobki:100000
# Podatek wynosi: 90000.0 pln.


sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f'Rabat wynosi: {rabat}')
# Rabat wynosi: 25

# operator warunkowy
rabat = 25 if sum_zam > 100 else 0
print(f'Rabat wynosi: {rabat}')  # Rabat wynosi: 25

# napisac test z...
# trzy pytania
# punktacja

#
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

# punkty = 0
# odp = input("Podaj rok Chrztu Polski: ")  # str
# if odp.strip().casefold() == "966":
#     print("Odpowiedź prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Masz w książce na stronie 26")
# print(punkty)
#
# odp = input("Jak Król jest na banknocie 200 zł: ")  # str
# if odp.strip().casefold() == "Zygmunt".casefold():
#     print("Odpowiedź prawidłowa")
#     punkty += 1
# else:
#     print("Masz w książce na stronie 60")
# print(punkty)
#
# odp = input("Czy koty trzeba głaskać: ")  # str
# if odp.strip().casefold() == "tak".casefold():
#     print("Odpowiedź prawidłowa")
#     punkty += 1
# else:
#     print("Masz w książce na stronie 90")
# print(punkty)
#
# print(f"Końcowy wynik: {punkty} pkt.")

# Podaj rok Chrztu Polski: 966
# Odpowiedź prawidłowa
# 1
# Jak Król jest na banknocie 200 zł: Zygmunt
# Odpowiedź prawidłowa
# 2
# Czy koty trzeba głaskać: tak
# Odpowiedź prawidłowa
# 3
# Końcowy wynik: 3 pkt.
#
# Process finished with exit code 0

# zasymulujemy system zbierania logów
# zmienna: typ systemu -> console, email inny
# console: "Stało się coś strasznego"
# email: "System email"
# do listy błedów dodac tłumaczenie błedu
# poziomy błedów: error, medium, inny

lista_b = []
alert_system = "email"
error_level = "error"

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")

else:
    print("Inny system")

print(lista_b)
# System email
# ['Krytyczny']
