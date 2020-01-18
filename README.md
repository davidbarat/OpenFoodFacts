OpenFoodFacts
-----------------

## database openfoodfacts
* table produits_recupérés (refcode, aliment, catégorie, description, magasin, lien, nutriscore)
* table produits_selectionnés (barcode, substitute_barcode)
* table categorie (id_categorie, nom categories)

*FK barcode et PK id categories*

## class database
* def init:
	* creation de l'enveloppe
* def create:
	* create de la structure, .sql à jouer
* def populate_database:
    * insert des données dans les tables categories et products
	* récupération list_sql (list_product) et passage de l'instruction insert
* def select:
	* select simple avec nom table en paramètre
* def select_products_selected:
	* affiche les détails du produit selectionné
* def select_better:
	* affiche le meilleur produit (nutriscore a) de la catégorie selectionnée
* def clean_sql:
	* permet de nettoyer la requête pour l'insert dans la table produit
* def select_random_categories
	* permet de retourner les 10 produits de la catégorie sélectionnée

## class api
* def recup_info
	* payload pour appel API

## class menu
* check_answer
	* check si la réponse est bien un chiffre
* create_menu
	* création d'un menu avec en paramètre une liste

## menu à créer
1. choisir une catégorie (select * from categories)
	1. choisir un produit parmi quelques produits malsains dans cette catégorie (select * from products top 10)
	2. choisir un substitut parmi le ou les substituts proposés (select * from productions where nutriscore = a)
2. choisir d'enregistrer ou pas le substitut en favoris (insert ou pas)
3. lister les choix enregistrés (select * from products_selected)

# OpenFoodFacts project

TODO

##  Instructions

TODO

## Installing

Fork the project on your local machine and launch the script via these commands:

    pip install -r requirements.txt
    python main.py


**liste des tags json utilisés**
* code
* url
* product_name
* ingredient_text
* stores
* categories
* nutrition_grade_fr