import db

if __name__ == '__main__':
    # create database connection
    conn = db.connect()

    # create tables if they are not exist
    db.creat_tables(conn)

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
    db.close(conn)
