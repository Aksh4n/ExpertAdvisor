# Generated by Django 4.2.1 on 2023-05-22 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_product_inputs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
            ],
        ),
    ]
