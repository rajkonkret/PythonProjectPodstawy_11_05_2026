from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-05-13

time = datetime.now()
print(time)
# 2026-05-13 13:46:04.189174

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)
print(today.year)  # 2026

# formatowanie daty
formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 13/05/2026
print(type(formated_date))  # <class 'str'>
