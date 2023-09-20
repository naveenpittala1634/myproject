from Oba.db_module.db_operations import MysqlDB


class RetrieveBasedOnHours:
    def time_based_data(self,hours):
        sql_query = f"SELECT * FROM sys.orders WHERE last_update_time >= NOW() - INTERVAL {hours} HOUR"
        mysqldb= MysqlDB()
        return mysqldb.fetch_data_from_db(sql_query)
# obj= RetrieveBasedOnHours()
# obj.time_based_data(10000)