import mysql.connector
from mysql.connector import Error
import requests
import random
import sys
import io
import re
import time

class api():

    def __init__(self):
        # api-endpoint 
        self.list_product = []
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def get_info_from_api(self, categories, index):

        self.payload = {
        "tag_0": "categories",
            "tag_contains_0": "contains",
            "tagtype_0": "categories",
            "sort_by": "unique_scans_n",
            "page": 1,
            "page_size": 20,
            "action": "process",
            "json": 1
        }
        self.list_product = []
        # self.counter = 1
        for c in range(1,6,1): # 5 pages
            self.payload['page'] = c
            self.payload['tag_0'] = categories
            for j in range(1, 19, 1): #  20 resultats par pages
                # self.payload['tag_0'] = i
                # print('-----------')
                # print(j)
                # time.sleep(1)
                # self.payload['page'] = self.counter #  nombre de pages
                self.r = requests.get(
                    url = self.url,
                    params = self.payload,
                    headers = {
                        'UserAgent':
                        'Project OpenFood - MacOS - Version 10.13.6'
                        }
                )
                self.data = self.r.json()
                # print(self.data)
                # time.sleep(1)

                if not 'nutriscore_grade' in self.data['products'][j]:
                    self.data['products'][j]['nutriscore_grade'] = 'na'
                if not 'ingredients_text_fr' in self.data['products'][j]:
                    self.data['products'][j]['ingredients_text_fr'] = 'na'
                if not 'stores_tags' in self.data['products'][j]:
                    self.data['products'][j]['stores_tags'] = 'na'
                self.list_product.append(
                    (self.data['products'][j]['code'],
                    index,
                    self.data['products'][j]['product_name'],
                    self.data['products'][j]['url'],
                    self.data['products'][j]['stores_tags'],
                    self.data['products'][j]['ingredients_text_fr'],
                    self.data['products'][j]['nutriscore_grade']
                    )

                )

        return(self.list_product)

class database():

    def __init__(self):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                )

    def init_database(self, dbname):
        self.mycursor = self.mydb.cursor()
        try:
            # print('create database')
            self.mycursor.execute("CREATE DATABASE %s " %(dbname))
            return True

        except mysql.connector.Error:
            print('Database is already created')
            return False

    def create_database(self, dbname):
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
            for sql_request in self.sql:
                print(sql_request + ';')
                # self.mycursor.execute(sql_request + ';')
                self.mycursor.execute(sql_request)

        self.mydb.commit()

    def populate_database(self, dbname, list_product, category):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )

        self.mycursor = self.mydb.cursor()
        # for columns in list_categories:
        self.sql_insert = """INSERT INTO categories (category_name) VALUES (%s);"""
        # self.value = (columns)
        print(
            'Les donnees pour la categorie '
            + category + ' sont en cours d insertion'
            )
        # self.list_category = [category]
        # print(self.list_category)
        self.mycursor.execute(self.sql_insert, (category,))
        self.mydb.commit()
        self.clean_list_product = self.clean_sql(list_product)
        self.sql_insert ="""INSERT INTO products (
            barcode,
            id_category,
            food,
            url_food,
            store,
            description_food,
            nutriscore) values (%s, %s, %s, %s, %s, %s, %s) 
            ON DUPLICATE KEY UPDATE barcode = VALUES (barcode);"""

        self.mycursor.executemany(self.sql_insert, self.clean_list_product)
        self.mydb.commit()

    def clean_sql(self, list_product):
        self.clean_desc = []
        self.clean_store = []
        self.clean_product = []
        self.list_final_product = []
        for i in list_product:
            self.clean_product = i[2].replace("\'"," ")
            self.store = ' , '.join(i[4])
            self.clean_store = self.store.replace("[","(")
            self.clean_desc = i[5].replace('"',"'")
            self.clean_desc = i[5].replace('%',' ')
            self.clean_desc = i[5].replace("\'"," ")
            i = [
                i[0],
                i[1],
                self.clean_product,
                i[3], 
                self.clean_store,
                self.clean_desc,
                i[6]]
            self.list_final_product.append(i)

        return(self.list_final_product)

    def insert(self, dbname, barcode_product_selected, 
        barcode_product_substitute):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        
        self.sql_insert ="INSERT INTO products_selected values (%s, %s); " % (barcode_product_selected, barcode_product_substitute)
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql_insert)
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
        self.result = self.mycursor.fetchall()
        for row in self.result :
            self.list_row.append(row[1]) #  display data without index
        return(self.list_row)
    
    def select_random_categories(self, dbname, table, id_category):

        self.list_row = []
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        self.mycursor = self.mydb.cursor()
        self.sql_select = "SELECT food, barcode FROM %s where id_category = %s order by rand() LIMIT 10" % (
            table, id_category)
        self.mycursor.execute(self.sql_select)
        self.result = self.mycursor.fetchall()
        for row in self.result :
            self.list_row.append(row) #  display data without index
        return(self.list_row)

    def select_better(self, dbname, id_category):
        self.list_row = []
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        self.mycursor = self.mydb.cursor()
        self.sql_select = "SELECT food, barcode, nutriscore, store, url_food FROM products where id_category = %s and nutriscore = 'a' order by rand() limit 1;" % (
            id_category)
        self.mycursor.execute(self.sql_select)
        self.result = self.mycursor.fetchall()
        self.list_product_substitute = list(self.result)
        self.products = self.list_product_substitute[0][0]
        self.substitute = self.list_product_substitute[0][1]
        print(self.result[0][0])
        print('Son indice nustriscore est de : ' + self.result[0][2])
        print('Vous pouvez vous le procurer dans le(s) magasin(s) suivants : '
            + self.result[0][3])
        return(self.result[0][1])

    def select_products_selected(self, dbname, table):
        self.list_row = []
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="karen250",
                database=dbname
                )
        self.mycursor = self.mydb.cursor()
        self.sql_select = "SELECT * FROM %s " %(table)
        self.mycursor.execute(self.sql_select)
        self.result = self.mycursor.fetchall()
        for i in self.result :
            self.list_product_substitute = list(i)
            self.products = self.list_product_substitute[0]
            self.substitute = self.list_product_substitute[1]
            print('\n')
            print('Vous avez selectionne le produit suivant : ')
            self.sql_select = "SELECT food, nutriscore FROM products where barcode = %s;" % (
                str(self.products))
            self.mycursor.execute(self.sql_select)
            self.result = self.mycursor.fetchall()
            # print(self.result)
            print(self.result[0][0])
            print('Son indice nustriscore est de : ' + self.result[0][1])
            print('Nous vous avons conseillé le produit suivant : ')
            self.sql_select = "SELECT food, nutriscore, store FROM products where barcode = %s;" % (
                str(self.substitute))
            self.mycursor.execute(self.sql_select)
            self.result = self.mycursor.fetchall()
            
            print(self.result[0][0])
            print('Son indice nustriscore est de : ' + self.result[0][1])
            print(
                'Vous pouvez vous le procurer dans le(s) magasin(s) suivants :'
                + self.result[0][2])
        return(self.list_row)

class menu():

    def create_menu(self, list_menu):
        for idx, item in enumerate(list_menu, 1):
            print('{}'.format(idx) + ') ' + '{}'.format(item))

    def check_answer(self, answer):
        regex = re.compile(r"[0-9]")
        if regex.match(answer):
            return True
        print('Vous devez taper un chiffre :')
        return False