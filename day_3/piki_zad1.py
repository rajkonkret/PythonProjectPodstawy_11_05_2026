# działania z plikami
# filehandler

# context manager
# with - context manager w pythonie

# w tworzy nowy plik, kasuje gdy taki istnieje
with open("test.log", "w") as file:  # pod file dostaniemy filehandler
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")
    # pass

# file.write("") # ValueError: I/O operation on closed file.

# x tworzy nowy plik
# # gdy istnieje dostajemy bład: FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x") as file:  # pod file dostaniemy filehandler
#     file.write("Powitanie\n")
#     file.write("Jeszcze jedno\n")
#     # pass
# # FileExistsError: [Errno 17] File exists: 'test.log'

# a - dodaje na koncu istniejącego pliku
with open("test.log", "a") as f:
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dodane\n")

with open('test.log', "r") as f:
    lines = f.read()

print(lines)
