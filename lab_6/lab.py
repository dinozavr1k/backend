def calculate_total_score(filename):
    
    # Оцінки для кожного варіанту
    points = {'X': 1, 'Y': 2, 'Z': 3}
    total_score = 0

    # Визначення результатів для кожної комбінації вибору
    result_map = {
        ('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3,  # Нічия
        ('A', 'Y'): 6, ('B', 'Z'): 6, ('C', 'X'): 6,  # Перемога
        ('A', 'Z'): 0, ('B', 'X'): 0, ('C', 'Y'): 0,  # Поразка
    }

    with open(filename, 'r') as file:
        for line in file:
            opponent_choice, my_choice = line.split()  # Розділяємо вибір суперника і свій вибір
            
            # Рахуємо очки за результат раунду
            round_score = result_map.get((opponent_choice, my_choice), 0)
            
            # Додаємо очки за вибір
            total_score += round_score + points[my_choice]

    return total_score

# Виклик функції і виведення результату
total_score = calculate_total_score("lab_6/input_6.txt")
print("Підсумковий рахунок за всі раунди:", total_score)

#8933