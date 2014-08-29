from datetime import datetime, timedelta
from requests import get, post

import config


class Notify:
    def get_users(self, username=config.API_USERNAME,
                  password=config.API_PASSWORD):
        """
        Get all users in the study.

        Uses environment username and password, but these can be overwritten.

        Returns a Response object.
        http://docs.python-requests.org/en/latest/user/quickstart/#response-content
        """
        return get(config.API_BASE_URI + 'users', auth=(username, password))


    def send_notification(self, user_id,
                          message='Hey, time to rate your mood for today!'):
        """
        Post a notification to the facebook user..

        This method specifies a default message, but the message can be
        overwritten.

        Returns a Response object.
        http://docs.python-requests.org/en/latest/user/quickstart/#response-content
        """

        payload = { 'access_token' : '{0}|{1}'.format(config.FACEBOOK_APP_ID,
                                                      config.FACEBOOK_APP_SECRET),
                    'href' : '',
                    'template' : message }

        return post(config.FACEBOOK_BASE_URI + user_id + '/notifications/',
                    params=payload)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass
