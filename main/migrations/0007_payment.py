# Generated by Django 3.2.5 on 2021-11-04 13:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_donation_uniq_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expired', models.DateTimeField()),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.donation')),
            ],
        ),
    ]
