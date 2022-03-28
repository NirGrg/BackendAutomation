import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params= {'AuthorName': 'Rahul Shetty2'},)
# print(response.text)
# print(type(response.text))
#
# dict_response = json.loads(response.text)
# print(dict_response[0]['isbn'])

json_response = response.json()
# print(type(json_response))
# print(json_response[0]['isbn'])
#
# print(response.status_code)
#
# assert response.status_code==200
#
# print(response.headers)
#
# assert response.headers['Content-Type']== 'application/json;charset=UTF-8'

for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        break

expectedBook = {
    'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '22755'
}

assert actualBook==expectedBook
