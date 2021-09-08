import sqlite3


def db_code():
    connection = sqlite3.connect("db/test.db");
    # this will create dababase if file not exists
    cursor = connection.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS Person
                (PID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME VARCHAR(100), 
                 HEIGHT INT)'''

    # create the table if needed
    cursor.execute(sql)

    sql1 = "INSERT INTO Person (NAME, HEIGHT) VALUES ('Jayanam', 175)"
    sql2 = "INSERT INTO Person (NAME, HEIGHT) VALUES ('Jayanam', 176)"
    sql3 = "INSERT INTO Person (NAME, HEIGHT) VALUES ('Jayanam', 178)"

    # insert new person into data
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)

    # commit for writing to file
    connection.commit()
    sql = "SELECT * FROM Person"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()
