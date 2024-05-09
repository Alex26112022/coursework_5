from config import companies_test_path, vacancies_test_path
from src.json_worker import JsonWorker

test_worker = JsonWorker(companies_test_path, vacancies_test_path)


def test_write_companies(companies_return):
    """ Проверяет запись данных о компаниях в json-файл. """
    test_worker.write_companies(companies_return)


def test_write_vacancies(vacancies_return):
    """ Проверяет запись данных о вакансиях в json-файл. """
    test_worker.write_vacancies(vacancies_return)


def test_read_companies(companies_return):
    """ Проверяет считывание данных о компаниях с json-файла. """
    assert test_worker.company_info is None
    test_worker.read_companies()
    assert test_worker.company_info == companies_return


def test_read_vacancies(vacancies_return):
    """ Проверяет считывание данных о вакансиях с json-файла. """
    assert test_worker.vacancy_info is None
    test_worker.read_vacancies()
    assert test_worker.vacancy_info == vacancies_return


def test_get_companies():
    """ Проверяет парсинг необходимых данных с json-файла компаний
        и формирование в виде списка кортежей.
    """
    assert test_worker.get_companies_info() == [
        ('3127', 'МегаФон', 'Москва', 4199, 'https://hh.ru/employer/3127',
         'test_description'),
        ('value1', 'value2', None, None, None, None)]


def test_get_vacancies():
    """ Проверяет парсинг необходимых данных с json-файла вакансий
        и формирование в виде списка кортежей.
    """
    assert test_worker.get_vacancies_info() == [
        ('98608860',
         '3127',
         'Специалист по работе с корпоративными клиентами (чат, е-mail)',
         'Краснодар', 45500, 100000, 'RUR', '2024-05-08T12:18:10+0300',
         'https://hh.ru/vacancy/98608860',
         'Высшее или неполное высшее образование.', 'Удаленная работа',
         'Нет опыта', 'Полная занятость'),
        ('value3', None, 'value4', None, None, None, None, None, None, None,
         None, None, None)]
