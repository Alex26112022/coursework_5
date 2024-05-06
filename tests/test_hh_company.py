import requests

from src.hh_company import HhCompany


def test_hh_vacancy(monkeypatch):
    """ Проверка парсера. """

    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.url = 'https://api.hh.ru/employers/{employer_id}'
            self.headers = {'User-Agent': 'HH-User-Agent'}

        def json(self):
            return {'items': ['test1', 'test2']}

    def mock_get(url, headers):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    test_request = HhCompany(1234)
    test_request.load_info()
    assert test_request.get_info() == {'items': ['test1', 'test2']}
    print(test_request.get_info())
