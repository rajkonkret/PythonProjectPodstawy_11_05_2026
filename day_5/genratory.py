# generator - generuje dane
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # generuje jeden element, pamięta gdzie skonczył


kwa = kwadrat2(5)

print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print(next(kwa))  # 9

print("Zrób cokolwiek")
lista = []
lista.append("123456")
print(lista)

# Zrób cokolwiek
# ['123456']

print(next(kwa))  # 16

try:
    print(next(kwa))  # StopIteration, koniec danych
except StopIteration:
    print("koniec danych")
# koniec danych

for i in kwadrat2(10):
    print(i)
    time.sleep(1)
