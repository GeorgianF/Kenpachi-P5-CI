# Generated by Django 3.2.15 on 2022-10-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='session_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
