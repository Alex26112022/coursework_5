import json

import requests


class Currency:
    """ Класс получения валют. """

    def __init__(self, json_path):
        self.json_path = json_path
        self.currency_list = []

    def json_currency(self):
        """
        Получает актуальные данные о курсах валют с API Центробанка
        и записывает их в json-файл.
        """
        with open(self.json_path, 'w', encoding='utf-8') as file:
            response = requests.get(
                'https://www.cbr-xml-daily.ru/daily_json.js').json()
            json.dump(response, file, indent=4, ensure_ascii=False)

    def load_json_currency(self):
        """ Получает данные о курсах валют из json-файла. """
        with open(self.json_path, encoding='utf-8') as file:
            data = json.load(file).get('Valute')

        for el in data:
            charCode = el
            value = data.get(el).get('Value')
            nominal = data.get(el).get('Nominal')
            full_name = data.get(el).get('Name')
            full_information = charCode, value, nominal, full_name
            self.currency_list.append(full_information)

    def get_currency(self):
        """ Возвращает список кортежей данных по курсам валют. """
        return self.currency_list
