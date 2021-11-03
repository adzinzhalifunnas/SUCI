from django.core.handlers.wsgi import WSGIRequest
from main.models import Text
from suci.settings import PUSHER_APP_ID, PUSHER_CLUSTER, PUSHER_KEY, PUSHER_SECRET, CHANNEL_PUSHER_NAME

def pusher(request: WSGIRequest):
    return {
        'PUSHER_APP_ID': PUSHER_APP_ID,
        'PUSHER_CLUSTER': PUSHER_CLUSTER,
        'PUSHER_KEY': PUSHER_KEY,
        'PUSHER_SECRET': PUSHER_SECRET,
        'CHANNEL_PUSHER_NAME': CHANNEL_PUSHER_NAME,
    }


def rank_text(request: WSGIRequest):
    RANK_TEXT = 'Para Sultan'
    data = Text.objects.filter(name = 'RANK_TEXT').first()
    if data:
        RANK_TEXT = data.text
    
    return {
        'RANK_TEXT': RANK_TEXT
    }