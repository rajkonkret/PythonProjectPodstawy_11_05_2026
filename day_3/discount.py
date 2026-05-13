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

# 13:50
# 13:50:56
# 1:50 pm

# formated_time = datetime.now().strftime("%H:%M:%S")
formated_time = datetime.now().strftime("%I:%M:%S %p")
print(formated_time)  # 13:53:43, 01:54:41 PM
print(type(formated_time))  # <class 'str'>
