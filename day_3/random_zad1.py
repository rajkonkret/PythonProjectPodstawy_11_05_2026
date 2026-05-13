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
