import os

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

API_VERSION = 'v0.3'
API_BASE_URI = 'https://thefadstudy.herokuapp.com/api/{0}/'.format(API_VERSION)
API_USERNAME = 'apiuser'
API_PASSWORD = 'letmeinbrah!'

FB_BASE_URI = 'https://graph.facebook.com/'
FB_APP_ID = '498777246878058'
FB_APP_SECRET = '02272a1ef565d2bbbec38c64e464094f'

HOUR = 14 # The hour of the day to send the notifcation
