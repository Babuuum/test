
import requests
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
token = "???"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)

