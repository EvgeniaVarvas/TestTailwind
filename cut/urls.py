from django.urls import path
from .views import cut_list


urlpatterns = [
    path('', cut_list, name='cut_list'),
    # path('orders/', filtered_orders, name='filtered_orders'),
]