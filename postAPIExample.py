import json
import requests
from payLoad import *
import configparser
from utilities.configurations import *
from utilities.resources import *

url_add = getConfig()['API']['endpoint'] + APIResources.addBook
headers = {"Content-Type": "application/json"}

addBook_response = requests.post(url_add, json=addBookPayLoad("tues"),
                                 headers=headers, )

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

book_Id = response_json['ID']

url_delete = getConfig()['API']['endpoint'] + APIResources.deleteBook
delete_book_response = requests.post(url_delete , json={
    "ID": book_Id}, headers=headers)

assert delete_book_response.status_code == 200

print(delete_book_response.json())

assert delete_book_response.json() == {'msg': 'book is successfully deleted'}

# Authentication
# base_url = "https://api.github.com/user"
# github_response = requests.get(base_url, verify=False, auth=('nirkum.90@gmail.com', 'Nir10061991'))
# print(github_response.status_code)
#
# url_1 = "https://api.github.com/user/repos"
# response = requests.get(url_1)
# print(response.status_code)

