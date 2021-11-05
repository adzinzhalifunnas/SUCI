from django.urls import path, re_path
from main.views import index, milestone, notification, qrcode_, webhook, rank, faq

urlpatterns = [
    path('', index, name = 'index'),
    path('faq/', faq, name = 'faq'),
    path('donation/notif/', notification, name = 'notification'),
    path('donation/rank/', rank, name = 'rank'),
    path('donation/milestone/', milestone, name = 'milestone'),
    path('donation/qrcode/', qrcode_, name = 'milestone'),
    re_path(r'^webhook/?$', webhook, name = 'webhook'),
]