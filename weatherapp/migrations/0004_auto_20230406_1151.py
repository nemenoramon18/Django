# Generated by Django 3.1 on 2023-04-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0003_auto_20230406_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('messages', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]
