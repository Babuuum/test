import requests
import unittest
from disk import create_folder

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
token = "???"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

class TestSomething(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def test_yadisk(self, folder_name = "wew"):
        short_body = requests.get(f"https://cloud-api.yandex.net/v1/disk/resources?path=/{folder_name}", headers=headers)
        create_folder(folder_name)
        self.assertEqual(str(short_body), "<Response [200]>")
        print(f"Код ответа соответствует {str(short_body)[11:14]}.")
        if str(short_body) == "<Response [200]>":
            print("Результат создания папки - папка появилась в списке файлов.")




    def tearDown(self):
        print("method tearDown")