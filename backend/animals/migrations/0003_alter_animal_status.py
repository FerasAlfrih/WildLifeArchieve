# Generated by Django 3.2.6 on 2021-08-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20210828_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='status',
            field=models.CharField(choices=[('EX', 'Extinct'), ('EW', 'Extinct in the Wild'), ('CR', 'Critically Endangered'), ('EN', 'Endangered'), ('VU', 'Vulnerable'), ('NT', 'Near Threatened'), ('CD', 'Conservation Dependent'), ('LC', 'Least Concern'), ('DD', 'Data Deficient'), ('NE', 'Not Listed')], default='LC', max_length=255),
        ),
    ]
