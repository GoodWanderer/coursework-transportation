# Generated by Django 3.2.2 on 2022-02-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0013_auto_20220226_0232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloglike',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Текст'),
        ),
    ]