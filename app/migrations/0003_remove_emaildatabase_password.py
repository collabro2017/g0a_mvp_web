# Generated by Django 2.1.2 on 2018-11-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_emaildatabase_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emaildatabase',
            name='password',
        ),
    ]
