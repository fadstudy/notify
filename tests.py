# -*- coding: utf8 -*-
from datetime import datetime, timedelta
from os import path
import unittest

from requests import get

from config import API_PASSWORD, API_USERNAME, API_VERSION, BASE_DIRECTORY, \
                   FB_APP_ID, FB_APP_SECRET, HOUR
from notify import Notify


class NotifyTests(unittest.TestCase):
    def test_config_variables(self):
        assert BASE_DIRECTORY == path.abspath(path.dirname(__file__))
        assert API_VERSION is not None
        assert API_USERNAME is not None
        assert API_PASSWORD is not None
        assert HOUR is not None
        assert FB_APP_ID is not None
        assert FB_APP_SECRET is not None

    def test_class_context(self):
        with Notify() as n:
            assert n is not None

    def test_send_unauthorized_notification(self):
        test_user = '100007897087250'

        with Notify() as n:
            response = n.send_notification(user_id=test_user)

            assert response.status_code == 500

    def test_send_authorized_notifcation(self):
        test_user = '535722798'

        with Notify() as n:
            response = n.send_notification(user_id=test_user)

            assert response.status_code == 200

    def test_unauthorized_access(self):
        with Notify() as n:
            response = n.get_users(username="jeezy", password="trapl0rd")

            assert response.status_code == 403


    def test_authorized_access(self):
        with Notify() as n:
            response = n.get_users()

            assert response.status_code == 200

    def test_get_users(self):
        with Notify() as n:
            response = n.get_users()

            assert response.status_code == 200
            assert response.json()['users'] is not None

def main():
    unittest.main()

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
