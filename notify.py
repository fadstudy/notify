from datetime import datetime, timedelta
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
            last_date = today

            with open('users.txt', 'rt') as _file:
                for user in _file:
                    send_notification(user)

'''
Send a notifcation to the user.

This method specifies a default message, but the message can be overriden.
'''
def send_notification(user_id, message='Hey, time to rate your mood for today!'):
    payload = {'access_token' : '{0}|{1}'.format(config.FB_APP_ID,
                                                 config.FB_APP_SECRET),
              'href' : '',
              'template' : message}

    post(config.BASE_URI + user_id + '/notifications', params=payload)


if __name__ == "__main__":
    notify()
