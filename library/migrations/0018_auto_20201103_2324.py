# Generated by Django 3.1.2 on 2020-11-03 17:54

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20201103_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='expirydate',
            field=models.DateField(verbose_name=library.models.get_expiry),
        ),
    ]