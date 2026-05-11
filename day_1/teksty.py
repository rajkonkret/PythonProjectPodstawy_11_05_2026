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
