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

object_data = datetime.now().strptime("13/05/2026", "%d/%m/%Y")
print(object_data)  # 2026-05-13 00:00:00
print(type(object_data))  # <class 'datetime.datetime'>

# tomorrow = today + 1
# TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-05-14

products = [
    {'sku': 1, "exp_date": today, "price": 200},
    {'sku': 2, "exp_date": today, "price": 200},
    {'sku': 3, "exp_date": tomorrow, "price": 200},
    {'sku': 4, "exp_date": today, "price": 200},
    {'sku': 5, "exp_date": tomorrow, "price": 200},
    {'sku': 6, "exp_date": today, "price": 200},
]

for p in products:
    # print(p)  # {'sku': 6, 'exp_date': datetime.date(2026, 5, 13), 'price': 200}
    # print(p["exp_date"])  # 2026-05-13

    # if p["exp_date"] == today:
    #     pass

    if p["exp_date"] != today:
        continue  # kończy bieżące wykonanie pętli, pobiera kolejny element

    print(p['price'])
    p['price'] *= 0.8  # price = price * 0.8

    print(f"""
Price for sku: {p['sku']}
is now: {p['price']:.2f} # .2f dwa miejsca po przecinku
""")
# 200
#
# Price for sku: 1
# is now: 160.00 # .2f dwa miejsca po przecinku
#
# 200
#
# Price for sku: 2
# is now: 160.00 # .2f dwa miejsca po przecinku
#
# 200
#
# Price for sku: 4
# is now: 160.00 # .2f dwa miejsca po przecinku
#
# 200
#
# Price for sku: 6
# is now: 160.00 # .2f dwa miejsca po przecinku
