# Generated by Django 3.0.8 on 2020-09-19 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200918_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='bid',
        ),
    ]
