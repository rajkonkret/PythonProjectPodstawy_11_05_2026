# REST API REST (Representational State Transfer)
# umożliwia szybki i zoptymalizowany dostęp do treści oraz metadanych Wikipedii w formatach maszynowych (głównie JSON).
# Działa pod ujednoliconym adresem URL dla każdej wersji językowej
# i jest mocno zintegrowany z systemem pamięci podręcznej (cache),
# co pozwala na obsługę dużego ruchu przy niskich opóźnieniach.

# GET: Pobiera dane z serwera (np. wczytanie strony).
# https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
# https://api.nbp.pl/api/exchangerates/rates/A/usd/

# klient http
import requests

# pip install requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

response = requests.get(url)
print(response)  # <Response [200]>
print(response.text)

dane = response.json()
print(type(dane))
print(dane)
# {'table': 'A', 'currency': 'dolar amerykański',
# 'code': 'USD',
# 'rates': [{'no': '093/A/NBP/2026', 'effectiveDate': '2026-05-15', 'mid': 3.6525}]}

print("Waluta:", dane['currency'])
print("Kod:", dane['code'])
# Waluta: dolar amerykański
# Kod: USD

print("Kurs:", dane['rates'][0]['mid'])  # Kurs: 3.6525
# https://github.com/public-apis/public-apis
