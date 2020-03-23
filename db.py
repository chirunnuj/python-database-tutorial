import psycopg2
from config import config


class DB:
    """ Database Manager Class"""

    def __init__(self):
        """ Initialize database connection to the PostgreSQL database server """
        self.conn = None

    def connect(self):
        """ Connect to the PostgreSQL database server """

        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            # ** Python dictionary unpacking
            self.conn = psycopg2.connect(**params)
            print('Connect to the PostgreSQL successfully')
            # create a cursor
            cur = self.conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            cur.close()

            # return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # finally:
            # if conn is not None:
            #     conn.close()
            #     print('Database connection closed.')

    def close(self):
        """ close the connection to the PostgreSQL database server """

        try:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def creat_tables(self):
        """ create tables in the PostgreSQL database """
        commands = (
            """
            CREATE TABLE IF NOT EXISTS vendors (
                vendor_id SERIAL PRIMARY KEY,
                vendor_name VARCHAR(255) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id, part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
        )

        try:
            cur = self.conn.cursor()

            print('Creating tables')
            for command in commands:
                cur.execute(command)

            # commit the changes
            self.conn.commit()

            # close communication with the PostgreSQL database server
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_vendor(self, vendor_name):
        """ insert a new vendor into the vendors table """

        sql = """INSERT INTO vendors(vendor_name)
                VALUES(%s) RETURNING vendor_id;"""

        vendor_id = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (vendor_name,))

            # retrieve the newly created vendor id
            vendor_id = cur.fetchone()[0]
            cur.close()

            # commit the changes
            self.conn.commit()

            print('A vendor has been inserted into the database succesfully')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return vendor_id

    def insert_vendor_list(self, vendor_list):
        """ insert a list of vendors into the vendors table """

        sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
        try:
            cur = self.conn.cursor()
            cur.executemany(sql, vendor_list)
            cur.close()

            self.conn.commit()

            print('Vendors have been inserted into the database successfully')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_vendor(self, vendor_id, vendor_name):
        """ update vendor_name of the vendors table """

        sql = """
                UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s
                """

        updated_rows = 0

        try:
            cur = self.conn.cursor()
            cur.execute(sql, (vendor_name, vendor_id))
            updated_rows = cur.rowcount
            self.conn.commit()
            print('The vendor has been updated')

            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return updated_rows

    # def get_vendors(self):
    #     """ get all vendors from the vendors table """

    #     try:
    #         cur = self.conn.cursor()
    #         cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
    #         print("THe number of vendors: ", cur.rowcount)
    #         row = cur.fetchone()

    #         while row is not None:
    #             print(row)
    #             row = cur.fetchone()

    #         cur.close()
