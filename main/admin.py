from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib import messages
from suci.settings import CHANNEL_PUSHER_NAME
from main.models import Text, Donation
from main.pusher import pusher_client
from rangefilter.filters import DateRangeFilter
from django_object_actions import DjangoObjectActions

admin.site.site_header = 'SUCI Dashboard'
admin.site.site_title = 'SUCI'

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.action(description = 'Munculkan notifikasi')
def show_notification(modeladmin, request, queryset):
    for query in queryset[:10]:
        pusher_client.trigger(CHANNEL_PUSHER_NAME, 'donation', {
            'name': query.name,
            'amount': query.amount,
            'message': query.message,
        })
    messages.success(request, 'Sukses!')


@admin.action(description = 'Aktifkan')
def active(modealadmin, request, queryset):
    queryset.update(active = True)
    messages.success(request, 'Sukses!')


@admin.action(description = 'Nonaktifkan')
def nonactive(modealadmin, request, queryset):
    queryset.update(active = False)
    messages.success(request, 'Sukses!')



class TextAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'text',
    ]


class DonationAdmin(DjangoObjectActions, admin.ModelAdmin):
    def nonactive_all(modeladmin, request, queryset):
        Donation.objects.all().update(active = False)
        messages.success(request, 'Sukses!')

    def active_all(modeladmin, request, queryset):
        Donation.objects.all().update(active = True)
        messages.success(request, 'Sukses!')

    changelist_actions = [
        'active_all',
        'nonactive_all',
    ]
    search_fields = [
        'name',
        'message'
    ]
    list_filter = [
        ('time', DateRangeFilter),
        'already_received',
        'active',
    ]
    list_display = [
        'name',
        'amount',
        'message',
        'already_received',
        'active',
    ]
    actions = [
        show_notification,
        active,
        nonactive
    ]


admin.site.register(Text, TextAdmin)
admin.site.register(Donation, DonationAdmin)



