# Базовые функции для запросов к сервису https://reqres.in/
# https://reqres.in/api-docs/

import requests
from requests import Response


BASE_URL = 'https://reqres.in/api/'


def build_url_list_users(page_num: int) -> str:
    url = f"{BASE_URL}users?page={page_num}"
    return url


def build_url_single_user(user_id: int) -> str:
    url = f"{BASE_URL}users/{user_id}"
    return url


def build_url_create_user() -> str:
    url = f"{BASE_URL}users"
    return url


def build_url_update_user() -> str:
    url = f"{BASE_URL}users/"
    return url


def send_request_list_users(page_num: int) -> Response:
    response = requests.get(url=build_url_list_users(page_num))
    return response


def send_request_single_user(user_id: int) -> Response:
    response = requests.get(url=build_url_single_user(user_id))
    return response


def send_request_create_user(user_data: dict) -> Response:
    response = requests.post(url=build_url_create_user(), data=user_data)
    return response


def send_request_update_user(user_data: dict) -> Response:
    response = requests.put(url=build_url_update_user(), data=user_data)
    return response


def send_request_delete_user() -> Response:
    response = requests.delete(url=build_url_update_user())
    return response
