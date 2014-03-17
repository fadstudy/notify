import os

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

API_VERSION = 'v0.3'
API_BASE_URI = 'https://thefadstudy.herokuapp.com/api/{0}/'.format(API_VERSION)
API_USERNAME = os.environ.get('API_USERNAME')
API_PASSWORD = os.environ.get('API_PASSWORD')

FB_BASE_URI = 'https://graph.facebook.com/'
FB_APP_ID = os.environ.get('FB_APP_ID')
FB_APP_SECRET = os.environ.get('FB_APP_SECRET')

HOUR = 14 # The hour of the day to send the notifcation
