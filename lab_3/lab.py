def calculate_sum(text_lines):

    total_sum = 0  # Зберігаємо загальну суму
    for line in text_lines:
        # Знайдемо всі цифри в рядку
        digits = [char for char in line if char.isdigit()]
        if digits:
            # Вибираємо першу і останню цифри
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value  # Додаємо до загальної суми
    return total_sum

# Читання файлу та передача його в функцію
with open('lab_3/input_3.txt', 'r') as file:
    input_lines = file.readlines()


print(calculate_sum(input_lines))
