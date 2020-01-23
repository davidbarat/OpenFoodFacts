OpenFoodFacts
-----------------

The purpose of this project is to retrieve a list of a food products and then insert them into a mysql database.
Then via an interactive menu to replace an unhealthy product of a category by a healthy product (nutriscore grade A).
Once the substitute has been proposed, you can save your choice in order to consult the different
products subsequently replaced.

## Main steps of the script
1. The program will create the database structure and 'play' the .sql provided in the resources directory,
2. Then it will query the API OFF and create a list of products for each given category,
3. Then products and categories will be inserted into the database,
4. The user menu will be based on the categories entered in the database and will suggest
select one, and then display ten unhealthy products,
5. The program will offer a product of the same category but with a nutriscore of A,
6. In addition the user will have the choice to save his searchs or not, and to list his previous searches
or not.

## database structure
* table products (barcode, id_category, food, url_food, store, description_food, nutriscore)
* table products_selected (barcode, substitute_barcode)
* table categories (id_categorie, category_name)

*PK id categories*

## class database
* def init:
	* creation of the bdd envelope
* def create:
	* structure creation of the database, execution database.sql
* def populate_database:
	* insert data in the categories and products tables
	* get list_sql (list_product) and pass the insert instruction
* def select:
	* select with table name as parameter
* def select_products_selected:
	* display details of a selected product
* def select_better:
	* display the best product (nutriscore grade a) of the selected category
* def clean_sql:
	* clean up the sql query for the insert in the products table
* def select_random_categories
	* return the top 10 products of a selected category
	
## class api
* def recup_info:
	* payload for API call

## class menu
* def check_answer:
	* check if the answer is a number
* create_menu:
	* creation of a menu with a list as parameter

## User menu
1. choose a category
2. choose a product from a list of unhealthy products in this category
3. choose whether or not to save the substitute 
4. list the saved choices

## Prerequisite
* Mysql 8.0.18 + password root

##  Instructions
You can modify the categories (main.py):
	list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']

And specify the database name :

	dbname = 'openfoodfacts2'

## Installing

Fork the project on your local machine and launch the script via these commands:

    pip install -r requirements.txt
    python main.py


** list of json tags used *** code

* url
* product_name
* ingredient_text
* stores
* categories
* nutrition_grade_fr
