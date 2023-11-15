from functions import *
from requests.exceptions import JSONDecodeError
import pytest


class TestListUsers:
    """
    Тестируем получения списка пользователей
    """

    @pytest.mark.get
    @pytest.mark.parametrize('page_num, expected_result',
                             [(-2, 0),
                              (-1, 6),
                              (0, 6),
                              (1, 6),
                              (2, 6),
                              (3, 0)])
    def test_data_users_list(self, page_num, expected_result):
        assert len(send_request_list_users(page_num).json()['data']) == expected_result

    @pytest.mark.get
    @pytest.mark.parametrize('page_num', [-2, 2, 100])
    def test_get_users_list_status_code(self, page_num):
        assert send_request_list_users(page_num).status_code == 200

    @pytest.mark.get
    @pytest.mark.parametrize('page_num', [-100, 1, 2, 100])
    def test_check_page_number_match(self, page_num):
        assert send_request_list_users(page_num).json()['page'] == page_num


class TestSingleUser:
    """
    Тестируем получение информации о пользователе
    """

    @pytest.mark.get
    @pytest.mark.parametrize('user_id', [-1, 0, 13, 'qwe', 'z123', '@@__!?'])
    def test_single_user_not_found_status_code(self, user_id):
        assert send_request_single_user(user_id).status_code == 404

    @pytest.mark.get
    @pytest.mark.parametrize('user_id', [1, 5, 11, 12])
    def test_single_user_ok_status_code(self, user_id):
        assert send_request_single_user(user_id).status_code == 200

    @pytest.mark.get
    @pytest.mark.parametrize('user_id', [2, 7, 11])
    def test_single_user_id_match(self, user_id):
        assert send_request_single_user(user_id).json()['data']['id'] == user_id

    @pytest.mark.get
    def test_single_user_ok_status_code_with_params(self, response_single_user):
        assert response_single_user.status_code == 200


class TestCreateUser:
    """
    Тестируем создание нового пользователя
    """

    @pytest.mark.post
    def test_create_user(self, check, create_user_data):
        check.is_in('name', send_request_create_user(create_user_data).json())
        check.is_in('job', send_request_create_user(create_user_data).json())
        check.is_in('id', send_request_create_user(create_user_data).json())
        check.is_in('createdAt', send_request_create_user(create_user_data).json())

    @pytest.mark.post
    def test_create_user_status_code(self, create_user_data):
        assert send_request_create_user(create_user_data).status_code == 201

    @pytest.mark.post
    @pytest.mark.xfail(reason='Отсутствует запрашиваемый ключ')
    def test_check_missing_key(self, check, create_user_data):
        check.is_in('avatar', send_request_create_user(create_user_data).json())


class TestUpdateUser:
    """
    Тестируем обновление информации о пользователе
    """

    @pytest.mark.put
    def test_update_user(self, check, update_user_data):
        check.is_in('name', send_request_update_user(update_user_data).json())
        check.is_in('job', send_request_update_user(update_user_data).json())
        check.is_in('updatedAt', send_request_update_user(update_user_data).json())

    @pytest.mark.put
    def test_update_user_status_code(self, update_user_data):
        assert send_request_update_user(update_user_data).status_code == 200


class TestDeleteUser:
    """
    Тестируем удаление пользователя
    """

    @pytest.mark.delete
    def test_delete_user_status_code(self):
        assert send_request_delete_user().status_code == 204

    @pytest.mark.delete
    def test_delete_user_no_content(self):
        with pytest.raises(JSONDecodeError):
            send_request_delete_user().json()
