from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
from collections import defaultdict


def parser_site(filename):
    BD = defaultdict(lambda: defaultdict(list))
    soup = BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")
    data = soup.find('ul', attrs={'class': "list-of-items col4 double"}).find_all('li')

    personage = ''
    for i in data:
        if len(i) == 1:
            personage = i.get_text()
            BD[i.get_text()]
        else:
            BD[personage][i.get_text()[0]].append(
                {"name": i.get_text()[1:], 'level': i.get_text()[0], 'url_spell': i.find('a').get('href')})

    for k, v in BD.items():
        for f, g in v.items():
            f = sorted(f)
    return BD


# x = {'name': 'Животные чувства', 'level': '2', 'url_spell': 'https://dungeon.su/spells/76-beast_sense/'}


def extract(html_link):
    html = urlopen(html_link)
    soup = BeautifulSoup(html,"html.parser")
    data = soup.find('ul', attrs={'class': "params"}).find_all('li')
    card_spell = ''
    for i in data:
        if i.get('class'):
            if i.get('class')[0] == 'translate-by':
                break
        card_spell += i.get_text() + '<br>'
    return card_spell


def save_html_in_pc(html_file, name_file):
    with open(f"{name_file}.html", "w") as file:
        file.write(html_file)
    return
