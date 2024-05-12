import os
from configparser import ConfigParser

ROOT_DIR = os.path.dirname(__file__)
companies_path = os.path.join(ROOT_DIR, 'src', 'company.json')
vacancies_path = os.path.join(ROOT_DIR, 'src', 'vacancy.json')
companies_test_path = os.path.join(ROOT_DIR, 'tests', 'company_test.json')
vacancies_test_path = os.path.join(ROOT_DIR, 'tests', 'vacancy_test.json')
database_params = os.path.join(ROOT_DIR, 'src', 'database.ini')
currency_json = os.path.join(ROOT_DIR, 'src', 'currency.json')


def config(filename=database_params, section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section,
                                                               filename))
    return db
