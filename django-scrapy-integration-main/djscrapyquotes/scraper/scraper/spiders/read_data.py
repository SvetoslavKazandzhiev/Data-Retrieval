from django.conf import settings
settings.configure()

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Data-Retrieval.django-scrapy-integration-main.djscrapyquotes.djscrapyquotes.settings.py')
django.setup()

import mysql.connector
from django.db import connection
from MySQLdb import connect as sql_connect

from mysql.connector import Error


def data_reader():


    try:
        db_key = 'default'
        connection = mysql.connector.connect(
            host='localhost',
            database='carslistingdiscovery',
            user='root',
            port=3306,
            password=''
        )
        query = """
                SELECT url
                FROM carapp_carlistingdiscovery as cld
                where cld.parse_batch = 308
                limit 2
                # ORDER BY cld.parse_batch DESC LIMIT 0, 1
                """
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        # for l in  (list(records)):
        print([item[0] for item in list(records)])
        return list(records)
    except Error as e:
        print("Error reading data from MySQL table", e)
    # finally:
    #     if connection.is_connected():
    #         connection.close()
    #         cursor.close()
    #         print("MySQL connection is closed")

data_reader()
