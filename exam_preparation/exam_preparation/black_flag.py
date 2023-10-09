def calculate_plugin(day_number, plunder_day, target):
    total_plunder = 0
    is_target = False
    for day in range(1, day_number + 1):
        total_plunder += plunder_day
        if day % 3 == 0:
            total_plunder += plunder_day * 0.5
        if day % 5 == 0:
            total_plunder -= total_plunder * 0.3
    if total_plunder >= target:
        is_target = True
    return total_plunder, is_target



days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
result, goal_reached = calculate_plugin(days, daily_plunder, expected_plunder)
if goal_reached:
    print(f'Ahoy! {result:.2f} plunder gained.')
else:
    percentage = result / expected_plunder * 100
    print(f'Collected only {percentage:.2f}% of the plunder.')

