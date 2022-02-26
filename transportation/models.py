from django.db import models
from accounts.models import UserAccount

import datetime 


class Contacts(models.Model):
  address = models.CharField(max_length=300, verbose_name='Адрес')
  phone = models.CharField(max_length=15, verbose_name='Телефон')
  email = models.EmailField(max_length=200, verbose_name='Почта')

  class Meta:
    verbose_name = 'Контактные данные'
    verbose_name_plural = 'Контактные данные'

  def __str__(self):
    return 'Контактные данные'


class ContactsMe(models.Model):
  name = models.CharField(max_length=200, verbose_name='Имя', blank=True, null=True)
  email = models.EmailField(max_length=200, verbose_name='Почта')
  notes = models.TextField(max_length=3000, verbose_name='Заметки', blank=True, null = True)

  class Meta:
    verbose_name = 'Запрос обратной связи'
    verbose_name_plural = 'Запросы обратной связи'

  def __str__(self):
    return 'Запрос обратной связи'

# * цены
class PriceForWay(models.Model):
  from_country = models.CharField(max_length=200, verbose_name='Страна отправления')

  class Meta:
    verbose_name = 'Цена от страны'
    verbose_name_plural = 'Цены от стран'

  def __str__(self):
    return self.from_country


class PriceForWayTo(models.Model):
  to_country = models.CharField(max_length=200, verbose_name='Страна получения')
  price = models.IntegerField('Цена')
  price_for_way = models.ForeignKey('priceForWay', on_delete=models.CASCADE, related_name='forWayTo')

  class Meta:
    verbose_name = 'Страна получения'
    verbose_name_plural = 'Страны получения'

  def __str__(self):
    return self.to_country


class CountryForQDate(models.Model):
  country = models.ForeignKey('priceForWay', on_delete=models.CASCADE, related_name="cForQDate")

  class Meta:
    verbose_name = 'Цена от дней хранения'
    verbose_name_plural = 'Цены от дней хранения'

  def __str__(self):
    return 'Цена от дней хранения'

class PriceForQDate(models.Model):
  country_for_q_date = models.ForeignKey('countryForQDate', on_delete=models.CASCADE, related_name="pForQDate")
  q_date = models.IntegerField(verbose_name="Кол-во дней хранения")
  price = models.IntegerField(verbose_name="Цена за день, при данном кол-ве дней")

  class Meta:
    verbose_name = 'Цена от дней хранения'
    verbose_name_plural = 'Цены от дней хранения'

  def __str__(self):
    return 'Цена от дней хранения'

class PriceForWeight(models.Model):
  typeOfSending_choise = (
      ("MIN", "Минимальный"),
      ("DEF", "Обычный"),
      ("MAX", "Максимальный"),
  )
  weight = models.IntegerField(verbose_name='Вес (кг)')
  price = models.IntegerField(verbose_name='Цена за кг, при данном весе')
  type = models.CharField(max_length=40, choices=typeOfSending_choise, default="DEF", verbose_name='Тип')

  class Meta:
    verbose_name = 'Цена от веса'
    verbose_name_plural = 'Цены от веса'

  def __str__(self):
    return '{} - {}'.format(self.weight, self.price)


class PriceForVolume(models.Model):
  typeOfSending_choise = (
      ("MIN", "Минимальный"),
      ("DEF", "Обычный"),
      ("MAX", "Максимальный"),
  )
  volume = models.IntegerField(verbose_name='Объём (см^3)')
  price = models.IntegerField(verbose_name='Цена за см^3, при данном весе')
  type = models.CharField(max_length=40, choices=typeOfSending_choise, default="DEF", verbose_name='Тип')

  class Meta:
    verbose_name = 'Цена от объёма'
    verbose_name_plural = 'Цены от объёма'

  def __str__(self):
    return '{} - {}'.format(self.volume, self.price)

# * Order

class Transaction(models.Model):
  typeOfSending_choise = (
      ("1", "В обработке"),
      ("2", "Комплектуется"),
      ("3", "На складе"),
      ("4", "В пути"),
      ("5", "На разгрузке"),
      ("6", "Ожидает"),
  )
  key = models.CharField(max_length=40, verbose_name="Номер заказа")
  user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="transactionUser")

  from_country = models.CharField(max_length=100, verbose_name="Страна отправителя")
  from_city = models.CharField(max_length=200, verbose_name="Город отправителя") 
  from_zip = models.CharField(max_length=20, verbose_name="Индикс отправителя") 
  from_address = models.CharField(max_length=300, verbose_name="Адрес отправителя") 
  from_name = models.CharField(max_length=200, verbose_name="ФИО отправителя") 
  from_phone = models.CharField(max_length=20, verbose_name="Телефон отправителя") 

  to_country = models.CharField(max_length=100, verbose_name="Страна получателя") 
  to_city = models.CharField(max_length=200, verbose_name="Город получателя")
  to_zip = models.CharField(max_length=20, verbose_name="Индикс получателя")
  to_address = models.CharField(max_length=300, verbose_name="Адрес получателя")
  to_name = models.CharField(max_length=200, verbose_name="ФИО получателя")
  to_phone = models.CharField(max_length=20, verbose_name="Телефон получателя")

  weight = models.IntegerField(verbose_name='Вес (кг)')
  volume = models.IntegerField(verbose_name='Объём (см^3)')
  price = models.IntegerField(verbose_name="Общая стоимость")
  paid = models.BooleanField(default=True, verbose_name="Оплачен?")
  status = models.CharField(max_length=40, choices=typeOfSending_choise, default="1", verbose_name='Статус доставки')

  class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'

  def __str__(self):
    return '{}'.format(self.key)

class TransactionStatus(models.Model):
  typeOfSending_choise = (
      ("1", "В обработке"),
      ("2", "Комплектуется"),
      ("3", "На складе"),
      ("4", "В пути"),
      ("5", "На разгрузке"),
      ("6", "Ожидает"),
  )
  date_status = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today, verbose_name='Дата')
  status_details = models.CharField(max_length=40, choices=typeOfSending_choise, verbose_name='Статус доставки')
  t = models.ForeignKey('transaction', on_delete=models.CASCADE, related_name="status_detail")

  class Meta:
    verbose_name = 'Детальный статус заказа'
    verbose_name_plural = 'Детальный статус заказа'

  def __str__(self):
    return 'Детальный статус заказа'



class Blog(models.Model):

  date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today, verbose_name='Дата')
  title = models.CharField(max_length=200, verbose_name='Заголовок')
  img = models.ImageField(upload_to='blog/', verbose_name='Изображение', blank=True, null = True)
  text = models.TextField(max_length=5000, verbose_name='Текст', blank=True, null = True)

  class Meta:
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'

  def __str__(self):
    return 'Статья'
  
class BlogLike(models.Model):

  user = models.ForeignKey(UserAccount, on_delete=models.PROTECT, related_name="like")
  blog = models.ForeignKey('blog', on_delete=models.PROTECT, related_name="blogUserLike")

  class Meta:
    verbose_name = 'Лайк'
    verbose_name_plural = 'Лайки'

  def __str__(self):
    return 'Лайк'