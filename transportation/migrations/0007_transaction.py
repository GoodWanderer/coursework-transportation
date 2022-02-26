# Generated by Django 3.2.2 on 2022-02-25 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportation', '0006_alter_priceforqdate_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=40, verbose_name='Номер заказа')),
                ('from_country', models.CharField(max_length=100, verbose_name='Страна отправителя')),
                ('from_city', models.CharField(max_length=200, verbose_name='Город отправителя')),
                ('from_zip', models.CharField(max_length=20, verbose_name='Индикс отправителя')),
                ('from_address', models.CharField(max_length=300, verbose_name='Адрес отправителя')),
                ('from_name', models.CharField(max_length=200, verbose_name='ФИО отправителя')),
                ('from_phone', models.CharField(max_length=20, verbose_name='Телефон отправителя')),
                ('to_country', models.CharField(max_length=100, verbose_name='Страна получателя')),
                ('to_city', models.CharField(max_length=200, verbose_name='Город получателя')),
                ('to_zip', models.CharField(max_length=20, verbose_name='Индикс получателя')),
                ('to_address', models.CharField(max_length=300, verbose_name='Адрес получателя')),
                ('to_name', models.CharField(max_length=200, verbose_name='ФИО получателя')),
                ('to_phone', models.CharField(max_length=20, verbose_name='Телефон получателя')),
                ('weight', models.IntegerField(verbose_name='Вес (кг)')),
                ('volume', models.IntegerField(verbose_name='Объём (см^3)')),
                ('price', models.IntegerField(verbose_name='Общая стоимость')),
                ('paid', models.BooleanField(default=True, verbose_name='Статус оплаты')),
                ('status', models.CharField(choices=[('1', 'В обработке'), ('2', 'Комплектуется'), ('3', 'На складе'), ('4', 'В пути'), ('5', 'На разгрузке'), ('6', 'Ожидает')], default='1', max_length=40, verbose_name='Статус доставки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactionUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
