import pandas

# pip install pandas

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#    sku  exp_date  price
# 0    1     today    200
# 1    2     today    200
# 2    3  tomorrow    200
# 3    4     today    200
# 4    5  tomorrow    200
# 5    6     today    200

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='str')

print(data.values)
# [[1 'today' 200]
#  [2 'today' 200]
#  [3 'tomorrow' 200]
#  [4 'today' 200]
#  [5 'tomorrow' 200]
#  [6 'today' 200]]

print(data.items)
# <bound method DataFrame.items of    sku  exp_date  price
# 0    1     today    200
# 1    2     today    200
# 2    3  tomorrow    200
# 3    4     today    200
# 4    5  tomorrow    200
# 5    6     today    200>
