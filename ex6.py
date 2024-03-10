def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_calories = 0
    total_cost = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            selected_items.append(item_name)
            total_calories += item_info['calories']
            total_cost += item_info['cost']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    num_items = len(item_names)
    
    dp = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(budget + 1):
            if items[item_names[i - 1]]['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[item_names[i - 1]]['cost']] + items[item_names[i - 1]]['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    optimal_calories = dp[num_items][budget]

    w = budget
    optimal_items = []
    for i in range(num_items, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            optimal_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']

    return optimal_items, optimal_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_items, greedy_calories = greedy_algorithm(items, budget)
dynamic_items, dynamic_calories = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Selected Items:", greedy_items)
print("Total Calories:", greedy_calories)

print("\nDynamic Programming:")
print("Selected Items:", dynamic_items)
print("Total Calories:", dynamic_calories)
