from datetime import datetime, timedelta
from requests import get, post
import config

def notify():
    # Set the last date to yesterday so the logic will work for today.
    last_date = datetime.utcnow() - timedelta(days=1)

    while True:
        today = datetime.utcnow() + timedelta(hours=11)

        # if a particular time:
        if today.day > last_date.day and today.hour == config.HOUR:
            last_date = today

            r = get(config.API_BASE_URI + 'users')

            if r.status_code == 200:
               users = r.json()['users']
            else:
                continue

            for user in users:
                send_notification(user['facebook_id'])

'''
Send a notifcation to the user.

This method specifies a default message, but the message can be overriden.
'''
def send_notification(user_id, message='Hey, time to rate your mood for today!'):
    payload = {'access_token' : '{0}|{1}'.format(config.FB_APP_ID,
                                                 config.FB_APP_SECRET),
              'href' : '',
              'template' : message}

    post(config.FACEBOOK_BASE_URI + user_id + '/notifications/',
         params=payload).url


if __name__ == "__main__":
    notify()
