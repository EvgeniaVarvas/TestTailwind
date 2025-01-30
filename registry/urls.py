from django.urls import path
from .views import registry_list

urlpatterns = [
    path('', registry_list, name='registry-list'),

]
