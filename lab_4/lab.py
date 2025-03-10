def calculate_dir_sizes(file_path):
    dir_sizes = {}  # Словник для зберігання розмірів директорій
    current_path = []  # Поточний шлях

    with open(file_path) as file:
        for line in file:
            parts = line.split()

            # Обробка команд для переходу між директоріями
            if parts[0] == "$" and parts[1] == "cd":
                if parts[2] == "/":
                    current_path = ["/"]
                elif parts[2] == "..":
                    if current_path:
                        current_path.pop()
                else:
                    current_path.append(parts[2])

            # Якщо рядок містить розмір файлу
            elif parts[0].isdigit():
                size = int(parts[0])
                # Оновлюємо розмір для всіх батьківських директорій
                for i in range(len(current_path)):
                    path = "/".join(current_path[:i + 1])
                    dir_sizes[path] = dir_sizes.get(path, 0) + size

    # Підрахунок суми для директорій, де розмір <= 100000
    return sum(size for size in dir_sizes.values() if size <= 100000)

# Виклик функції та виведення результату
total = calculate_dir_sizes("lab_4/input_4.txt")
print("Сума:", total)

#1453349