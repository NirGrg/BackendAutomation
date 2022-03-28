import requests
from bs4 import BeautifulSoup

# url = requests.get('https://rahulshettyacademy.com/AutomationPractice/')
# data = BeautifulSoup(url.content, 'html.parser')
#
# courseTable = data.find('table', {'id':'product'})
#
# rows = courseTable.findAll('tr')
# # print(rows)
# # print(courseTable)
# for row in rows:
#     rowData = row.findAll('td')
#     rowData.find('td').text

url = requests.get('https://jira.ncontext.com/browse/UEBT-1507')
print(url.status_code)
data = BeautifulSoup(url.content, 'html.parser')
# print(data)

productTable = data.find_all('table', {'id': 'exec-entries-table'})
print(productTable)