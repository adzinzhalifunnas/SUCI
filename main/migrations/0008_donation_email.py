# Generated by Django 3.2.5 on 2021-11-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='email',
            field=models.EmailField(default='salismazaya@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]