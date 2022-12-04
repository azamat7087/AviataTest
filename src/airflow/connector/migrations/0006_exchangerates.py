# Generated by Django 4.1.3 on 2022-12-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0005_alter_providersdata_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rates', models.JSONField()),
            ],
            options={
                'verbose_name': 'Курс валют',
                'verbose_name_plural': 'Курс валют',
                'ordering': ['-created_at'],
            },
        ),
    ]