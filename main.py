from classes import database
from classes import menu
from classes import api

list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']

my_api = api()
my_database = database()
if my_database.init_database('openfoodfacts'):
    my_database.create_database('openfoodfacts')
    for idx, i in enumerate(list_categories,1):
        list_product = my_api.get_info_from_api(i, idx)
        my_database.populate_database('openfoodfacts', list_product, i)

list_categories = my_database.select('openfoodfacts', 'categories')
menu_categories = menu()
print('Selectionnez votre categorie : ')
menu_categories.create_menu(list_categories)
answer_category = input()
while not menu_categories.check_answer(answer_category):
    print('Selectionnez votre categorie : ')
    menu_categories.create_menu(list_categories)
    answer_category = input()

list_products_selected = my_database.select_random_categories('openfoodfacts', 'products', answer_category)
menu_products = menu()
print('Selectionnez le produit que vous voulez substituez : ')
menu_categories.create_menu(list_products_selected)

# print(answer)