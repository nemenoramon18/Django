# Generated by Django 3.1 on 2023-04-06 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0004_auto_20230406_1151'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='User',
        ),
    ]
