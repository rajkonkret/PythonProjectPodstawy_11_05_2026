# '{"name":"John", "age":30, "car":null}'
# json - dane typu klucz wartość
# typ wymiany danych pomiędzy klient - server
# odpowiednikiem jsona w pythonie jest słownik
# zawsze podwójne cudzysłowia
# None -> null
# {
#         "description": "\u201eName mangling\u201d to mechanizm zmiany nazwy atrybut\u00f3w klasy, kt\u00f3re s\u0105 zdefiniowane jako prywatne, co ma na celu unikni\u0119cie konflikt\u00f3w nazw w klasach pochodnych.",
#         "example": "print(\"Przyk\u0142ad do: Co to jest \u201ename mangling\u201d w Pythonie?\")",
#         "id": 30,
#         "level": "podstawowy",
#         "term": "Co to jest \u201ename mangling\u201d w Pythonie?"
#     },
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# zapis danych jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowanie po kluczu
with open('nasze_dane_sorted.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>

print("Imię pacjenta:", data['name'])
print("Wiek pacjenta:", data['age'])
# Imię pacjenta: Radek
# Wiek pacjenta: 40

# zamiana słownika na json (tekst)
json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

# zamiana jsona na słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>

print("Imię pacjenta:", dict_json['name'])
print("Wiek pacjenta:", dict_json['age'])
# Imię pacjenta: Radek
# Wiek pacjenta: 40
