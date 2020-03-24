import psycopg2
import os
from Connection import Connection
import urllib.parse as up


class ElephantConnection(Connection):

    def __init__(self):
        super().__init__()

    def connect(self):
        try:

            # read connection parameters
            params = self.config(section='elephantsql')

            up.uses_netloc.append("postgres")
            super().conn = psycopg2.connect(
                database=params['database'],
                user=params['user'],
                password=params['password'],
                host=params['host'],
                port=params['port']
            )
            print('Connect to the PostgreSQL on ElephantSQL successfully')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
