# Generated by Django 3.0.8 on 2020-09-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]