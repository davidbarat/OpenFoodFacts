from classes import database
from classes import menu
from classes import api

list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']
dbname = 'openfoodfacts2'
my_api = api()
my_database = database()
db_exists = my_database.init_database(dbname)
if db_exists:
    my_database.create_database(dbname)
    for idx, category in enumerate(list_categories, 1):
        # print(i)
        list_product = my_api.get_info_from_api(category, idx)
        my_database.populate_database(dbname, list_product, category)

list_categories = my_database.select(dbname, 'categories')
menu_categories = menu()
print('Selectionnez votre categorie : \n')
menu_categories.create_menu(list_categories)
answer_category = input()
while not menu_categories.check_answer(answer_category) or int(
    answer_category) > len(list_categories):
    print('Selectionnez votre categorie : \n')
    menu_categories.create_menu(list_categories)
    answer_category = input()

list_products_selected = my_database.select_random_categories(dbname,
    'products', answer_category)
menu_products = menu()
# print(list_products_selected)
list_products_selected_name = [i[0] for i in list_products_selected]
print('Selectionnez le produit que vous voulez substituer : \n')
menu_categories.create_menu(list_products_selected_name)
answer_product = input()
while not menu_categories.check_answer(answer_product) or int(
    answer_product) > len(list_products_selected):
    print('Selectionnez le produit que vous voulez substituer : ')
    menu_categories.create_menu(list_products_selected)
    answer_product = input()
id_answer_product = int(answer_product) - 1 #  index de la liste -1
# print(list_products_selected)
barcode_product_selected = list_products_selected[id_answer_product][1]
# print(barcode_product_selected)

print('Nous vous conseillons le produit sain suivant : ')
barcode_product_substitute = my_database.select_better(dbname, 
    answer_category)
# print(barcode_product_substitute)
print('Souhaitez vous enregistrer votre choix ? (o/n)')
answer_record = input()
if answer_record == 'o':
    my_database.insert(dbname, barcode_product_selected, 
        barcode_product_substitute)
elif answer_record == 'n':
    print('\n')
else:
    print('Vous devez taper o ou n ')    

print('Souhaitez vous revoir vos précédentes recherches ? (o/n)')
answer_research = input()
if answer_research == 'o':
    my_database.select_products_selected(dbname, 'products_selected')
else:
    print('\n')
