import pymysql

def get_conn():
    return pymysql.connect(
        host= "127.0.0.1",
        user= "root",
        password= "1234",
        database= "my_db",
        charset= "utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )