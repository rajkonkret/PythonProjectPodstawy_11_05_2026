import chardet

# pip install chardet w terminalu

# with open('test.log', "r", encoding="utf-8") as f:
#     lines = f.read()
#
# print(lines)

# odczyt binarny - rb
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Powitanie\r\nJeszcze jedno\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.8438461538461539, 'language': 'pl', 'mime_type': 'text/plain'}
# {'encoding': 'utf-8', 'confidence': 0.9572413793103448, 'language': 'pl', 'mime_type': 'text/plain'} - przy większej ilości polskich znaków
encoding = result['encoding']
print("Kodowanie:", encoding)  # Kodowanie: utf-8

print(50 * "-")
print(raw_data.decode(encoding=encoding))
# --------------------------------------------------
# Powitanie
# Jeszcze jedno
# Dodane
# Dodane
# Dośąźćdane
