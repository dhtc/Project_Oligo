# Generated by Django 2.0.7 on 2018-12-19 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20181206_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequenceinput',
            name='sequence_name',
            field=models.CharField(default=datetime.datetime(2018, 12, 19, 18, 52, 36, 570299), max_length=60),
        ),
    ]
