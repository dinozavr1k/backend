def calculate_total_valid_games(filename):

    # Обмеження по кольорах
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total_sum = 0

    with open(filename) as file:
        for line in file:
            game_id_str, rounds_str = line.split(": ")  # Розділяємо на ID гри та раунди
            game_id = int(game_id_str.split()[1])  # Витягуємо ID гри після "Game"
            rounds = [
                (int(num), color) 
                for round in rounds_str.split("; ")  # Розділяємо на раунди
                for pair in round.split(", ")  # Розділяємо пари в кожному раунді
                for num, color in [pair.split()]  # Розділяємо число та колір
            ]
            
            # Перевіряємо, чи кожен номер не перевищує відповідні обмеження по кольору
            if all(num <= limits[color] for num, color in rounds):
                total_sum += game_id  # Додаємо ID гри до загальної суми

    return total_sum

print(calculate_total_valid_games("lab_5/input_5.txt"))

#2810