# -*- coding: utf8 -*-

from datetime import datetime, timedelta
import os
import unittest

from requests import get

import config
from notify import Notify

class NotifyTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_class_init(self):
        assert Notify().last_date.day == (datetime.utcnow() - timedelta(days=1)).day

    def test_get_users(self):
        assert Notify().get_users() == True

    def test_send_notification(self):
        assert Notify().send_notification() == True

    def test_config_variables(self):
        pass

    def test_unauthorized_access(self):
        pass

    def test_authorized_access(self):
        pass


def main():
    unittest.main()

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
