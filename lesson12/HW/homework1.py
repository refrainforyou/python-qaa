import csv

# Вхідний і вихідний файли
input_file = "random.csv"
output_file = "random-no-duplicates.csv"

# Читання даних з CSV
with open(input_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Видалення дублікатів
unique_data_set = set()
unique_data = []

for row in data:
    row_tuple = tuple(row.items())  # Перетворюємо рядок на кортеж
    if row_tuple not in unique_data_set:  # Перевіряємо унікальність
        unique_data_set.add(row_tuple)  # Додаємо в множину
        unique_data.append(row)  # Додаємо в список

# Запис у новий CSV файл
with open(output_file, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()  # Запис заголовків
    writer.writerows(unique_data)  # Запис унікальних рядків

print(f"Очищені дані збережено в '{output_file}'")
