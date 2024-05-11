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
                cur.execute(f'DROP DATABASE {name_new_database}')
                cur.execute(f'CREATE DATABASE {name_new_database}')
            except:
                cur.execute(f'CREATE DATABASE {name_new_database}')
        conn.commit()
        conn.close()
