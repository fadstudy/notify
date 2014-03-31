from os import environ, path

BASE_DIRECTORY = path.abspath(path.dirname(__file__))

API_VERSION = environ.get('API_VERSION')
API_BASE_URI = 'https://thefadstudy.herokuapp.com/api/{0}/'.format(API_VERSION)
API_USERNAME = environ.get('API_USERNAME')
API_PASSWORD = environ.get('API_PASSWORD')

FB_BASE_URI = 'https://graph.facebook.com/'
FB_APP_ID = environ.get('FB_APP_ID')
FB_APP_SECRET = environ.get('FB_APP_SECRET')

HOUR = environ.get('NOTIFY_HOUR') # The hour of the day to send the notifcation
