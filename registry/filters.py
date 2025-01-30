import django_filters
from django_filters import MultipleChoiceFilter
from .models import Orders

#
# class OrdersFilter(django_filters.FilterSet):
#     compound = MultipleChoiceFilter(
#         lookup_expr='icontains',
#         field_name='compound',
#         choices=[
#             ('Т-25.1 цмм 115/140/140', 'Т-25 цмм'),
#             ('Т-23.1 цмм 115/125/125', 'Т-23 цмм'),
#             ('Т', 'Все')
#         ]
#     )
#
#     class Meta:
#         model = Orders
#         fields = ['compound']