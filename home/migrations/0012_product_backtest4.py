# Generated by Django 4.2.1 on 2023-05-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_product_backtest1_product_backtest2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='backtest4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
