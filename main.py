from config import companies_path, vacancies_path, currency_path
from src.currency import Currency
from src.db_create import DbCreate
from src.db_insert import DbInsert
from src.interactive import interactive_func
from src.json_worker import JsonWorker
from src.parser import Parser

companies_dict = {3127: 'Мегафон', 4934: 'Билайн',
                  3776: 'МТС', 1740: 'Yandex',
                  2748: 'Ростелеком', 907345: 'Лукойл',
                  2180: 'Ozon', 87021: 'WILDBERRIES',
                  3529: 'Сбер', 1373: 'Аэрофлот'}


def main():
    print('Ожидайте! Идет загрузка данных...')

    parser_info = Parser(companies_dict)
    parser_info.parser_companies()  # Парсит данные по компаниям в json.
    parser_info.parser_vacancies()  # Парсит данные по вакансиям в json.
    # Возвращает список данных по компаниям.
    companies_list = parser_info.get_all_companies()
    # Возвращает список данных по вакансиям.
    vacancies_list = parser_info.get_all_vacancies()

    json_loader = JsonWorker(companies_path, vacancies_path)
    # Записывает данные о компаниях в json-файл
    json_loader.write_companies(companies_list)
    # Записывает данные о вакансиях в json-файл.
    json_loader.write_vacancies(vacancies_list)
    # Считывает данные о компаниях с json-файла.
    json_loader.read_companies()
    # Считывает данные о вакансиях с json-файла.
    json_loader.read_vacancies()

    valuta_json = Currency(currency_path)
    # Получает актуальные данные о курсах валют с API Центробанка
    # и записывает их в json-файл.
    valuta_json.json_currency()
    # Получает данные о курсах валют из json-файла.
    valuta_json.load_json_currency()

    # Возвращает список кортежей необходимых данных о компаниях.
    companies_info = json_loader.get_companies_info()
    # Возвращает список кортежей необходимых данных о вакансиях.
    vacancies_info = json_loader.get_vacancies_info()
    # Возвращает список кортежей данных по курсам валют.
    valuta_info = valuta_json.get_currency()

    # Подключение к БД 'postgres'.
    # Если название Вашей БД отличается введите свое!
    create_manager = DbCreate('postgres')
    # Создает новую БД.
    create_manager.create_database('hh_base')
    # Создает таблицы.
    create_manager.create_table_companies('hh_base', 'companies')
    create_manager.create_table_vacancies('hh_base', 'vacancies')
    create_manager.create_table_currency('hh_base', 'currency')

    # Заполняет таблицы информацией.
    insert_info = DbInsert('postgres')
    insert_info.insert_companies('hh_base', 'companies', companies_info)
    insert_info.insert_vacancies('hh_base', 'vacancies', vacancies_info)
    insert_info.insert_currency('hh_base', 'currency', valuta_info)

    print('Данные успешно загружены!\n')

    # Запускает программу пользовательских запросов.
    interactive_func('postgres')


if __name__ == '__main__':
    main()
