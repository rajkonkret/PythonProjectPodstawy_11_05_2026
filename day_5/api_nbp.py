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
