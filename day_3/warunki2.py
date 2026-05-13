# od pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania:")

match lang.strip().casefold():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Jave")
    case "c":
        lista.append("Znam C")
    case _:  # odpowiednik else
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowania:java
# ['Znam Jave']
