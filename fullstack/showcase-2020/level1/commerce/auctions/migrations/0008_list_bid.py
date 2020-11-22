# Generated by Django 3.0.8 on 2020-09-18 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_list_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='bid',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.Bid'),
        ),
    ]
