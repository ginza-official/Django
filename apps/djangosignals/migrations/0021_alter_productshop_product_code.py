# Generated by Django 4.2.1 on 2023-07-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangosignals', '0020_alter_productshop_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='product_code',
            field=models.BigIntegerField(blank=True, default=5340881125, null=True, unique=True),
        ),
    ]
