# Generated by Django 3.2 on 2021-04-25 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('picture_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('picture_2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('picture_3', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('picture_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('picture_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
