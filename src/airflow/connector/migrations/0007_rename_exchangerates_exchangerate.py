# Generated by Django 4.1.3 on 2022-12-04 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0006_exchangerates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExchangeRates',
            new_name='ExchangeRate',
        ),
    ]