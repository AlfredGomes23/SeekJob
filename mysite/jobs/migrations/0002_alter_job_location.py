# Generated by Django 4.2.6 on 2024-04-28 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
