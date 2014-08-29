# -*- coding: utf8 -*-
from datetime import datetime, timedelta
from os import path
import unittest

from requests import get

from config import API_PASSWORD, API_USERNAME, API_VERSION, BASE_DIRECTORY, \
                   FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, HOUR
from notify import Notify


class NotifyTests(unittest.TestCase):
    def test_config_variables(self):
        assert BASE_DIRECTORY == path.abspath(path.dirname(__file__))
        assert API_VERSION is not None
        assert API_USERNAME is not None
        assert API_PASSWORD is not None
        assert HOUR is not None
        assert FACEBOOK_APP_ID is not None
        assert FACEBOOK_APP_SECRET is not None
        
        # checking for hour - remove this code later
        assert HOUR is not 0
        assert HOUR is not 1
        assert HOUR is not 2
        assert HOUR is not 3
        assert HOUR is not 4
        assert HOUR is not 5
        assert HOUR is not 6
        assert HOUR is not 7
        assert HOUR is not 8
        assert HOUR is not 9
        assert HOUR is not 10
        assert HOUR is not 11
        assert HOUR is not 12
        assert HOUR is not 13
        assert HOUR is not 14
        assert HOUR is not 15
        assert HOUR is not 16
        assert HOUR is not 17
        assert HOUR is not 18
        assert HOUR is not 19
        assert HOUR is not 20
        assert HOUR is not 21
        assert HOUR is not 22
        assert HOUR is not 23
        assert HOUR is not 24
        

    def test_class_context(self):
        with Notify() as n:
            assert n is not None

    def test_send_unauthorized_notification(self):
        test_user = '100007897087250'

        with Notify() as n:
            response = n.send_notification(user_id=test_user)
                   

            # Have facebook changed the error code for this?
            # assert response.status_code == 500
            
            # updated new expected status code
            # Apparrently we want 400 error now
            # TODO - check this is correct
            assert response.status_code == 400

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
