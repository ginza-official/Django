# Generated by Django 4.2.1 on 2023-05-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangosignals', '0009_alter_productshop_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='product_code',
            field=models.BigIntegerField(blank=True, default=7008677640, null=True, unique=True),
        ),
    ]
