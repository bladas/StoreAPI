import requests

import json
from bs4 import BeautifulSoup
import os

ROOT_URL = 'https://www.citrus.ua/'
ROOT_IMG = '?tab=photo'


def get_file(url):
    r = requests.get(url, stream=True)
    return r


def get_name(url):
    name = url.split('/')[-1]
    templates = os.path.abspath('media/citrus')
    path = os.path.abspath(templates)
    return path + '/' + name


def save_image(name, file_object):
    with open(name, 'bw')as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


myjson = []


def get_html(url):
    response = requests.get(url)

    return response.content


def parse_url(html):
    soup = BeautifulSoup(html, 'html.parser')

    container = soup.find('ul', class_='menu-aim')
    for item in container.find_all('a', 'href' == True)[2:-1]:
        category_url = item.get('href')
        print('Category url = ' + category_url)

        page_count = get_page_count(get_html(ROOT_URL + category_url))

        for page in range(page_count + 1):
            print('page# - ' + str(page))
            get_product(get_html(ROOT_URL + category_url + 'page_%d' % page))


def get_product(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:

        container = soup.find('div', class_='catalog__main-content')
        print('1')

        for item in container.find_all('div', class_="product-card__body"):
            category = soup.find('ul', class_='breadcrumbs')
            categoryitem = category.find_all('a')[1].text
            undercategory = soup.find('ul', class_='breadcrumbs')
            undercategoryitem = undercategory.find_all('a')[2].text
            name = item.find('div', class_='product-card__name').a.get('title')

            print('Category - ' + categoryitem)
            print('und cat - ' + undercategoryitem)
            print(name)
            price = item.find('span', class_='price').text

            print('price = ' + price)
            url = item.find('div', class_='product-card__name').a.get('href')
            # print(ROOT_URL+url+ROOT_IMG)
            get_img(get_html(ROOT_URL + url + ROOT_IMG))

            img_url = get_url_img(get_html(ROOT_URL + url + ROOT_IMG))
            ready_img = img_url.split('/')[-1]
            print(ready_img)
            myjson.append({
                'category': categoryitem,
                'undercategory': undercategoryitem,
                'name': name,
                'price': price,
                'img': ready_img,

             })


    except:
        try:

            container = soup.find('div', class_='ui-categories')
            # h1 = soup.find('h1').text

            # print('Category = ' + h1)
            for item in container.find_all('div', class_='ui-category'):
                udndercategory_url = item.a.get('href')

                # print(udndercategory_url)
                get_product(get_html(ROOT_URL + udndercategory_url))
        except:
            print('no products')


def get_page_count(html):
    soup = BeautifulSoup(html, 'html.parser')

    try:

        paggination = soup.find('div', class_='pagination-container')

        try:
            number = int(paggination.find_all('a', class_='')[-2].text)
            print('poslednyaya stranica = ' + str(number))
        except:
            number = 1

        return number
    except:
        print('tak i dumav')
        try:
            container = soup.find('div', class_='sub-categories__items')

            for item in container.find_all('div', class_='ui-category'):
                udndercategory_url = item.a.get('href')
                print(udndercategory_url)
                get_page_count(get_html(ROOT_URL + udndercategory_url))

        except:
            print('xz etogo ne budet')


def get_img(html):
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.find('ul', class_='gallery')

    img = container.find('img')
    # print(img.get('src'))
    url_img = img.get('src')
    save_image(get_name(url_img), get_file(url_img))
    print('ready')


def get_url_img(html):
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.find('ul', class_='gallery')

    img = container.find('img')
    # print(img.get('src'))
    url_img = img.get('src')

    return url_img


def save(product):
    with open('citrus.json', 'w') as f:
        json.dump(product, f)


def main():
    parse_url(get_html(ROOT_URL))
    save(myjson)


if __name__ == '__main__':
    main()
