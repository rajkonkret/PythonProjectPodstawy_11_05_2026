# funkcja lambda
# skrócony zapis funkcji
# lambda zawsze zwraca wynika -> return
# funkcja anonimowa


def odejmij(a, b):
    return a - b


print(odejmij(6, 90))  # -84

odejmij2 = lambda a, b: a - b  # return
print(odejmij2(7, 9))  # -2

# przerobic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100
