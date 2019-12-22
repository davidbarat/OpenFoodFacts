import mysql.connector


class database():

    def __init__(self):
        print('init')

    def create(self):

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="karen250"
            )

        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("CREATE DATABASE openfoodfacts")
