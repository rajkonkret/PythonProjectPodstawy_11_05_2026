# wyjątki - błedy podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy_11_05_2026\day_3\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

# obsługa wyjątków
try:
    # print(5 / 0)
    # int("A")
    # print(2 + "Ania")
    # raise KeyError("Bład klucza")
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print("Bład:", e)
else:  # wykona się tylko wtedy gdy nie ma błedu
    print(wynik)
finally:  # wykona się zawsze
    print('Następne obliczenia')

print("Dalej...")

# Bład: 'Bład klucza'
# Dalej...

# try except - [else - finally]
