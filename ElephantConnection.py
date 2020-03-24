import psycopg2
from connection import Connection

class ElephantConnection(Connection):

    def __init__(self):
        super.__init__(self)
    
    def connect(self):
        try:
            # read connection parameters
            params = self.config(section='elephantsql')
            self.conn = psycopg2.connect(**params)
            print('Connect to the PostgreSQL successfully')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        