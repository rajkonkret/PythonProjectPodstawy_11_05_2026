# pętla - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for _ in range(15):
    print("Test podłoga")
    print(_)  # 14

for i in range(5):
    print(i * 2)
    print(i + 2)

print("Wyjście z pętli")
# 8
# 6
# Wyjście z pętli

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# parzyste do listy
lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for i in range(len(lista3)):  # pod i mamy index
    pass
    print(lista3[i])

for c in lista3:  # podstawia kolejne elemnty z listy
    print(c)
# 0
# 2
# 4
# 6
# 8

lista_nazwy = ['Ala', 'Tomek', 'Zenek', 'Basia']
for p in lista_nazwy:
    print(p)

for c in lista3:
    if c > 4:
        print(c, "Większa niż 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze niż 4")
    print(c)  # za każdym przejściem pętli

print("Po zakończy pętli")

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # (start, stop, krok)
    print(i)
