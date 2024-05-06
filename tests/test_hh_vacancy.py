import requests

from src.hh_vacancy import HhVacancy


def test_hh_vacancy(monkeypatch):
    """ Проверка парсера. """

    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.url = 'https://api.hh.ru/vacancies?employer_id={employer_id}'
            self.headers = {'User-Agent': 'HH-User-Agent'}
            self.params = {'page': 0, 'per_page': 100}

        def json(self):
            return {'items': ['test1', 'test2']}

    def mock_get(url, headers, params):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    test_request = HhVacancy(1234)
    test_request.load_info()
    assert len(test_request.get_info()) == 40
    print(test_request)
