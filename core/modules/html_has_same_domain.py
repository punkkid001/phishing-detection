import requests
from bs4 import BeautifulSoup as bs


def get_root_domain(url):
    try:
        l = url.split('/')
        if l[0] in ['http:', 'https:']:
            return ".".join(l[2].split('.')[-2:])
    except AttributeError as e:
        print(e)

    return False


def html_has_same_domain(url):
    cnt = 0
    root = get_root_domain(url)

    current_page = bs(requests.get(url).text, 'lxml')
    for tag in current_page.find_all('a'):
        in_url = get_root_domain(tag.get('href'))
        if in_url == root:
            cnt += 1

    if cnt >= 1:
        return "S"
    return "U"