# Generated by Django 2.1.4 on 2019-01-16 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='user',
        ),
    ]
