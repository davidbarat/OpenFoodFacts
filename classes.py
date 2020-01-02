import mysql.connector
from mysql.connector import Error
import sys
import io


class database():

    def __init__(self):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250"
                )
        self.list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']

    def init_database(self, dbname):
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("CREATE DATABASE" + dbname)
            return True

        except mysql.connector.Error as err:
            print('Database is already created')
            return False

    def create_database(self, dbname):
        print('create_database')
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SHOW DATABASES")
        self.result = self.mycursor.fetchall()

        for i in range(len(self.result)):
	        print(self.result[i])

        with open("resources/database.sql", 'r') as self.sqlcommands:
            self.sql = self.sqlcommands.read().split(';')
            for idx, sql_request in enumerate(self.sql):
                print(sql_request + ';')
                # self.message = format(idx, sql_request)
                # print(self.message)
                self.mycursor.execute(sql_request + ';')
        self.mydb.commit()

    def populate_database(self, dbname):
        print('populate')
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )

        self.mycursor = self.mydb.cursor()
        for columns in self.list_categories:
            self.mycursor.execute(" INSERT INTO categories(category_name) values (" + columns + ");" )
        self.mydb.commit()

    def insert(self, dbname, table):
        print('insert')
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(sql_request + ';')
        self.mydb.commit()
