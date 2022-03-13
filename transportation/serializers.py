from rest_framework import fields, serializers

from .models import Contacts, ContactsMe
from .models import PriceForWay, PriceForWayTo
from .models import CountryForQDate, PriceForQDate
from .models import PriceForWeight, PriceForVolume
from .models import Transaction, TransactionStatus
from .models import Blog, BlogLike


class ContactsSerializer(serializers.ModelSerializer):
  class Meta:
      model = Contacts
      fields = '__all__'


class ContactsMeSerializer(serializers.ModelSerializer):
  class Meta:
      model = ContactsMe
      fields = ("name", "email", "notes")

  
# * Цена
class PriceForWayToSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceForWayTo
    fields = '__all__'

class PriceForWaySerializer(serializers.ModelSerializer):
  forWayTo = PriceForWayToSerializer(many=True)
  class Meta:
    model = PriceForWay
    fields = ("from_country", "forWayTo")


class PriceForWeightSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceForWeight
    fields = '__all__'

class PriceForVolumeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceForVolume
    fields = '__all__'


class PriceForQDateSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceForQDate
    fields = '__all__'

class CountryForQDateSerializer(serializers.ModelSerializer):
  pForQDate = PriceForQDateSerializer(many=True)
  country = PriceForWaySerializer()
  class Meta:
    model = CountryForQDate
    fields = ("id", "pForQDate", "country")


class TransactionStatusSerializer(serializers.ModelSerializer):
  date_status = serializers.DateField(format="%d-%m-%Y")
  class Meta:
    model = TransactionStatus
    fields = ('date_status', 'status_details')
  
class TransactionSerializer(serializers.ModelSerializer):
  status_detail = TransactionStatusSerializer(many=True)
  class Meta:
    model = Transaction
    fields = (
      'id', 'key', 'user', 
      'from_country', 'from_city', 'from_zip', 'from_address', 'from_name', 'from_phone', 
      'to_country', 'to_city', 'to_zip', 'to_address', 'to_name', 'to_phone', 
      'weight', 'volume', 'price', 'paid', 'status', 
      'status_detail'
    )


class TransactionOrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = (
      'id', 'key', 'user', 
      'from_country', 'from_city', 'from_zip', 'from_address', 'from_name', 'from_phone', 
      'to_country', 'to_city', 'to_zip', 'to_address', 'to_name', 'to_phone', 
      'weight', 'volume', 'price', 'paid', 'status', 
    )


class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceForWay
    fields = ("from_country")

class BlogLikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogLike
    fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
  blogUserLike = BlogLikeSerializer(many=True)
  date = serializers.DateField(format="%d-%m-%Y")
  class Meta:
    model = Blog
    fields = ("id", "title", "date", "text", "img", "blogUserLike")