import mymodule
import listFunctions
import objectOrientedModule
import pyFunctions
import sqlite3

#mymodule.greeting("Jonathan")
#listFunctions.listfunc()
#listFunctions.tupleFunctions()
#listFunctions.setFunctions()
#listFunctions.dictFunctions()
#objectOrientedModule.runme()
#pyFunctions.runme()



def dbcode():
    connection = sqlite3.connect("db/test.db");
    # this will create dababase if file not exists
    cursor = connection.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS Person
                (PID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME VARCHAR(100), 
                 HEIGHT INT)'''

    # create the table if needed
    cursor.execute(sql)


    sql = "INSERT INTO Person (NAME, HEIGHT) VALUES ('Jayanam', 174)"
    # insert new person into data
    cursor.execute(sql)
    # commit for writing to file
    connection.commit()
    sql = "SELECT * FROM Person"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print (row)
    connection.close()


dbcode()

#a = Animal("dummy")
#b = Horse("second dummy");
#a.printInfo()
#b.printInfo()




