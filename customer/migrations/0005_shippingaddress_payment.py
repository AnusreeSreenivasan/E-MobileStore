# Generated by Django 4.1.7 on 2023-03-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_product_digital_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='payment',
            field=models.CharField(choices=[('COD', 'COD'), ('Debit/Credit_Card', 'Debit/Credit_Card'), ('UPI', 'UPI')], default='COD', max_length=100),
        ),
    ]
