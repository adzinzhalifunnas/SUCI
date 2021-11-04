from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.urls import reverse
from django.utils.crypto import get_random_string
from suci.settings import CHANNEL_PUSHER_NAME, SECRET_KEY, PAYMENT_GATEWAY, TRIPAY_PRIVATE_KEY
from main.pusher import pusher_client
from main.models import Donation, Text
from main.forms import DonationForm
from main.tripay import generatePayment
import json, re, hmac, hashlib

@require_http_methods(['GET', 'POST'])
def index(request: WSGIRequest):
    title = 'SUCI'
    description = 'Software Untuk Charity Indonesia'

    data = Text.objects.filter(name = 'TITLE').first()
    if data:
        title = data.text
    
    data = Text.objects.filter(name = 'DESCRIPTION').first()
    if data:
        description = data.text


    context = {
        'title': title,
        'description': description
    }


    if request.method == 'GET':
        if request.GET.get('transaction_status') == 'pending' or request.GET.get('tripay_status') == 'UNPAID':
            context['info_msg'] = 'Pembayaran kamu belum selesai'

        elif request.GET.get('transaction_status') == 'settlement' or request.GET.get('tripay_status') == 'PAID':
            context['success_msg'] = 'Pembayaran telah berhasil!'

        return render(request, 'main/index.html', context)

    elif request.method == 'POST':
        form = DonationForm(request.POST)
        if not form.is_valid():
            context['error_msg'] = 'Terjadi kesalahan!'
            return render(request, 'main/index.html', context)
        
        total = int(re.sub(r'\D', '', form.cleaned_data['total']))

        if total < 5_000 or total > 1_000_000:
            context['error_msg'] = 'Minimal Rp. 5.000 maksimal Rp. 1.000.000'
            return render(request, 'main/index.html', context)

        uniq_name = get_random_string()
        context['channel'] = uniq_name

        donation = Donation(
            name = form.cleaned_data['name'],
            uniq_name = uniq_name,
            message = form.cleaned_data['message'],
            email = form.cleaned_data['email'],
            amount = total,
        )
        donation.save()

        if PAYMENT_GATEWAY == 'tripay':
            url = generatePayment(request, donation)['data']['checkout_url']
            return redirect(url)


def notification(request: WSGIRequest):
    if request.GET.get('secret_key') != SECRET_KEY:
        return HttpResponseForbidden('Forbidden')
    
    return render(request, 'main/donation.html')


def rank(request: WSGIRequest):
    if request.GET.get('secret_key') != SECRET_KEY:
        return HttpResponseForbidden('Forbidden')

    rank_title = 'Para Sultan'
    data = Text.objects.filter(name = 'RANK_TITLE')
    if data:
        rank_title = data.text
    
    context = {
        'rank_title': rank_title,
    }
    return render(request, 'main/rank.html', context)


def milestone(request: WSGIRequest):
    if request.GET.get('secret_key') != SECRET_KEY:
        return HttpResponseForbidden('Forbidden')
    
    milestone_title = 'Untuk ke jalan yang benar'

    data = Text.objects.filter(name = 'MILESTONE_TEXT').first()
    if data:
        milestone_title = data.text

    context = {
        'milestone_title': milestone_title
    }

    return render(request, 'main/milestone.html', context)


def faq(request: WSGIRequest):
    return render(request, 'main/faq.html')


@csrf_exempt
@require_POST
def webhook(request: WSGIRequest):
    if PAYMENT_GATEWAY == 'tripay':
        calcSignature = request.headers.get('X-Callback-Signature', '')
        signature = hmac.new(bytes(TRIPAY_PRIVATE_KEY, 'latin-1'), bytes(request.body.decode(), 'latin-1'), hashlib.sha256).hexdigest()
        data = json.loads(request.body.decode())

        if calcSignature != signature:
            return HttpResponseForbidden('Bad Signature')

        if data['status'] != 'PAID':
            return HttpResponse(json.dumps({'status':'ok'}))

        donation: Donation = Donation.objects.get(id = data['merchant_ref'])
        donation.already_received = True
        donation.save()

        pusher_client.trigger(CHANNEL_PUSHER_NAME, 'donation', {
            'name': donation.name,
            'amount': donation.amount,
            'message': donation.message,
        })

        return HttpResponse(json.dumps({'status':'ok'}))
