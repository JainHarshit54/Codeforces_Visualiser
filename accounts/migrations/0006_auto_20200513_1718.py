# Generated by Django 2.2.5 on 2020-05-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200511_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='atcoder_handle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='codechef_handle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='codeforces_handle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='leetcode_handle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
