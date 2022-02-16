import re
import requests
import json
from bs4 import BeautifulSoup, Tag, PageElement, NavigableString

# scraping function

def olx_scraper():
    try:
        r = requests.get('https://www.olx.pl/')
        soup = BeautifulSoup(r.content, features='html.parser')

        # The section containing header " Ogłoszenia promowane"
        # has an id "mainpageAds"

        mainAdSection = soup.find('section', id='mainpageAds')
        listAds = mainAdSection.find('ul')
        extracted = []
        for item in listAds.children:
            if isinstance(item, NavigableString):
                continue
            if isinstance(item, Tag):
                extracted.append(extractListData(item))

        with open('data.json', 'w') as fp:
            json.dump(extracted, fp)        

    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


def extractListData(listItem: PageElement):
    """
    Extract title, price, descriptionUrl
    and ImageUrl from the list data
    """
    # The element with class 'mheight' contains
    # the title and image url and decription Url
    descAndTitleElement = listItem.find(class_="mheight").a
    title = descAndTitleElement.get('title')
    imageUrl = descAndTitleElement.img.get('src')

    # The element with class 'price' contains price
    priceData = listItem.find(class_="price").text
    price = extractPrice(priceData)
  
    descriptionUrl = descAndTitleElement.get('href')
    description = scrape_description(descriptionUrl)
    return formatData(title, description, price, imageUrl)

def extractPrice(text):
    val = re.sub("[^0-9]", "", text)
    if val != '':
        return int(val)
    return 0

def scrape_description(url):
    """
    Extract description data by scraping descriptionUrl
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='html.parser')
    posdata = soup.findAll('div', attrs={'data-cy': True})

    # description data can be found in element with 
    # data attribute 'data-cy'
    # and value "ad_description"
    try:
        el = [x for x in posdata if x['data-cy'] == "ad_description"][0]
    except:
        el = 'None'
    return str(el)

def formatData(title, description, price, imageUrl):
    result = {
        'title': title,
        'description': description,
        'price': price,
        'image': imageUrl
    }
    return result

print('Starting scraping')
olx_scraper()
print('Finished scraping')
