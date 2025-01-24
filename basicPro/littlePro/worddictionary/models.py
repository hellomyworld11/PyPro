import json
import requests
from bs4 import BeautifulSoup as bs

def create_dictionnary()->dict:
    config = get_config()
    url = config['url']
    tag = config['html_tag']

    html =  get_html(url)
    soup = parse_html(html)
    datalist = get_taglist(soup, tag)
    print(datalist)
    print("...\n")
    sinolst = datalist[0::4]
    pinyinlst =  datalist[1::4]
    rolelst = datalist[2::4]
    deflst = datalist[3::4]
    return dict(zip(sinolst, zip(pinyinlst, rolelst, deflst)))


def get_config(configname="config.json"):
    with open(configname) as f:
        return json.load(f)

def get_html(url):
    return requests.get(url).text

def parse_html(html):
    return bs(html, "html.parser")

def get_taglist(soup, tag)->list:
    findstr = soup.find_all(tag)
    return [label.get_text() for label in findstr]
