# Generated by Django 4.2.6 on 2024-04-29 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Freelance', 'Freelance'), ('Internship', 'Internship'), ('Temporary', 'Temporary')], default='Full-time ', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.DecimalField(decimal_places=0, max_digits=7, validators=[django.core.validators.MinValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='job',
            name='vacancy',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
