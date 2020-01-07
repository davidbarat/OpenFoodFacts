OpenFoodFacts
-----------------

database openfoodfacts:
    * table produits_recupérés (refcode, aliment, catégorie, description, magasin, lien, nutriscore)
    * table produits_selectionnés (choix aliments, substitus sélectionnés)
	* table categorie (id, nom categories)

clé etrangère aliment

## class database
	* def init
		creation de l'enveloppe
	* def create
		create de la structure, .sql à jouer
	* def populate_database
        insert des données dans les tables categories et products
		récupération list_sql (list_product) et passage de l'instruction insert
	* def select
		select simple avec nom table en paramètre

## class api
    * def recup_info
		payload pour appel API


create menu
(1) choisir une catégorie
	(1.2) choisir un produit parmi quelques produits malsains dans cette catégorie 
	(1.3) choisir un substitut parmi le ou les substituts proposés
(2) choisir d'enregistrer ou pas le substitut en favoris

# OpenFoodFacts project

TODO

##  Instructions

TODO 

## Installing

Fork the project on your local machine and launch the game with the command below :

    pip install -r requirements.txt
    python main.py


tags json
code
url
product_name
ingredient_text
stores
categories
nutrition_grade_fr
additives_n

