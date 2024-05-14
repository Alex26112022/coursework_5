import psycopg2

from config import config


class DBManager:
    """ Подключается к БД и собирает необходимые данные. """

    def __init__(self, db_name):
        self.conn_params = config()
        self.db_name = db_name

    def get_companies_and_vacancies_count(self, name_new_database,
                                          table_companies):
        """
        Получает список всех компаний и количество вакансий у каждой
        компании.
        """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                         SELECT company_name, company_open_vacancies
                         FROM {table_companies}
                        """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_all_vacancies(self, name_new_database, table_companies,
                          table_vacancies):
        """
        Получает список всех вакансий с указанием названия компании, названия
        вакансии и зарплаты и ссылки на вакансию.
        """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT company_name, vacancy_name, salary_from,
                        salary_to, currency, vacancy_url FROM {table_vacancies}
                        JOIN {table_companies} USING (company_id)
                        """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_avg_salary(self, name_new_database, table_companies,
                       table_vacancies, table_currency):
        """
        Получает среднюю зарплату по вакансиям.
        """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT company_name, AVG(salary_from * value / nominal)
                        AS avg_salary FROM {table_vacancies}
                        JOIN {table_companies} USING (company_id)
                        JOIN {table_currency} ON currency=char_code
                        GROUP BY {table_vacancies}.company_id,
                        {table_companies}.company_name
                        """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_vacancies_with_higher_salary(self, name_new_database,
                                         table_companies,
                                         table_vacancies, table_currency):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем
        вакансиям.
        """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT company_name, vacancy_name, vacancy_city,
                        salary_from, salary_to, currency, published,
                        vacancy_url, schedule, experience, employment, snippet
                        FROM {table_vacancies}
                        JOIN {table_companies} USING (company_id)
                        JOIN {table_currency} ON currency=char_code
                        WHERE salary_from > (SELECT AVG(salary_from)
                        FROM {table_vacancies})
                        """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_vacancies_with_keyword(self, name_new_database, table_companies,
                                   table_vacancies, keyword):
        """
        Получает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например python.
        """
        conn = psycopg2.connect(dbname=name_new_database, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT company_name, vacancy_name, vacancy_city,
                        salary_from, salary_to, currency, published,
                        vacancy_url, schedule, experience, employment, snippet
                        FROM {table_vacancies}
                        JOIN {table_companies} USING (company_id)
                        WHERE LOWER(vacancy_name) LIKE LOWER('%{keyword}%')
                        """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result


new_select = DBManager('postgres')
result_info = new_select.get_vacancies_with_keyword('hh_base',
                                                    'companies',
                                                    'vacancies',
                                                    'python')
