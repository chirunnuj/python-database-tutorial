from db import DB
from ElephantConnection import ElephantConnection
from PostgresqlConnection import PostgresqlConnection

if __name__ == '__main__':

    # create database manager object
    # db_manager = DB()
    # db_manager.connect()
    # db_manager.update_vendor(3, 'AKM Semiconductor Incorporation')
    # db_manager.close()

    # use postgresql on Elephant
    ele = ElephantConnection()
    ele.connect()
    db_manager = DB(ele)
    db_manager.creat_tables()
    ele.close()

    # create database connection
    # conn = db.connect()

    # create tables if they are not exist
    # db.creat_tables(conn)

    # insert vendors
    # db.insert_vendor(conn, "3M Co.")

    # insert multiple vendors
    # db.insert_vendor_list(conn, [
    #     ('AKM Semiconductor Inc.',),
    #     ('Asahi Glass Co Ltd.',),
    #     ('Dailin Industries Ltd.',),
    #     ('Dynacast International Inc.',),
    #     ('Foster Electric Co. Ltd.',),
    #     ('Murata Manufacturing Co. Ltd.',)
    # ])

    # close the database connection
    # db.close(conn)
