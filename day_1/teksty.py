tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>


# pula tekstów
# teksty są niemutowalne - nie zmienia oryginały, zwraca kopię
tekst.upper()  # Return a copy of the string converted to up
print(tekst)  # Witaj Świecie

# wyswietlic kopie tekstu
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)
print(tekst_upper)
print(tekst_upper)
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

print(tekst)
# Witaj Świecie
print(len(tekst))  # 13
# Witaj Świecie
# 0123456789.... numerowane od zera

print(tekst[1])  # i
print(tekst[3])  # a
print(tekst[6])  # Ś

print(tekst.index("Ś"))  # indeks 6
# "e"
print(tekst.index("e"))  # indeks 9
print(tekst.count("e"))  # występuje 2 razy

# "w"
print(tekst.lower().count("w"))  # występuje 2 razy

# Witaj Świecie
# 0123456789.... numerowane od zera
print(tekst.count('j', 0, 4))  # występuje 0 razy, z prawej strony zbiór otwarty, 0123
print(tekst.count('a', 3, 4))  # występuje 1 raz
print(tekst.count('w', 7, 9))  # występuje 1 raz

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie bialych znaków, wiodących i kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# \xhh - Znak o wartości szesnastkowej (np. \x0A reprezentuje znak nowej linii)
# \xc5\x9a -> Ś
print(type(encode_s))  # <class 'bytes'> - dane bajtowe

print(encode_s.decode('utf-8'))  # Witaj Świecie
