# Generated by Django 4.2.3 on 2023-08-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0003_sale_customer_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]