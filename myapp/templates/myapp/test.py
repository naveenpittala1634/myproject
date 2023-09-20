import datetime
result = [('Cookies', 'Delivered', datetime.datetime(2012, 5, 3, 9, 4, 53), 115, 1928, 50),
          ('Cookies', 'Delivered', datetime.datetime(2012, 5, 2, 9, 4, 53), 115, 1928, 50)]
# date_list= [each_row[2].strftime('%Y-%m-%d %H:%M:%S')() for each_row in result]
# print(result)
for index, each_row in enumerate(result):
    each_row = list(each_row)
    each_row[2] = str(each_row[2])
    result[index] = each_row
print(result)
