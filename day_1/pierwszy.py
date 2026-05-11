import sys

print("Hello World")
print("Witaj Świecie")
# ctrl alt l - formatowanie pep8
# cd .\day_1\ - przejscie do katologu day_1
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy_11_05_2026\day_1> python .\pierwszy.py
# Hello World
# Witaj Świecie

# ctrl / - komentarz
# print('Hello")
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy_11_05_2026\day_1\pierwszy.py", line 9
#     print('Hello")
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
#
# Process finished with exit code 1 - mamy błąd
print("Dalsza część")
# Process finished with exit code 0 - program dziła poprawnie
print("Radek")
print('Radek')
print('Radek')
print('Radek')
print('Radek')
print('Radek')
print('Radek')
# ctrl d - powielanie linijek

print('"Radek"')  # "Radek"
print('Radek \"Radek\"')  # Radek "Radek"

# type() - spradzenie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe

print("39" + "89")  # 3989 - konkatenacja, łaczy teksty
print("Radek" + "1")  # Radek1

print(39 + 89)  # 128
print(type(39))  # <class 'int'>, ineger, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# print("39" + 30)
# TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zamienai typów

# rzutowanie  typów int(), str()
print(int("39") + 30)  # 69
print("39" + str(30))  # 3930

# zmienna
# pudełko, szufladka na dane

name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

print(50 * "90")
# 9090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090
print(50 * 90)  # 4500

# podpowiedzi typów
name: str = "Radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

# mypy  - sprawzanie typów
# pip - menadżer pakietów
# pip install mypy - w terminalu
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy_11_05_2026\day_1> mypy .\pierwszy.py
# pierwszy.py:62: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:71: error: Name "name" already defined on line 58  [no-redef]
# pierwszy.py:75: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy_11_05_2026\day_1>
# mypy .\day_1\pierwszy.py
