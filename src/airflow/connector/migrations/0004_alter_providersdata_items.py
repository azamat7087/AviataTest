# Generated by Django 4.1.3 on 2022-12-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0003_providersdata_status_alter_providersdata_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providersdata',
            name='items',
            field=models.JSONField(default=None, null=True),
        ),
    ]