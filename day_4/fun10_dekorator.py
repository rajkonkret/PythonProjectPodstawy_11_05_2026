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

# print("\033[31mHello\033[0m")

from colorama import init, Fore, Style

init(autoreset=True)


def color_decorator(fun):
    def wrapper():
        result = fun()
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


@color_decorator
def napis():
    return "Hello WOrld!!!"


print(napis())
