# Generated by Django 4.2.1 on 2023-05-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
