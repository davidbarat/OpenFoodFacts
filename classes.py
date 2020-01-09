import mysql.connector
from mysql.connector import Error
import requests
import random
import sys
import io
import re

class api():

    def __init__(self):
        # api-endpoint 
        self.list_product = []
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def get_info_from_api(self):

        self.payload = {
        "tag_0": "snack",
            "tag_contains_0": "contains",
            "tagtype_0": "categories",
            "sort_by": "unique_scans_n",
            "page": 1,
            "page_size": 5,
            "action": "process",
            "json": 1
        }

        for i in range(5):
            self.r = requests.get(
                url = self.url,
                params = self.payload,
                headers = {'UserAgent': 'Project OpenFood - MacOS - Version 10.13.6'}
                )
            self.data = self.r.json()

            for j in range(1, 5, 1):
                if not 'nutriscore_grade' in self.data['products'][j]:
                    self.data['products'][j]['nutriscore_grade'] = 'na'
                self.list_product.append(
                    (self.data['products'][j]['code'],
                    j,
                    self.data['products'][j]['product_name'],
                    self.data['products'][j]['url'],
                    self.data['products'][j]['stores_tags'],
                    self.data['products'][j]['ingredients_text_fr'],
                    self.data['products'][j]['nutriscore_grade']
                    )
                )
                # print(self.list_product)
                self.payload['page'] = i
        return(self.list_product)

class database():

    def __init__(self):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
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

    def populate_database(self, dbname, list_product):
        print('populate')
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )

        self.mycursor = self.mydb.cursor()
        for columns in self.list_categories:
            self.sql_insert = """INSERT INTO categories(category_name) values (%s);"""
            self.value = (columns)
            # self.mycursor.execute(self.sql_insert, (self.value,))
        # self.mydb.commit()
        
        self.clean_list_product = self.clean_sql(list_product)
        print('---')
        print(self.clean_list_product)
        for sql in self.clean_list_product:
            self.sql_insert ="""INSERT INTO products (
                barcode,
                id_category,
                food,
                url_food,
                store,
                description_food,
                nutriscore) values (%s, %s, %s, %s, %s, %s, %s);"""
            self.value = (sql)
            # print(self.value)
            self.mycursor.executemany(self.sql_insert, self.value)
        self.mydb.commit()

    def clean_sql(self, list_product):
        print('clean_sql')
        # list_product[5] = [w.replace("'"," ") for w in list_product[5]]
        # print(list_product)
        self.clean_desc = []
        self.new_desc = []
        self.list_david = []
        for i in list_product:
            # print(i)
            self.clean_desc = i[5].replace('"',"'")
            self.clean_desc = i[5].replace("\'"," ")
            self.new_desc.append(self.clean_desc)
            i = [i[0], i[1], i[2], i[3], i[4], self.clean_desc, i[6]]
            self.list_david.append(i)
            # self.clean_desc = f'"{a}"'
            # list_product.append(self.clean_desc)
            # print(self.clean_desc)
            # print(list_product)
        # print('---')
        # print(self.new_desc)
        # print('---')
        # for idx, i in enumerate(list_product):
            # i[5] = self.new_desc[idx]
        print('--------------------------------')
        print(self.list_david)

        return(list_product)

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

    def select(self, dbname, table):

        self.list_row = []
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        self.mycursor = self.mydb.cursor()
        self.sql_select = "SELECT * FROM %s" % table
        self.mycursor.execute(self.sql_select)
        # self.mycursor.execute("SELECT * FROM %s", (self.value, ))
        self.result = self.mycursor.fetchall()
        for row in self.result :
            self.list_row.append(row[1]) #  display data without index
        return(self.list_row)

class menu():

    def create_menu(self, list_menu):
        # print('create_menu')
        self.idx = 1
        for item in list_menu:
            print('{}'.format(self.idx) + ') ' + '{}'.format(item))
            self.idx += 1
    
    def check_answer(self, answer):
        regex = re.compile(r"[0-9]")
        if regex.match(answer):
            return True
        print('Vous devez taper un chiffre pour désigner une catégorie')
        return False