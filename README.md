# OpenFoodFacts


database openfoodfacts
une table produits_recupérés (id, aliment, catégorie, description, magasin, lien)
          produits_selectionnés (choix aliments, substitus sélectionnés)

clé etrangère aliment


class database
	def create
	def select
	def insert
	def truncate


create menu
(1) choisir une catégorie
	(1.2) choisir un produit parmi quelques produits malsains dans cette catégorie 
	(1.3) choisir un substitut parmi le ou les substituts proposés
(2) choisir d'enregistrer ou pas le substitut en favoris


tags json
code
url
product_name
ingredient_text
stores
categories
nutrition_grade_fr
additives_n
