from classes import database
from classes import menu
from classes import api

my_api = api()
list_product = my_api.get_info_from_api()
print(list_product)

my_database = database()
if my_database.init_database('openfoodfacts'):
    my_database.create_database('openfoodfacts')
my_database.populate_database('openfoodfacts', list_product)


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