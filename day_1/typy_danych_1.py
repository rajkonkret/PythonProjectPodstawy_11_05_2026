import sys

wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float

print(wiek + rok)  # 2073
print(wiek - rok)  # -1979
print(wiek * rok)  # 95222
print(wiek / rok)  # 0.02319842053307009 -> float

print(2026 / 47)  # 43.1063829787234
print(2026 // 47)  # 43, część calkowita

print(rok % wiek)  # modulo, reszta z dzielenia
print(2026 % 47)
print(43 * 47)  # 2021
print(2026 - 2021)  # 5

print(10 % 3)  # reszta 1
# ctrl shift f - wyszukiwanie w projekcie

print(wiek ** rok)  # potęgowanie

# len() - długość
# str() - rzutowanie/zamiana na tekst
print(len(str(wiek ** rok)))  # 3388

# print(len(str(wiek ** rok ** 2)))  # 3388
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999 == 0.9 fałsz
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004

# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15,
# mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# decimal() - pozwala ominąć problem zaokrąglenia

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, logiczny

print(int(True))  # 1
print(int(False))  # 0

# bool() - rzutowanie na typ logiczny
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True

print(bool("Radek"))  # True

print(bool(""))  # False

print(bool("0"))  # True

print(None)  # odpowiednik null, stan nieokreślony, nie wiem
print(bool(None))  # False

# operacje logiczne

print(40 * "-")

# and - i
print(False and True)  # False
# True and True    True
# True and False    False
# False and True    False
# False and False    False

print(30 * "-")

# or - lub
print(False or True)  # True
# True or True    True
# True or False    True
# False or True    True
# False or False    False

print(30 * "-")

# not - negacja
print(not True)
print(not False)
# ------------------------------
# False
# True

a = 6
b = 8
# > < >= <=

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 6 > 8 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 6 < 8 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 6 >= 8 = False
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 6 <= 8 = True

print(f"Porównanie {a <= b = }")  # Porównanie a <= b = True

print(f"Porównanie {a} == {b} {a == b}")  # Porównanie 6 == 8 False, czy równa się?
print(f"Porównanie {a} != {b} {a != b}")  # Porównanie 6 == 8 True, czy różne?
