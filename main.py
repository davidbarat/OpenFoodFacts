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

list_products_selected = my_database.select_random_categories('openfoodfacts',
    'products', answer_category)
menu_products = menu()
print('Selectionnez le produit que vous voulez substituer : ')
menu_categories.create_menu(list_products_selected)
answer_product = input()
while not menu_categories.check_answer(answer_product):
    print('Selectionnez le produit que vous voulez substituer : ')
    menu_categories.create_menu(list_products_selected)
    answer_product = input()
id_answer_product = int(answer_product)
# print(list_products_selected)
barcode_product_selected = list_products_selected[id_answer_product][1]
# print(barcode_product_selected)

print('Nous vous conseillons le produit sain suivant : ')
barcode_product_substitute = my_database.select_better('openfoodfacts', answer_category)
print(barcode_product_substitute)
print('Souhaitez vous enregistrer votre choix ? (o/n)')
answer_record = input()
if answer_record == 'o':
    my_database.insert('openfoodfacts', barcode_product_selected, 
        barcode_product_substitute)
elif answer_record == 'n':
    print('Bonne journée')
else:
    print('Vous devez taper o ou n ')    

print('Souhaitez vous revoir vos précédentes recherches ? (o/n)')
answer_research = input()
if answer_research == 'o':
    my_database.select('openfoodfacts', 'products_selected')
else:
    print('Bonne journée')
