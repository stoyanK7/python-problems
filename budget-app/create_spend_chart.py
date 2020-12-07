def create_spend_chart(categories):
    # Frequently used
    whitespace = " "
    dash = "-"

    # Bar chart string
    bar_chart = "Percentage spent by category\n"

    # Will be used later in the chart
    max_category_name_length = 0

    # Calculate total spendings and spendings for each category
    total_costs = 0
    total_spent_by_category = list()
    for category in categories:
        # Only withdrawals
        current_category_costs = list()
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                current_category_costs.append(-transaction["amount"])

        total_spent_by_category.append(sum(current_category_costs))
        total_costs += sum(current_category_costs)

        # Get the max category name length
        if len(category.name) > max_category_name_length:
            max_category_name_length = len(category.name)

    # Calculate percentages for each category
    percentage_per_category = list()
    for category in total_spent_by_category:
        percentage_per_category.append(round(category / total_costs, 2) * 100)
    
    # Chart
    percentages = 100
    while percentages >= 0:
        current_row = f"{str(percentages).rjust(3)}| "
        for category in percentage_per_category:
            if category >= percentages:
                current_row += f"o{whitespace * 2}"
            else:
                current_row += f"{whitespace * 3}"
        percentages -= 10
        bar_chart += f"{current_row}\n"

    # Horizontal line
    bar_chart += f"{whitespace * 4}{dash * (3 * len(categories) + 1)}\n"

    # Category names in vertical
    for i in range(max_category_name_length):
        bar_chart += f"{whitespace * 5}"
        for category in categories:
            try:
                bar_chart += f"{category.name[i]}{whitespace * 2}"
            except:
                bar_chart += f"{whitespace * 3}"
        bar_chart += "\n"


    # Return chart and remove last newline
    return bar_chart.rstrip("\n")
