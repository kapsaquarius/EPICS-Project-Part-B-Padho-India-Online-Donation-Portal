# Generated by Django 2.0.2 on 2020-06-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0007_auto_20200613_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
