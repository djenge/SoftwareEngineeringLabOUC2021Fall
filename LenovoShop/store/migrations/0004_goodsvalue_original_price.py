# Generated by Django 3.2.9 on 2021-12-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211222_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsvalue',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=4, default=5000, max_digits=20),
        ),
    ]
