from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from main.models import Donation
import json

def rank_donation(request: WSGIRequest):
    rank_by_donation = {}
    donations = Donation.objects.filter(active = True).filter(already_received = True).all()[:5]
    for donation in donations:
        if rank_by_donation.get(donation.name):
            rank_by_donation[donation.name] += donation.amount
        else:
            rank_by_donation[donation.name] = 0
            rank_by_donation[donation.name] += donation.amount
    
    rank_by_donation = rank_by_donation.items()
    rank_by_donation = sorted(rank_by_donation, key = lambda x: x[1], reverse = True)
    for i in range(len(rank_by_donation)):
        rank_by_donation[i] = list(rank_by_donation[i])
    
    return HttpResponse(json.dumps(rank_by_donation))

def milestone(request: WSGIRequest):
    total = 0
    donations = Donation.objects.filter(active = True).filter(already_received = True).all()
    for donation in donations:
        total += donation.amount
    
    return HttpResponse(json.dumps(total))