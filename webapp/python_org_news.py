import requests
from bs4 import BeautifulSoup
from datetime import datetime

from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status() #обработка ошибок при вызове url
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find('ul', class_ = "list-recent-posts menu").findAll('li')
        result_news = []
        for news in news_list:
            title = news.find('a').text
            url = news.find('a')["href"]
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title=title, url=url, published=published)

def save_news(title, url, published):
    new_news = News(title=title, url=url, published=published)
    db.session.add(new_news)
    db.session.commit()
