import psycopg2

from config import config


class DbCreate:
    """ Создает и наполняет БД. """

    def __init__(self, db_name='postgres'):
        self.conn_params = config()
        self.db_name = db_name

    def create_database(self, name_new_database='hh_base'):
        """ Создает базу данных. """
        conn = psycopg2.connect(dbname=self.db_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            try:
                cur.execute(f'CREATE DATABASE {name_new_database}')
            except psycopg2.Error:
                pass
        conn.commit()
        conn.close()

    def create_table_companies(self, name_new_database='hh_base',
                               table_name='companies'):
        """ Создает таблицу компании. """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS {table_name} (
                        company_id VARCHAR(20) PRIMARY KEY,
                        company_name VARCHAR(100),
                        company_city VARCHAR(100),
                        company_open_vacancies INTEGER,
                        company_url VARCHAR(100),
                        company_description TEXT
                        )
                        """)
        conn.commit()
        conn.close()

    def create_table_vacancies(self, name_new_database='hh_base',
                               table_name='vacancies'):
        """ Создает таблицу вакансии. """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS {table_name} (
                        vacancy_id VARCHAR(20) PRIMARY KEY,
                        company_id VARCHAR(20),
                        vacancy_name VARCHAR(100),
                        vacancy_city VARCHAR(100),
                        salary_from INTEGER,
                        salary_to INTEGER,
                        currency VARCHAR(10),
                        published TIMESTAMP,
                        vacancy_url VARCHAR(100),
                        snippet TEXT,
                        schedule VARCHAR(50),
                        experience VARCHAR(50),
                        employment VARCHAR(50),
                        company_description TEXT
                        )
                        """)
        conn.commit()
        conn.close()
