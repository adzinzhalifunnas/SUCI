from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from main.models import Donation
from suci.settings import TRIPAY_MERCHANT_CODE, TRIPAY_API_KEY, TRIPAY_PRIVATE_KEY, SANDBOX
import requests as r, hmac, hashlib

ses = r.Session()
ses.headers.update({'Authorization': 'Bearer ' + str(TRIPAY_API_KEY)})

def generateSignature(donation: Donation):
    signStr = "{}{}{}".format(TRIPAY_MERCHANT_CODE, donation.id, donation.amount)
    signature = hmac.new(bytes(TRIPAY_PRIVATE_KEY, 'latin-1'), bytes(signStr, 'latin-1'), hashlib.sha256).hexdigest()
    return signature


def generatePayment(request: WSGIRequest, donation: Donation):
    signature = generateSignature(donation)
    url = 'https://tripay.co.id/api-sandbox/transaction/create' if SANDBOX else 'https://tripay.co.id/api/transaction/create'
    payload = {
        'method': 'QRIS',
        'merchant_ref': donation.id,
        'amount': donation.amount,
        'customer_name': donation.name,
        'customer_email': donation.email,
        'order_items': [{
            'sku': 'donation',
            'name': 'Donation ' + str(donation.amount),
            'quantity': 1,
            'price': donation.amount,
        }],
        'callback_url': request.scheme + '://' + request.get_host() + reverse('webhook'),
        'return_url': request.scheme + '://' + request.get_host() + reverse('index'),
        'signature': signature,
    }
    data = ses.post(url, json = payload).json()
    return data
