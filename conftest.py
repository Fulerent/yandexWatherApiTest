import pytest
import requests


class GetToApi:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, params=None, headers=None):
        url = self.base_address
        return requests.get(url=url, params=params, headers=headers)


@pytest.fixture(scope="session")
def req_ya_api_weather(request):
    return GetToApi(base_address="https://api.weather.yandex.ru/v2/forecast")


def pytest_addoption(parser):
    parser.addoption("--url",
                     action="store",
                     default="https://ya.ru/",
                     help="This is request url.")
    parser.addoption("--status_code",
                     action="store",
                     default=200,
                     help="Status code.")
