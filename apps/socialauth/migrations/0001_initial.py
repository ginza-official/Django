# Generated by Django 4.2.1 on 2023-05-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('provider', models.CharField(max_length=255)),
                ('uid', models.CharField(max_length=255)),
                ('extra_data', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Social Auth User',
                'verbose_name_plural': 'Social Auth Users',
                'db_table': 'social_auth_users',
            },
        ),
    ]
