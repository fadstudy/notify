from datetime import datetime, timedelta
from os import path
from requests import post
import config

# TODO remove the file and hook it up to the API
def notify():
    # Set the last date to yesterday so the logic will work for today.
    last_date = datetime.utcnow() - timedelta(days=1)

    while True:
        # if a particular time:
        today = datetime.utcnow() + timedelta(hours=11)

        if today.day > last_date.day and today.hour == config.HOUR:
            print 'print true'
            last_date = today

            with open(path.join(config.BASE_DIRECTORY, 'users.txt'), 'rt') as \
                                                                          _file:
                for user in _file:
                    send_notification(user.strip())

'''
Send a notifcation to the user.

This method specifies a default message, but the message can be overriden.
'''
def send_notification(user_id, message='Hey, time to rate your mood for today!'):
    payload = {'access_token' : '{0}|{1}'.format(config.FB_APP_ID,
                                                 config.FB_APP_SECRET),
              'href' : '',
              'template' : message}

    print post(config.BASE_URI + user_id + '/notifications/', params=payload).url


if __name__ == "__main__":
    notify()
