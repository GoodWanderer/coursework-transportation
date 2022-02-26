from rest_framework import fields, serializers

from .models import Contacts, ContactsMe

from .models import PriceForWay, PriceForWayTo
from .models import CountryForQDate, PriceForQDate
from .models import PriceForWeight, PriceForVolume

from .models import Transaction

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


  
class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = '__all__'



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