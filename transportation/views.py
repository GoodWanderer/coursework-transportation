# class contacts_view(viewsets.ModelViewSet):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializer
    # permission_classes = [permissions.IsAuthenticated]
  #  return Response({"message": "Hello, world!"})
    # object =  pattern.get(api_name, None)
    # if object == None:
    # return Response(
    #   data = "Invalid URL",
    #   status = status.HTTP_404_NOT_FOUND,
    #     )
    # if request.method == "GET":
        # object_list = Contacts.objects.all()
        # serializers  = ContactsSerializer.serializers(object_list, many=True)
        # return Response(serializers.data)

    # if request.method == "POST":
    #     data = request.data
    #     serializers = object.serializers(data=data)
        
    #     if not serializers.is_valid():
    #         return Response(
    #             data   = serializers.error,
    #             status = status.HTTP_404_NOT_FOUND
    #         )
    #     serializers.save()
    #     return Response(
    #             data   = serializers.error,
    #             status = status.HTTP_201_CREATED
    #     )


from django.core.paginator import Paginator

from .models import Contacts, ContactsMe
from .serializers import ContactsSerializer, ContactsMeSerializer

from .models import PriceForWay
from .serializers import PriceForWaySerializer
from .models import PriceForWeight
from .serializers import PriceForWeightSerializer
from .models import PriceForVolume
from .serializers import PriceForVolumeSerializer
from .models import CountryForQDate
from .serializers import CountryForQDateSerializer

from .models import Transaction, TransactionStatus
from .serializers import TransactionSerializer, TransactionStatusSerializer

from .models import Blog, BlogLike
from .serializers import BlogSerializer
from accounts.models import UserAccount 

from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response



@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def contacts_view(request):
  object_list = Contacts.objects.all()
  serializers  = ContactsSerializer(object_list, many=True)
  return Response(serializers.data)


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def contacts_me_view(request):
  if request.method == "POST":
      data = request.data
      serializers = ContactsMeSerializer(data=data)
      
      if not serializers.is_valid():
        return Response({"status": "bad_data"})

      serializers.save()
      return Response({"status": "success"})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def price_view(request):
  way_list = PriceForWay.objects.all()
  way = PriceForWaySerializer(way_list, many=True)

  weight_list = PriceForWeight.objects.all()
  weight = PriceForWeightSerializer(weight_list, many=True)

  volume_list = PriceForVolume.objects.all()
  volume = PriceForVolumeSerializer(volume_list, many=True)

  volume_list = PriceForVolume.objects.all()
  volume = PriceForVolumeSerializer(volume_list, many=True)

  qDate_list = CountryForQDate.objects.all()
  qDate = CountryForQDateSerializer(qDate_list, many=True)

  price = {
    'way': way.data,
    'weight': weight.data,
    'volume': volume.data,
    'qDate': qDate.data
  }
  
  return Response(price)



@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def get_price_transportation(request):
  if request.method == "POST":
    data = request.data

    try:      
      reqObj = data['data']
    except:
      return Response({"status": "bad_data"})    
      
    obj = {}

    wayData1 = PriceForWay.objects.filter(from_country=reqObj['fromCountry']).first()
    if wayData1 is not None:
      wayData2 = wayData1.forWayTo.filter(to_country=reqObj['toCountry']).first()
      if wayData2 is not None:
        obj['way'] = wayData2.price 
      else:
        return Response({"status": "server_get_error"}) 
    else:
      return Response({"status": "server_get_error"}) 


    maxVolume = PriceForVolume.objects.filter(type='MAX').first()
    if maxVolume is not None:
      if reqObj['volume'] < maxVolume.volume:
        volumeData1 = PriceForVolume.objects.all().order_by('volume')
        if volumeData1 is not None:
          volumeData2 = volumeData1.filter(volume__gte=reqObj['volume']).first()
          if volumeData2 is not None:
            obj['volume'] = volumeData2.price * reqObj['volume']
          else:
            return Response({"status": "server_get_error"}) 
        else:
          return Response({"status": "server_get_error"}) 
      else: 
        obj['volume'] = maxVolume.price * reqObj['volume']
    else:
      return Response({"status": "server_get_error"}) 



    maxWeight = PriceForWeight.objects.filter(type='MAX').first()
    if maxWeight is not None:
      if reqObj['weight'] < maxWeight.weight:
        weightData1 = PriceForWeight.objects.all().order_by('weight')
        if weightData1 is not None:
          weightData2 = weightData1.filter(weight__gte=reqObj['weight']).first()
          if weightData2 is not None:
            obj['weight'] = weightData2.price * reqObj['weight']
          else:
            return Response({"status": "server_get_error"}) 
        else:
          return Response({"status": "server_get_error"}) 
      else: 
        obj['weight'] = maxWeight.price * reqObj['weight']
    else:
      return Response({"status": "server_get_error"}) 


    print(obj)

    return Response({"status": "success", "price": obj['way']+obj['volume']+obj['weight']})



@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def get_price_storage(request):
  if request.method == "POST":
    data = request.data
    try:      
      reqObj = data['data']
    except:
      return Response({"status": "bad_data"})    
      
    obj = {}

    maxVolume = PriceForVolume.objects.filter(type='MAX').first()
    if maxVolume is not None:
      if reqObj['volume'] < maxVolume.volume:
        volumeData1 = PriceForVolume.objects.all().order_by('volume')
        if volumeData1 is not None:
          volumeData2 = volumeData1.filter(volume__gte=reqObj['volume']).first()
          if volumeData2 is not None:
            obj['volume'] = volumeData2.price * reqObj['volume']
          else:
            return Response({"status": "server_get_error"}) 
        else:
          return Response({"status": "server_get_error"}) 
      else: 
        obj['volume'] = maxVolume.price * reqObj['volume']
    else:
      return Response({"status": "server_get_error"}) 



    maxWeight = PriceForWeight.objects.filter(type='MAX').first()
    if maxWeight is not None:
      if reqObj['weight'] < maxWeight.weight:
        weightData1 = PriceForWeight.objects.all().order_by('weight')
        if weightData1 is not None:
          weightData2 = weightData1.filter(weight__gte=reqObj['weight']).first()
          if weightData2 is not None:
            obj['weight'] = weightData2.price * reqObj['weight']
          else:
            return Response({"status": "server_get_error"}) 
        else:
          return Response({"status": "server_get_error"}) 
      else: 
        obj['weight'] = maxWeight.price * reqObj['weight']
    else:
      return Response({"status": "server_get_error"}) 

    daysData = CountryForQDate.objects.all()
    for dayData in daysData:
      itemCountry = dayData.country.from_country
      if itemCountry == reqObj['fromCountry']:
        date1 = dayData.pForQDate.all().order_by('q_date')
        if date1 is not None:
          maxData = date1.all().last()
          if maxData is not None:
            date2 = maxData.q_date
            if date2 is not None and reqObj['day'] < date2:
              date3 = date1.filter(q_date__gte=reqObj['day']).first()
              if date3 is not None:
                obj['day'] = date3.q_date * date3.price
              else:
                return Response({"status": "server_get_error"}) 
            else :
              obj['day'] = reqObj['day'] * maxData.price
          else:
            return Response({"status": "server_get_error"})
        else:
          return Response({"status": "server_get_error"})

    try:
      return Response({"status": "success", "price": obj['weight']+obj['volume']+obj['day']})
    except:
      return Response({"status": "server_get_error"})


from .serializers import TransactionOrderSerializer

@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def order(request):
  if request.method == "POST":
    try:
      data = request.data
      serializers = TransactionOrderSerializer(data=data)

      if not serializers.is_valid():
        return Response({"status": "server_get_error"})

      serializers.save()

      transaction = Transaction.objects.get(id=serializers.data['id'])
      transactionStatus = TransactionStatus(t=transaction,  status_details=1)
      transactionStatus.save()

      return Response({"status": "success"})
    except:
      return Response({"status": "server_get_error"})

from django.conf import settings
from django.utils import dateformat


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def get_order_status(request, key):
  transaction = Transaction.objects.filter(key=key).first()
  if transaction is not None:
    statuses = transaction.status_detail.all().order_by('-status_details')
    if statuses is not None:
      arr = []
      for status in statuses:
        arr.append({
          'date': dateformat.format(status.date_status, settings.DATE_FORMAT),
          'status': status.typeOfSending_choise[int(status.status_details)-1][1]
        })
      return Response({"status": "success", "data": arr})

  return Response({"status": "bad_data"})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def get_countrys(request):
  countrys_list = PriceForWay.objects.all().values('from_country')
  # countrys = CountryForQDateSerializer(countrys_list, many=True)
  return Response({"status": "success", "data": countrys_list})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def get_order(request, id):
  data_list = Transaction.objects.filter(user=id).order_by('-id')
  transaction = TransactionSerializer(data_list, many=True)

  for item in transaction.data:
    for status in item['status_detail']:
      item['status'] = data_list[0].typeOfSending_choise[int(status['status_details'])-1][1]

  return Response({"status": "success", "data": transaction.data})



@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def get_blog(request, numPage, qItemsForPage):
  try:
    blog_list = Blog.objects.all().order_by('-date')

    pagin = Paginator(blog_list, qItemsForPage)
    pagin_lsit = pagin.page(numPage)

    blog = BlogSerializer(pagin_lsit, many=True)
    return Response({"status": "success", 'data': blog.data, 'qPages': pagin.num_pages})
  except:
    return Response({"status": "bad_data", 'data': [], 'qPages': 0})




@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def set_like(request):
  data = request.data
  try:
    item = Blog.objects.get(id=data['idB'])
    if data['like'] == True:
      item1 = item.blogUserLike.get(user=data['idU'])
      item1.delete()
    else:
      user = UserAccount.objects.get(id=data['idU'])
      BlogLike.objects.create(user=user, blog=item)
  except:
    return Response({"status": "bad_data"})
  return Response({"status": "success"})



@api_view()
@authentication_classes(())
@permission_classes(())
def get_blog_detail(request, id):
  try:
    blog_list = Blog.objects.get(id=id)
    blog = BlogSerializer(blog_list)
    return Response({"status": "success", 'data': blog.data})
  except:
    return Response({"status": "bad_data"})