OpenFoodFacts
-----------------

Le but de ce projet est de récupérer une liste de produits alimentaires, les insérer dans une base de données.
Puis via un menu interactif de substituer un produit malsain d'une catégorie par un produit sain (nutriscore à A).
Une fois le substitut proposé, vous avez la possibilité d'enregistrer votre choix afin de consulter les différents
produits substitués ultérieurement.

## Etapes principales du script
1. Le programme va créer l'enveloppe de la base et 'jouer' le .sql fourni dans le répertoire resources,
2. Puis il va interroger l'api OFF et créer une liste de produits pour chaque catégories,
3. Ensuite les produits et les catégories vont être insérés en base de données,
4. Le menu utilisateur se basera sur les catégories rentrés en base de données et proposera d'en 
sélectionner une, puis affichera dix produits malsains,
5. Le programme proposera un produit de la même catégorie mais avec un nutriscore de A,
6. Puis l'utilisateur aura le choix d'enregistrer son choix ou non et de lister ces différentes recherches
ou non.

## structure database openfoodfacts
* table products (barcode, id_category, food, url_food, store, description_food, nutriscore)
* table products_selected (barcode, substitute_barcode)
* table categories (id_categorie, category_name)

*PK id categories*

## class database
* def init:
	* creation de l'enveloppe de la bdd
* def create:
	* creation de la structure de la bdd, execution .sql à jouer
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
	* permet de nettoyer la requête pour l'insert dans la table products
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

## menu utilisateur
1. choisir une catégorie
	1. choisir un produit parmi quelques produits malsains dans cette catégorie
	2. choisir un substitut parmi le ou les substituts proposés
2. choisir d'enregistrer ou pas le substitut en favoris
3. lister les choix enregistrés

## Pre requis
* Mysql 8.0.18 + password root

##  Instructions
Vous avez la possibilité de modifier les catégories (main.py):
	list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']

Et de spécifier le nom de la base que vous désirez :
	dbname = 'openfoodfacts2'


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