from suci.settings import PUSHER_APP_ID, PUSHER_CLUSTER, PUSHER_KEY, PUSHER_SECRET
import pusher

pusher_client = pusher.Pusher(
    app_id = PUSHER_APP_ID,
    key = PUSHER_KEY,
    secret = PUSHER_SECRET,
    cluster = PUSHER_CLUSTER,
    ssl = True,
)