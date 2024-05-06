import requests

from src.hh_abc import HhAbc


class HhVacancy(HhAbc):
    """ Парсит дынные о вакансиях компании по ее id. """

    def __init__(self, employer_id):
        self.__url = f'https://api.hh.ru/vacancies?employer_id={employer_id}'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'page': 0, 'per_page': 100}
        self.vacancies = []
        print('Ждите! Идет загрузка данных...')

    def load_info(self):
        """ Загружает данные с сайта. """
        while self.params.get('page') != 20:
            response = requests.get(self.__url, headers=self.headers,
                                    params=self.params)
            if response.status_code == 200:
                company_info = response.json().get('items')
                for el in company_info:
                    self.vacancies.append(el)
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
            self.params['page'] += 1

    def get_info(self) -> list:
        """ Возвращает список данных. """
        return self.vacancies

    def __str__(self):
        return f'Найдено вакансий...{len(self.vacancies)}'
