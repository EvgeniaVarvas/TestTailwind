from registry import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='registry-list'),
]
