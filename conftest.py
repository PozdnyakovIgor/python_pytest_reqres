import pytest
import requests
from functions import *


@pytest.fixture(scope='session', autouse=True)
def session_start_and_end_message():
    print('\nНачало тестовой сессии')
    yield
    print('\nКонец тестовой сессии')


@pytest.fixture(autouse=True)
def start_and_end_message():
    print('\nТест запущен')
    yield
    print('\nТест завершен')


@pytest.fixture(params=[1, 5, 11])
def response_single_user(request):
    response = requests.get(url=build_url_single_user(request.param))
    return response


@pytest.fixture
def create_user_data():
    return {'name': 'Igor', 'job': 'jobless'}


@pytest.fixture
def update_user_data():
    return {'name': 'Igor', 'job': 'best job in the world'}
