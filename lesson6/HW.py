# Рахування унікальних символів в строці

_string = input('Enter the string: ')

unique_count = 0

for i in range(len(_string)):
    is_unique = True

    for j in range(len(_string)):
        if i != j and _string[i] == _string[j]:
            is_unique = False
            break

    if is_unique:
        unique_count += 1

print(f'Кількість унікальних символів: {unique_count}')

# Дочекайся літери
wait_letter = True
while wait_letter:
    a = input('Enter the word with "h": ')
    for i in a:
        if i == 'h':
            wait_letter = False

# Забери зі списку що потрібно
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [value for value in lst1 if isinstance(value, str)]
print(lst2)

# Сумуємо числа
list_of_numbers = [2, 3, 4, 12, 12, 3, 1]
summ = sum(i for i in list_of_numbers if i % 2 == 0)
print(summ)
