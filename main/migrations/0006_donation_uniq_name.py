# Generated by Django 3.2.5 on 2021-11-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_donation_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='uniq_name',
            field=models.CharField(default='keren', max_length=20),
            preserve_default=False,
        ),
    ]
