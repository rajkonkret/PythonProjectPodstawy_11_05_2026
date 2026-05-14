# dekorator
# przyjmują inną funkcję jako argument
# dodaja, zmieniają funkcjonalnosc
# wykorzystuja konstrukcję funkcji wew

def dekor(func):
    def wew():
        print("Dodatkowe działanie")
        return func()

    return wew  # zwraca adres funkcji wew


@dekor
def hej():
    print("Hej!!")


hej()
# po dodaniu dekorator:
# Dodatkowe działanie
# Hej!!

# zamimana koloru tekstu w konsoli