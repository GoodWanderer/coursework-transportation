# Generated by Django 3.2.2 on 2022-02-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_auto_20220224_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceforwayto',
            name='price',
            field=models.IntegerField(default=100, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
