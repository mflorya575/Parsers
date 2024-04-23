from bs4 import BeautifulSoup
import requests
import lxml


with open('index.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
    print("Анализ файла с использованием менеджера контекста:\n", soup2)
