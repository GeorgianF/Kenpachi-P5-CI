# Generated by Django 3.2.15 on 2022-09-24 21:20

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220924_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
