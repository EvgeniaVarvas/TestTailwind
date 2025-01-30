from django.shortcuts import render
from django.db.models import F
from registry.models import Orders
from .forms import OrderFilterForm
from itertools import combinations as comb
from .utils import generate_combinations


def cut_list(request):
    orders = Orders.objects.filter(done__lt = F('quantity'))
    return render(request, 'cut/cut_list.html', {'orders': orders})

# def filtered_orders(request):
#     form = OrderFilterForm(request.GET or None)
#     optimal_plans = {}
#
#     if form.is_valid():
#         selected_compounds = form.cleaned_data['compounds']
#         selected_formats = list(map(int, form.cleaned_data['formats']))
#
#         for compound in selected_compounds:
#             # Получаем все заказы для данного состава
#             orders = Orders.objects.filter(compound=compound)
#
#             # Генерируем все возможные комбинации заказов
#             all_combinations = []
#             for r in range(1, len(orders) + 1):
#                 for combination in comb(orders, r):
#                     total_width = sum(order.workpiece_width for order in combination)
#                     min_waste = float('inf')
#                     best_format = None
#
#                     # Проверяем каждое выбранное формат
#                     for format_ in selected_formats:
#                         waste = format_ - total_width
#                         if 0 <= waste < min_waste:
#                             min_waste = waste
#                             best_format = format_
#
#                     if best_format is not None:
#                         all_combinations.append({
#                             'format': best_format,
#                             'waste': min_waste,
#                             'orders': combination
#                         })
#
#             # Находим оптимальную комбинацию для каждого заказа
#             optimal_combinations = []
#             for order in orders:
#                 min_waste = float('inf')
#                 best_combination = None
#                 for combination in all_combinations:
#                     if order in combination['orders'] and combination['waste'] < min_waste:
#                         min_waste = combination['waste']
#                         best_combination = combination
#                 if best_combination:
#                     optimal_combinations.append(best_combination)
#
#             optimal_plans[compound] = optimal_combinations
#
#     return render(request, 'cut/filtered-orders.html', {'form': form, 'optimal_plans': optimal_plans})