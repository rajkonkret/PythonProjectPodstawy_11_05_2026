import pandas as pd

excel_data = pd.read_excel('dane.xlsx')
print(excel_data)
#    Unnamed: 0 Sales Date Sales Person  Amount
# 0           0 2018-05-12   Sila Ahmed   60000
# 1           1 2019-12-06  Mir Hossain   50000

data = pd.DataFrame(excel_data)
print(data.columns)
print(data.values)
print(data.items)

print(data.index[-1])  # 1

print(data.columns[0])  # Unnamed: 0

print(50 * "-")
print(data['Amount'].median())  # 55000.0

# filtrowanie danych
print(data[data['Amount'] > 50_000])
#    Unnamed: 0 Sales Date Sales Person  Amount
# 0           0 2018-05-12   Sila Ahmed   60000

dane_filter = data[data['Amount'] > 50_000]

# zapis do excela
dane_filter.to_excel('dane_nowe.xlsx')