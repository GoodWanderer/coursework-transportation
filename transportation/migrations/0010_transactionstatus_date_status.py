# Generated by Django 3.2.2 on 2022-02-25 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0009_auto_20220225_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionstatus',
            name='date_status',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
    ]