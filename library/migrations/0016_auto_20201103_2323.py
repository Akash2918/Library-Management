# Generated by Django 3.1.2 on 2020-11-03 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_auto_20201103_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='expirydate',
            field=models.DateField(default=datetime.datetime(2020, 11, 18, 23, 23, 1, 777805)),
        ),
    ]
