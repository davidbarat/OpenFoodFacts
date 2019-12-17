import requests
import mysql.connector
import random



# api-endpoint 
url = "https://fr.openfoodfacts.org/cgi/search.pl"
payload = {
    "tag_0": "pizza",
    "tag_contains_0": "contains",
    "tagtype_0": "categories",
    "sort_by": "unique_scans_n",
    "page_size": 1000,
    "page": 1,
    "action": "process",
    "json": 1
}

# data = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&json=1&search_terms2=pates-a-tartiner"
# sending get request and saving the response as response object 
r = requests.get(
    url = url,
    params = payload,
    headers = {'UserAgent': 'Project OpenFood - MacOS - Version 10.13.6'}
    )

# extracting data in json format 
data = r.json() 

# print(data)
for i in range(10):
    print(data['products'][i]['product_name'])
    print(data['products'][i]['categories'])
    print(data['products'][i]['nutriscore_grade'])
    # print(data['products'][i]['stores'])
    print(data['products'][i]['url'])
    # print(data['products'][i]['additives_n'])
    print('----')

# extracting latitude, longitude and formatted address 
# of the first matching location 
# latitude = data['results'][0]['geometry']['location']['lat'] 
# longitude = data['results'][0]['geometry']['location']['lng'] 
# formatted_address = data['results'][0]['formatted_address']



answer = input('Entrez votre nombre: ')
print(answer)
