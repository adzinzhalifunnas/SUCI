from django.core.handlers.wsgi import WSGIRequest
from main.models import Text
from suci.settings import PUSHER_APP_ID, PUSHER_CLUSTER, PUSHER_KEY, PUSHER_SECRET, CHANNEL_PUSHER_NAME, NOREK, OWNERNAME

def pusher(request: WSGIRequest):
    return {
        'PUSHER_APP_ID': PUSHER_APP_ID,
        'PUSHER_CLUSTER': PUSHER_CLUSTER,
        'PUSHER_KEY': PUSHER_KEY,
        'PUSHER_SECRET': PUSHER_SECRET,
        'CHANNEL_PUSHER_NAME': CHANNEL_PUSHER_NAME,
    }


def bank(request: WSGIRequest):
    return {
        'NOREK': NOREK,
        'OWNERNAME': OWNERNAME,
    }