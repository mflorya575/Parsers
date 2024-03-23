"""
Эта программа проходит по файлу user_agent.txt и выводит каждый user-agent с новой строки.
"""
import requests
from random import choice


url = 'http://httpbin.org/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)


