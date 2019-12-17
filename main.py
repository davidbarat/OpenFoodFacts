import requests
import mysql.connector
import random



# api-endpoint 
url = "https://fr.openfoodfacts.org/cgi/search.pl"
payload = {
    "tag_0": "snack",
    "tag_contains_0": "contains",
    "tagtype_0": "categories",
    "sort_by": "unique_scans_n",
    "page": 1,
    "page_size": 20,
    "action": "process",
    "json": 1
}

# data = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&json=1&search_terms2=pates-a-tartiner"
# sending get request and saving the response as response object 
# r = requests.get(
#     url = url,
#     params = payload,
#     headers = {'UserAgent': 'Project OpenFood - MacOS - Version 10.13.6'}
#     )

# extracting data in json format 
# data = r.json() 


for i in range(20):
    r = requests.get(
        url = url,
        params = payload,
        headers = {'UserAgent': 'Project OpenFood - MacOS - Version 10.13.6'}
        )
    data = r.json()
    # print(data)
    for j in range(1, 20, 1):
        print(data['products'][j]['product_name'])
        print(data['products'][j]['categories'])
        # print(data['products'][j]['nutriscore_grade'])
        print(data['products'][j]['stores_tags'])
        print(data['products'][j]['url'])
        print(data['products'][j]['additives_n'])
        print('----')
        # print(j)
    payload['page'] = i
# answer = input('Entrez votre nombre: ')
# print(answer)