# Generated by Django 3.2.2 on 2021-05-06 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20210425_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='location',
        ),
    ]
