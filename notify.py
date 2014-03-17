
from datetime import datetime, timedelta
from requests import get, post

import config

class Notify:
    '''
    Get all users in the study.

    Uses environment username and password, but these can be overwritten.

    Returns a Response object.
    http://docs.python-requests.org/en/latest/user/quickstart/#response-content
    '''
    def get_users(self, username=config.API_USERNAME,
                  password=config.API_PASSWORD):
        return get(config.API_BASE_URI + 'users', auth=(username, password))

    '''
    Post a notifcation to the facebook user based on the user_id.

    This method specifies a default message, but the message can be
    overwritten.

    Returns a Response object.
    http://docs.python-requests.org/en/latest/user/quickstart/#response-content
    '''
    def send_notification(self, user_id,
                          message='Hey, time to rate your mood for today!'):
        payload = { 'access_token' : '{0}|{1}'.format(config.FB_APP_ID,
                                                      config.FB_APP_SECRET),
                    'href' : '',
                    'template' : message }

        return post(config.FB_BASE_URI + user_id + '/notifications/',
                    params=payload)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass
