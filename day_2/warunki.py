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
zarobki = int(input("Podaj zarobki:"))

# kolejność ma znaczenie
podatek = 0
if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.6
else:
    podatek = 0.9

print(f"Podatek wynosi: {zarobki * podatek} pln.")
# Podaj zarobki:100000
# Podatek wynosi: 90000.0 pln.
