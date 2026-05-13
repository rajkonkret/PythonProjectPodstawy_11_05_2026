import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # od 1 do 100, int

print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.4733209816123689 float od 0 do 0.9999999
print(random.random() * 8)  # 7.692429343699482 float od 0 do 7.9999999

lista = [67, 45, 32, 68, 90, 42, 49]
print(lista[random.randrange(len(lista))])  # 68

print(random.choice(lista))  # element z listy, 90, losuje jeden element

lista_kul = list(range(1, 50))  # od 1 do 49
for _ in range(6):
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    print(kula)

print(random.choices(lista_kul, k=6))  # [15, 10, 27, 27, 24, 32], z powtórzeniami

print(random.sample(lista_kul, k=6))  # [17, 13, 22, 44, 15, 5], bez powtórzeń
print(random.sample(lista_kul, 6))  # [17, 13, 22, 44, 15, 5], bez powtórzeń
# [23, 1, 28, 41, 29, 46]
# [18, 13, 28, 39, 27, 49]
# [12, 25, 8, 44, 45, 13]
