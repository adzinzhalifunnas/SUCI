from django.urls import re_path
from api.views import milestone, rank_donation

urlpatterns = [
    re_path(r'^rank-donation/?$', rank_donation, name = 'rank-donation'),
    re_path(r'^milestone/?$', milestone, name = 'api-milestone'),
]