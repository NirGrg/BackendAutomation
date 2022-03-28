import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm')
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())

moviesTable = soup.find('table', {'class': 'findList'})
# print(moviesTable)

rows = moviesTable.findAll('tr')
for row in rows:
    rowData = row.findAll('td')
    print(rowData[1].find('a').text)
    suburl = rowData[1].a['href']
    subData = requests.get('https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm'+suburl)
    childSoup = BeautifulSoup(subData.content, 'html.parser')
    genre = childSoup.find('div', {'class': 'see-more inline canwrap'})
    print(genre)