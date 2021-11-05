from django.urls import path, re_path
from django.conf import urls
from main.views import index, milestone, notification, qrcode_, webhook, rank, faq, handler404

urlpatterns = [
    path('', index, name = 'index'),
    path('faq/', faq, name = 'faq'),
    path('donation/notif/', notification, name = 'notification'),
    path('donation/rank/', rank, name = 'rank'),
    path('donation/milestone/', milestone, name = 'milestone'),
    path('donation/qrcode/', qrcode_, name = 'milestone'),
    re_path(r'^webhook/?$', webhook, name = 'webhook'),
]

urls.handler404 = handler404