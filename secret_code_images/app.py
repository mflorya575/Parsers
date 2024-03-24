"""
Этот код парсит картнки с сайта https://parsinger.ru/img_download/index.html и заносит в данную папку
(если хотите, можно занести в какую-то другую папку)
"""
import requests

for i in range(1, 161):
    url = f'http://parsinger.ru/img_download/img/ready/{i}.png'
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'image_{i}.png', 'wb') as image_file:
            image_file.write(response.content)
            print(f'Изображение {i}.png скачано успешно.')
    else:
        print(f'Не удалось скачать изображение {i}.png. Код состояния: {response.status_code}')
