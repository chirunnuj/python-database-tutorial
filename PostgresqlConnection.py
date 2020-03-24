import psycopg2
from Connection import Connection
from configparser import ConfigParser


class PostgresqlConnection(Connection):

    def __init__(self):
        super.__init__(self)

    def connect(self):
        try:
            # read connection parameters
            params = self.config(section='postgresql')
            self.conn = psycopg2.connect(**params)
            print('Connect to the PostgreSQL successfully')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
