from django.contrib import admin

from .models import Contacts, ContactsMe
from .models import PriceForWay, PriceForWayTo
from .models import CountryForQDate, PriceForQDate
from .models import PriceForWeight, PriceForVolume

from .models import Transaction, TransactionStatus

from .models import Blog, BlogLike

admin.site.site_title = 'Доставка МТК'
admin.site.site_header = 'Доставка МТК'

@admin.register(Contacts)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email')

@admin.register(ContactsMe)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


# * Цена от страны
class PriceForWayToInline(admin.TabularInline): 
  fk_name = 'price_for_way'
  model = PriceForWayTo

@admin.register(PriceForWay)
class PriceForWayAdmin(admin.ModelAdmin):
  list_display = ('__str__',)
  inlines = [PriceForWayToInline,]

# * Цена от дней хранения
class PriceForQDateInline(admin.TabularInline):
  fk_name = 'country_for_q_date'
  model = PriceForQDate

@admin.register(CountryForQDate)
class CountryForQDateAdmin(admin.ModelAdmin):
  list_display = ('country',)
  inlines = [PriceForQDateInline,]

# * Цена от веса
@admin.register(PriceForWeight)
class PriceForWeightAdmin(admin.ModelAdmin):
  list_display = ('weight', 'price')

# * Цена от объёма
@admin.register(PriceForVolume)
class PriceForVolumeAdmin(admin.ModelAdmin):
  list_display = ('volume', 'price')

# * Заказы
class TransactionStatusInline(admin.TabularInline):
  fk_name = 't'
  model = TransactionStatus


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
  list_display = ('key', 'from_country', 'to_country')
  inlines = [TransactionStatusInline,]


# * Блог
class BlogInline(admin.TabularInline):
  fk_name = 'blog'
  model = BlogLike


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ('title', 'date')
  inlines = [BlogInline,]



