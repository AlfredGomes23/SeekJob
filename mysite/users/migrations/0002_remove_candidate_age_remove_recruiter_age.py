# Generated by Django 4.2.6 on 2024-04-26 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='age',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='age',
        ),
    ]
