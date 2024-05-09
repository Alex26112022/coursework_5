import pytest

test_companies_info = [
    {
        "id": "3127",
        "name": "МегаФон",
        "type": "company",
        "description": "test_description",
        "alternate_url": "https://hh.ru/employer/3127",
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3127",
        "relations": [],
        "area": {
            "name": "Москва"},
        "open_vacancies": 4199
    },
    {'id': 'value1', 'name': 'value2'}]

test_vacancies_info = [
    {
        "id": "98608860",
        "name": "Специалист по работе с корпоративными клиентами "
                "(чат, е-mail)",
        "area": {
            "name": "Краснодар",
        },
        "salary": {
            "from": 45500,
            "to": 100000,
            "currency": "RUR",
        },
        "published_at": "2024-05-08T12:18:10+0300",
        "alternate_url": "https://hh.ru/vacancy/98608860",
        "employer": {
            "id": "3127",
        },
        "snippet": {
            "requirement": "Высшее или неполное высшее образование."
        },
        "schedule": {
            "name": "Удаленная работа"
        },
        "experience": {
            "name": "Нет опыта"
        },
        "employment": {
            "name": "Полная занятость"
        },
    },
    {'id': 'value3', 'name': 'value4'}]


@pytest.fixture
def companies_return():
    """ Возвращает данные по компаниям в виде списка словарй. """
    return test_companies_info


@pytest.fixture()
def vacancies_return():
    """ Возвращает данные по вакансиям в виде списка словарй. """
    return test_vacancies_info
