# instrukcje warunkowe
# instrukcje sterowania przepływem programu

# if
# w zależnosci od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwrócic typ bool

odp = True

if odp: print("test")  # test

if odp:
    # blok programu wykonywany gdy warunek True
    print("Test")  # Test

# debugger - narzędzie do wykonywania kodu krok po kroku
# pułapka - miejsce gdzie program się zatrzyma
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")
