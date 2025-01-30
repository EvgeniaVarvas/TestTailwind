def generate_combinations(workpiece_width, orders, selected_formats):
    combinations = []

    # Фильтруем заказы по выбранным форматам
    filtered_orders = [order for order in orders if order.format in selected_formats]

    # Одиночные ширины
    for order in filtered_orders:
        fmt = order.format
        waste = fmt - workpiece_width if fmt >= workpiece_width else float('inf')
        combinations.append({
            'widths': [workpiece_width],
            'format': fmt,
            'waste': waste,
            'orders': [order]
        })

    # Двойные ширины
    for i in range(len(filtered_orders)):
        for j in range(i, len(filtered_orders)):
            total_width = workpiece_width * 2
            if filtered_orders[i].format + filtered_orders[j].format >= total_width:
                waste = filtered_orders[i].format + filtered_orders[j].format - total_width
                combinations.append({
                    'widths': [workpiece_width, workpiece_width],
                    'format': f"{filtered_orders[i].format}+{filtered_orders[j].format}",
                    'waste': waste,
                    'orders': [filtered_orders[i], filtered_orders[j]]
                })

    # Тройные ширины
    for i in range(len(filtered_orders)):
        for j in range(i, len(filtered_orders)):
            for k in range(j, len(filtered_orders)):
                total_width = workpiece_width * 3
                if filtered_orders[i].format + filtered_orders[j].format + filtered_orders[k].format >= total_width:
                    waste = filtered_orders[i].format + filtered_orders[j].format + filtered_orders[k].format - total_width
                    combinations.append({
                        'widths': [workpiece_width, workpiece_width, workpiece_width],
                        'format': f"{filtered_orders[i].format}+{filtered_orders[j].format}+{filtered_orders[k].format}",
                        'waste': waste,
                        'orders': [filtered_orders[i], filtered_orders[j], filtered_orders[k]]
                    })

    return combinations