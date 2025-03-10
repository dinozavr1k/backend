list1 = []
list2 = []

# Читаємо файл
with open("lab_1/lists.txt", "r") as file:
    for line in file:
        numbers = line.split()
        if len(numbers) == 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

# Функція сортування вибором
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Сортуємо кожен масив окремо
sorted_list1 = selection_sort(list1)
sorted_list2 = selection_sort(list2)

# Виводимо результат для кожного рядка
print("Результати сортування рядків:")
for num1, num2 in zip(sorted_list1, sorted_list2):
    print(num1, num2)

# Обчислюємо суму всіх відстаней
distance_sum = sum(abs(num1 - num2) for num1, num2 in zip(sorted_list1, sorted_list2))

# Висновок: сума всіх відстаней
print("\nВисновок:", distance_sum)