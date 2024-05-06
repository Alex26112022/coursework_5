import requests

from src.hh_abc import HhAbc


class HhCompany(HhAbc):
    """ Парсит дынные о компании по ее id. """
    def __init__(self, employer_id):
        self.__url = f'https://api.hh.ru/employers/{employer_id}'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'page': 0, 'per_page': 100}
        self.company = None
        print('Ждите! Идет загрузка данных...')

    def load_info(self):
        """ Загружает данные с сайта. """

        response = requests.get(self.__url, headers=self.headers)
        if response.status_code == 200:
            self.company = response.json()
        else:
            print(
                f"Request failed with status code: {response.status_code}")

    def get_info(self) -> dict:
        """ Возвращает список данных. """
        return self.company

    def __str__(self):
        return (f'Найдена компания...{self.company.get('name')}\n'
                f'ID...{self.company.get('id')}\n'
                f'Количество вакансий...'
                f'{self.company.get('open_vacancies')}\n'
                f'Территориальное расположение...'
                f'{self.company.get('area').get('name')}\n'
                f'url_hh...{self.company.get('alternate_url')}\n'
                f'url_company...{self.company.get('site_url')}')
