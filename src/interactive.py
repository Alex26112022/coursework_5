from src.db_manager import DBManager


def interactive_func(db_name):
    """ Взаимодействие с пользователем. """
    # Создаем подключение. Если название Вашей БД отличается введите свое!
    while True:
        db_manager = DBManager(db_name)

        print('Укажите требуемую выборку или наберите exit для '
              'выхода...')
        print('\t1. Получить список всех компаний и количество вакансий у '
              'каждой компании.\n'
              '\t2. Получить список всех вакансий с указанием названия '
              'компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
              '\t3. Получить среднюю зарплату по вакансиям.\n'
              '\t4. Получить список всех вакансий, у которых зарплата выше '
              'средней по всем вакансиям.\n'
              '\t5. Получить список всех вакансий, в названии которых '
              'содержатся переданные в метод слова, например python.\n')

        input_user = input()

        if input_user.lower().strip() == 'exit':
            break
        else:
            if input_user == '1':
                res = db_manager.get_companies_and_vacancies_count('hh_base',
                                                                   'companies')
                for el in res:
                    print(f'"{el[0]}". Количество открытых вакансий: {el[1]}')
                print('')
            elif input_user == '2':
                res = db_manager.get_all_vacancies('hh_base', 'companies',
                                                   'vacancies')
                for el in res:
                    print(
                        f'"{el[0]}": {el[1]}. Минимальная зарплата: {el[2]}. '
                        f'Максимальная зарплата: {el[3]}. Валюта: {el[4]}. '
                        f'URL: {el[5]}')
                print('')
                print(f'Количество найденных вакансий: {len(res)}.\n')
            elif input_user == '3':
                res = db_manager.get_avg_salary('hh_base', 'companies',
                                                'vacancies', 'currency')
                for el in res:
                    print(f'"{el[0]}". Средняя зарплата: {el[1]} RUR')
                print('')
            elif input_user == '4':
                res = db_manager.get_vacancies_with_higher_salary('hh_base',
                                                                  'companies',
                                                                  'vacancies',
                                                                  'currency')
                for el in res:
                    print(f'"{el[0]}": {el[1]}.\n'
                          f'Город: {el[2]}. Мин.зарплата: {el[3]}. '
                          f'Макс.зарплата: {el[4]}. Валюта: {el[5]}. Дата '
                          f'публикации: {el[6]}.\n'
                          f'URL: {el[7]}. График: {el[8]}. Опыт: {el[9]}. '
                          f'Тип занятости: {el[10]}.\n'
                          f'Требования: {el[11]}\n')
                print('')
                print(f'Количество найденных вакансий: {len(res)}.\n')
            elif input_user == '5':
                user_keyword = input('Введите ключевое слово!\n')
                res = db_manager.get_vacancies_with_keyword('hh_base',
                                                            'companies',
                                                            'vacancies',
                                                            user_keyword)
                for el in res:
                    print(f'"{el[0]}": {el[1]}.\n'
                          f'Город: {el[2]}. Мин.зарплата: {el[3]}. '
                          f'Макс.зарплата: {el[4]}. Валюта: {el[5]}. Дата '
                          f'публикации: {el[6]}.\n'
                          f'URL: {el[7]}. График: {el[8]}. Опыт: {el[9]}. '
                          f'Тип занятости: {el[10]}.\n'
                          f'Требования: {el[11]}\n')
                print('')
                print(f'Количество найденных вакансий: {len(res)}.\n')
