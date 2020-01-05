# все перенес

from datetime import time
import csv
import requests
from bs4 import BeautifulSoup as bs
import lxml
headers = {'accept':'*/*',
      'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://zaochnik.com/lenta_rabot/?page='

def za_parse(base_url, headers):
    lenta = []
    urls = []
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code ==200:
        request = session.get(base_url, headers=headers)
        soup = bs(request.content, 'lxml')
        try:
            pagination = soup.find_all('li',attrs={'class':'paginator__item'})
            count = int(pagination[-4].text)
            for i in range(count):
                url = f'https://zaochnik.com/lenta_rabot/?page={i}'
                if url not in urls:
                    urls.append(url)
        except:
            pass
    for url in urls:
        request = session.get(url, headers=headers)
        soup = bs(request.content, 'lxml')
        divs = soup.find_all('div',attrs={'class':'tape-card'})
        for div in divs:
            try:
                title = div.find('span', attrs={'class':'tape-card__type'}).text
                tile_pr = div.find('a', attrs={'class': 'tape-card__name'}).text
                href = div.find('a', attrs={'href=': ''})['href']
                lenta.append({
                    'title': title,
                    'tile_pr': tile_pr,
                    'href': href
                })
            except:
                pass

    print (lenta)
    # else:
    # print('ERROR or Done' + str(request.status_code))
    return lenta
def files_writer(lenta):
    with open('parsed_lenta.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Название', 'Предмет', 'URL'))
        for job in lenta:
            a_pen.writerow((job['title'], job['tile_pr'], job['href']))


lenta = za_parse(base_url, headers)
files_writer(lenta)
