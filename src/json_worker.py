import json

from config import companies_path, vacancies_path


class JsonWorker:
    """ Класс взаимодействия с json-файлом. """

    def __init__(self, company_path: str = companies_path,
                 vacancy_path: str = vacancies_path):
        self.vacancy_info = None
        self.company_info = None
        self.company_path = company_path
        self.vacancy_path = vacancy_path

    def write_companies(self, companies: list[dict]):
        """ Записывает данные о компаниях в json-файл. """
        with open(self.company_path, 'w', encoding='utf-8') as file_company:
            json.dump(companies, file_company, ensure_ascii=False, indent=4)

    def write_vacancies(self, vacancies: list[dict]):
        """ Записывает данные о вакансиях в json-файл. """
        with open(self.vacancy_path, 'w', encoding='utf-8') as file_vacancy:
            json.dump(vacancies, file_vacancy, ensure_ascii=False, indent=4)

    def read_companies(self):
        """ Считывает данные о компаниях с json-файла. """
        with open(self.company_path, encoding='utf-8') as f_company:
            self.company_info = json.load(f_company)

    def read_vacancies(self):
        """ Считывает данные о вакансиях с json-файла. """
        with open(self.vacancy_path, encoding='utf-8') as f_vacancy:
            self.vacancy_info = json.load(f_vacancy)

    def get_companies_info(self) -> list[tuple]:
        """ Возвращает список кортежей необходимых данных о компаниях. """
        all_companies_info = []
        if self.company_info is not None:
            for company in self.company_info:
                company_id = company.get('id')
                company_name = company.get('name')
                company_city = company.get('area')
                if company_city is not None:
                    company_city = company_city.get('name')
                company_open_vacancies = company.get('open_vacancies')
                company_url = company.get('alternate_url')
                company_description = company.get('description')
                company_information = (company_id, company_name, company_city,
                                       company_open_vacancies, company_url,
                                       company_description)
                all_companies_info.append(company_information)

        return all_companies_info

    def get_vacancies_info(self) -> list[tuple]:
        """ Возвращает список кортежей необходимых данных о вакансиях. """
        all_vacancies_info = []
        if self.vacancy_info is not None:
            for vacancy in self.vacancy_info:
                vacancy_id = vacancy.get('id')
                company_id = vacancy.get('employer')
                if company_id is not None:
                    company_id = company_id.get('id')
                vacancy_name = vacancy.get('name')
                vacancy_city = vacancy.get('area')
                if vacancy_city is not None:
                    vacancy_city = vacancy_city.get('name')
                salary_from = vacancy.get('salary')
                if salary_from is not None:
                    salary_from = salary_from.get('from')
                salary_to = vacancy.get('salary')
                if salary_to is not None:
                    salary_to = salary_to.get('to')
                currency = vacancy.get('salary')
                if currency is not None:
                    currency = currency.get('currency')
                published = vacancy.get('published_at')
                vacancy_url = vacancy.get('alternate_url')
                snippet = vacancy.get('snippet')
                if snippet is not None:
                    snippet = snippet.get('requirement')
                schedule = vacancy.get('schedule')
                if schedule is not None:
                    schedule = schedule.get('name')
                experience = vacancy.get('experience')
                if experience is not None:
                    experience = experience.get('name')
                employment = vacancy.get('employment')
                if employment is not None:
                    employment = employment.get('name')
                vacancy_information = (vacancy_id, company_id, vacancy_name,
                                       vacancy_city, salary_from, salary_to,
                                       currency, published, vacancy_url,
                                       snippet, schedule, experience,
                                       employment)
                all_vacancies_info.append(vacancy_information)
        return all_vacancies_info
