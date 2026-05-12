# słownik - para klucz : wartość
# {'user' : 'Radek'}
# klucze nie mogą się powtarzac
# słownik jest odpowienikiem jsona
# {"name":"John", "age":30, "car":null}

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementów do słownika
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz 'wiek'
dictionary["wiek"] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}
