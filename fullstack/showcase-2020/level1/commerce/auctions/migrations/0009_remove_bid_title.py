# Generated by Django 3.0.8 on 2020-09-18 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_list_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='title',
        ),
    ]
