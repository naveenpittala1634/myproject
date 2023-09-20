from faker import Faker
from datetime import datetime
import pandas as pd

fake = Faker()
# Create a list of 100 rows
rows = []
for i in range(10000):
    row = [
        fake.random_element(["Cake", "Cookies", "Muffins"]),
        fake.random_element(["Created", "Shipped", "Delivered", "Canceled"]),
        fake.date_time(),
        fake.random_int(min=1, max=1000),
        fake.random_int(min=1001, max=2000),
        fake.random_int(min=100, max=999),
    ]
    rows.append(row)

# Print the sample data

for i in rows:
    if i[0] =="Cake":
        i[5]=500
    elif i[0]=="Cookies":
        i[5]=50
    else:
        i[5]=100
print(rows)


df= pd.DataFrame(rows)
df.to_csv('output.csv', index=False)