from suci.settings import MIDTRANS_CLIENT_KEY, MIDTRANS_SERVER_KEY, SANDBOX
import midtransclient

core_api = midtransclient.CoreApi(
    is_production = not SANDBOX,
    server_key = MIDTRANS_SERVER_KEY,
    client_key = MIDTRANS_CLIENT_KEY
)

snap = midtransclient.Snap(
    is_production = not SANDBOX,
    server_key = MIDTRANS_SERVER_KEY,
    client_key = MIDTRANS_CLIENT_KEY
)