# Generated by Django 3.1.2 on 2020-11-03 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20201103_1858'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.AddField(
            model_name='issue',
            name='expirydate',
            field=models.DateField(default=datetime.datetime(2020, 11, 18, 20, 48, 9, 589110)),
        ),
    ]
