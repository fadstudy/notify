# -*- coding: utf8 -*-
from datetime import datetime, timedelta

from notify import Notify
import config

if __name__ == "__main__":
    # Set the last date to yesterday so the logic will work for today.
    last_date = datetime.utcnow() - timedelta(days=1)

    while True:
        today = datetime.utcnow() + timedelta(hours=11)

        # If it's the right time of the day...
        if today.day > last_date.day and today.hour == config.HOUR:
            last_date = today

            # Get all the users and send them a notifcation.
            with Notify() as n:
                [n.send_notification(user_id=user['facebook_id'])
                 for user in n.get_users().json()['users']]
