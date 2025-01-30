from django.shortcuts import render
from .models import Orders



def registry_list(request):
    orders = Orders.objects.all()

    context = {
        'orders': orders,
     }
    return render(request, 'registry/registry-list.html', context)




