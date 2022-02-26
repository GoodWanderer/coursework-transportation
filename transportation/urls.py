from django.urls import path

from .views import contacts_view, contacts_me_view
from .views import price_view
from .views import get_price_transportation, get_price_storage
from .views import order, get_order_status, get_order
from .views import get_blog, set_like, get_blog_detail


urlpatterns = [
    path('contacts/', contacts_view, name=None),
    path('contacts-me/', contacts_me_view, name=None),
    path('calc/transportation/price/', get_price_transportation, name=None),
    path('calc/storage/price/', get_price_storage, name=None),
    path('order/', order, name=None),
    path('status/order/get/<slug:key>', get_order_status, name=None),
    path('order/get/<slug:id>', get_order, name=None),
    path('blog/get/', get_blog, name=None),
    path('like/set/', set_like, name=None),
    path('blog/detail/<int:id>', get_blog_detail, name=None),
]

