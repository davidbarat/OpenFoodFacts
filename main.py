import requests
import mysql.connector
import random
from classes import database
from classes import menu

# api-endpoint 
url = "https://fr.openfoodfacts.org/cgi/search.pl"
payload = {
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
    r = requests.get(
        url = url,
        params = payload,
        headers = {'UserAgent': 'Project OpenFood - MacOS - Version 10.13.6'}
        )
    data = r.json()
    # print(data)
    for j in range(1, 5, 1):
        if data['products'][j]['product_name']:
            print(data['products'][j]['product_name'])
        if data['products'][j]['categories']:
            print(data['products'][j]['categories'])
        if 'nutriscore_grade' in data['products'][j]:
            # print(data['products'][j])
            print(data['products'][j]['nutriscore_grade'])
        else:
            print('na')
        if data['products'][j]['stores_tags']:
            print(data['products'][j]['stores_tags'])
        if data['products'][j]['url']:
           print(data['products'][j]['url'])
        if data['products'][j]['ingredients_text_fr']:
           print(data['products'][j]['ingredients_text_fr'])
        print('----')
        
        # print(j)
    payload['page'] = i


my_database = database()
if my_database.init_database('openfoodfacts'):
    my_database.create_database('openfoodfacts')
    my_database.populate_database('openfoodfacts')


list_categories = my_database.select('openfoodfacts', 'categories')
menu_categories = menu()
print('Selectionnez votre categorie : ')
menu_categories.create_menu(list_categories)
answer = input()
while not menu_categories.check_answer(answer):
    print('Selectionnez votre categorie : ')
    menu_categories.create_menu(list_categories)
    answer = input()
# print(answer)