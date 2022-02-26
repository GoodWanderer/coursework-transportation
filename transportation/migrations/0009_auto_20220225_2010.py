# Generated by Django 3.2.2 on 2022-02-25 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0008_auto_20220225_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='status_details',
        ),
        migrations.CreateModel(
            name='TransactionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_details', models.CharField(choices=[('1', 'В обработке'), ('2', 'Комплектуется'), ('3', 'На складе'), ('4', 'В пути'), ('5', 'На разгрузке'), ('6', 'Ожидает')], default='1', max_length=40, verbose_name='Статус доставки')),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_detail', to='transportation.transaction')),
            ],
            options={
                'verbose_name': 'Детальный статус заказа',
                'verbose_name_plural': 'Детальный статус заказа',
            },
        ),
    ]
