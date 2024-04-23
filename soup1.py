"""Этот код парсит html код сайта и выводит в print в консоли"""

from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
