# Generated by Django 4.2.1 on 2023-05-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_product_backtest4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='pricebasic',
        ),
        migrations.AddField(
            model_name='product',
            name='pricelifetime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pricepro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
