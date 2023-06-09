# Generated by Django 4.2.1 on 2023-05-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=100, verbose_name='word')),
                ('word_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='word')),
                ('word_uz', models.CharField(blank=True, max_length=100, null=True, verbose_name='word')),
                ('word_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='word')),
                ('definition', models.TextField(blank=True, verbose_name='definition')),
                ('definition_en', models.TextField(blank=True, null=True, verbose_name='definition')),
                ('definition_uz', models.TextField(blank=True, null=True, verbose_name='definition')),
                ('definition_ru', models.TextField(blank=True, null=True, verbose_name='definition')),
                ('language', models.CharField(blank=True, default='en', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Modeltranslation_words',
                'db_table': 'Modeltranslation',
            },
        ),
    ]
