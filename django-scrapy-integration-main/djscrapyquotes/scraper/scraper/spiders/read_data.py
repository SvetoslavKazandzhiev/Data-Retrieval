import mysql.connector
from mysql.connector import Error


class GetLastBatch:
    connection = mysql.connector.connect(
        host='localhost',
        database='carslistingdiscovery',
        user='root',
        port=3306,
        password=''
    )

    pb_query = """
                    SELECT cl.parse_batch 
                    FROM carapp_carlistingdiscovery as cl
                    ORDER BY cl.runidmodel_ptr_id DESC LIMIT 1;

                    """

    urls_query = '''
                    SELECT url
                    FROM carapp_carlistingdiscovery as cld
                    where cld.parse_batch = {}
                    limit 1
                '''

    def get_last_batch_number(self):
        cursor = self.connection.cursor()
        cursor.execute(self.pb_query)
        last_parse_batch = cursor.fetchall()
        last_parse_batch = last_parse_batch[0][0]
        return last_parse_batch

    def get_last_batch_urls(self):
        pb_number = self.get_last_batch_number()
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.urls_query.format(pb_number))
            records = cursor.fetchall()
            return list(records)

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")

get_data = GetLastBatch()
get_data.get_last_batch_number()