import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://xgma-excavators.ru/', auth=HTTPBasicAuth('user', 'pass'))
print(response.text)
