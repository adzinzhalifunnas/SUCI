# Generated by Django 3.2.5 on 2021-10-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_donation_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='already_received',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]