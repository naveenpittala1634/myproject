from datetime import datetime

import mysql.connector
import csv


class MysqlDB:
    def get_connection(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="sys"
        )
        cursor = conn.cursor()
        return conn, cursor

    def upload_data(self):
        conn, cursor = self.get_connection()
        # Read the CSV data
        with open("orders_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            # Insert the data into the database
            next(reader)
            cursor.execute("delete from sys.orders")
            for row in reader:
                str_row = row[:2]
                int_row = list(map(int, row[3:]))
                date_element = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                str_row.append(date_element)
                row = str_row + int_row
                cursor.execute(
                    "INSERT INTO sys.orders (item_type, order_state, last_update_time, branch, customer, price) VALUES (%s, %s, %s, %s, %s, %s)",
                    row)
                conn.commit()
            print("data insertion done")

    def fetch_data_from_db(self, sql_query):
        conn, cursor = self.get_connection()
        print("fetching_data_from_db")
        # Execute a SQL query
        cursor.execute(sql_query)
        # Fetch the results
        results = cursor.fetchall()
        for index, each_row in enumerate(results):
            results[index] = list(each_row)
            results[index][2] = str(each_row[2])
        cursor.close()
        conn.close()
        return results

    def update_datatype_for_a_column(self, results):
        for index, each_row in enumerate(results):
            each_row = list(each_row)
            each_row[2] = str(each_row[2])
            results[index] = each_row
        return results

    def fetch_data_based_on_id(self, id):
        sql_query= f'select * from sys.orders where customer={id}'
        return self.fetch_data_from_db(sql_query)

    def insert_into_db(self, data):
        data=str(data)
        print(data)
        conn, cursor = self.get_connection()
        sql_query= f'INSERT INTO sys.orders VALUES ({data})'
        print(sql_query)
        cursor.execute(sql_query)
        conn.commit()






mysqldb = MysqlDB()
# mysqldb.upload_data()
# print(mysqldb.fetch_data_from_db("select * from sys.orders"))
