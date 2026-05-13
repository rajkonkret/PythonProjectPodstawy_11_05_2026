# while - pętla sterowana warunkiem

# pętla nieskonczona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

print(50 * "-")

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# --------------------------------------------------
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

# password = input("Podaj hasło:")
# while password != "secret":  # != - różne
#     password = input("podaj hasło:")
# Podaj hasło:a
# podaj hasło:asdasfd
# podaj hasło:as
# podaj hasło:fsddfgtrhtr
# podaj hasło:secret

while (password := input("Podaj hasło:")) != "secret":
    pass
# Podaj hasło:asad
# Podaj hasło:secret
