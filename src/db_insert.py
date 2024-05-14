import psycopg2

from config import config


class DbInsert:
    """ Наполняет таблицы БД контентом. """

    def __init__(self, db_name):
        self.conn_params = config()
        self.db_name = db_name

    def insert_companies(self, name_new_database, table_name,
                         list_companies: list[tuple]):
        """ Наполняет таблицу компании. """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.executemany(f"""
                        INSERT INTO {table_name}
                        (company_id, company_name, company_city,
                        company_open_vacancies, company_url,
                        company_description) VALUES
                        (%s, %s, %s, %s, %s, %s)
                        """, list_companies)
        conn.commit()
        conn.close()

    def insert_vacancies(self, name_new_database, table_name,
                         list_vacancies: list[tuple]):
        """ Наполняет таблицу вакансии. """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.executemany(f"""
                        INSERT INTO {table_name}
                        (vacancy_id, company_id, vacancy_name, vacancy_city,
                        salary_from, salary_to, currency, published,
                        vacancy_url, snippet, schedule, experience,
                        employment) VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, list_vacancies)
        conn.commit()
        conn.close()

    def insert_currency(self, name_new_database, table_name,
                        list_currencies: list[tuple]):
        """ Наполняет таблицу валюты. """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        INSERT INTO {table_name}
                        (char_code, value, nominal, full_name) VALUES
                        ('RUR', 1, 1, 'Российский рубль')
                        """)
            cur.executemany(f"""
                        INSERT INTO {table_name}
                        (char_code, value, nominal, full_name) VALUES
                        (%s, %s, %s, %s)
                        """, list_currencies)
        conn.commit()
        conn.close()

    def truncate_table(self, name_new_database, table_name):
        """ Удаляет все содержимое таблицы. """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f'TRUNCATE TABLE {table_name}')
        conn.commit()
        conn.close()
