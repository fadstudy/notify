from os import environ, path
from datetime import datetime, timedelta

BASE_DIRECTORY = path.abspath(path.dirname(__file__))

# These settings are for the API in our moody app
# Environment settings are set from the heroku/travis dashboard or from the .env file during testing
API_VERSION = environ.get('API_VERSION')
API_BASE_URI = 'https://thefadstudy.herokuapp.com/api/{0}/'.format(API_VERSION)
API_USERNAME = environ.get('API_USERNAME')
API_PASSWORD = environ.get('API_PASSWORD')

# These settings are for the Facebook API and can be found on the FAD Study Facebook Dashboard 
FACEBOOK_BASE_URI = 'https://graph.facebook.com/'
FACEBOOK_APP_ID = environ.get('FACEBOOK_APP_ID')
FACEBOOK_APP_SECRET = environ.get('FACEBOOK_APP_SECRET')

# The hour of the day to send the notifcation
HOUR = environ.get('NOTIFY_HOUR') 