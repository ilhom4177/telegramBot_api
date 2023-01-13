import requests

TOKEN = ''
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']

# print each update
