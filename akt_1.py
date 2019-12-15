import requests
from bs4 import BeautifulSoup as bs

headers = {'accept':'*/*',
      'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://zaochnik.com/lenta_rabot/?page=1'

def za_parse(base_url, headers):
    lenta = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code ==200:
        soup = bs(request.content, 'html.parser')
        # print(soup.h1.text)
        # print(soup.title.text)
        # print(soup)
        divs = soup.find_all('div',attrs={'class':'tape-card'})
        for div in divs:
            title = div.find('span', attrs={'class':'tape-card__type'}).text
            # print(title)
            tile_pr = div.find('a', attrs={'class': 'tape-card__name'}).text
            # print(tile_pr)
            href = div.find('a', attrs={'href=': ''})['href']
            href_za = ('https://zaochnik.com'+href)
            # print(href_za)
            lenta.append({
                'title': title,
                'tile_pr': tile_pr,
                'href_za': href_za


            })
            print(lenta)
    else:
        print('ERROR')
za_parse(base_url, headers)
