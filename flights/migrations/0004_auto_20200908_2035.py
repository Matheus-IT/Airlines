# Generated by Django 3.1 on 2020-09-08 23:35

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('flights', '0003_passanger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passanger',
            new_name='Passenger',
        ),
    ]
