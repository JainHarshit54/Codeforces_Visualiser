# Generated by Django 2.2.5 on 2020-05-14 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200513_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]