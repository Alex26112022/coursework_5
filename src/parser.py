from src.hh_company import HhCompany
from src.hh_vacancy import HhVacancy


class Parser:
    """
    Класс-парсер. Собирает данные по всем заданным компаниям и их
    вакансиям.
    """

    def __init__(self, companies: dict):
        self.companies = companies
        self.all_vacancies = []
        self.all_companies = []

    def parser_vacancies(self):
        """ Собирает данные по вакансиям. """
        for el in self.companies:
            new_vacancy = HhVacancy(el)
            print(f'\tЗагрузка вакансий компании "{self.companies.get(el)}"')
            new_vacancy.load_info()
            self.all_vacancies.extend(new_vacancy.get_info())

    def parser_companies(self):
        """ Собирает данные по компаниям. """
        for company in self.companies:
            new_company = HhCompany(company)
            print(f'\tЗагрузка данных компании '
                  f'"{self.companies.get(company)}"')
            new_company.load_info()
            self.all_companies.append(new_company.get_info())

    def get_all_vacancies(self) -> list[dict]:
        """ Возвращает список данных по вакансиям. """
        return self.all_vacancies

    def get_all_companies(self) -> list[dict]:
        """ Возвращает список данных по компаниям. """
        return self.all_companies
