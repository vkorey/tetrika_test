import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as urlparse
from urllib.parse import parse_qs

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
r = requests.get(url).text
result = {}
anm = []
result = {}
letter_flag = True


def get_soup(url):
    r = requests.get(url)
    soup = bs(r.text, "lxml")
    return soup


def get_letters(soup):
    for link in soup.select(
        "#mw-content-text > div.mw-parser-output > table > tbody > tr"
    ):
        link_list = [url["href"] for url in link.select("a", class_="external text")]
        urls = link_list[2:31]
    letters = []
    for url in urls:
        parsed = urlparse.urlparse(url)
        letters.append(parse_qs(parsed.query)["from"][0])
    return letters


def get_animal_names(soup):
    for name in soup.select("#mw-pages > div > div"):
        name_list = [nm.text for nm in name.select("li")]
        return name_list


letters = get_letters(get_soup(url))

while letter_flag is True:
    soup = get_soup(url)
    name_list = get_animal_names(soup)
    if (name_list[0][0]) in letters:
        anm.extend(name_list)
    elif (name_list[0][0]) not in letters:
        letter_flag = False
        for letter in letters:
            count = 0
            for name in anm:
                if name[0] == letter:
                    count += 1
            result[letter] = count
        print(result)
    links = soup.find("div", id="mw-pages").find_all("a")
    for a in links:
        if a.text == "Следующая страница":
            url = "https://ru.wikipedia.org/" + a.get("href")
