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
print(type(39)) # <class 'int'>, ineger, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)