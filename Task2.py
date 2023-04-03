# Задача 32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input("Введите нижнюю границу диапазона: "))
max_number = int(input("Введите верхнюю границу диапазона: "))
array_final = []
for i in range(len(array)):
    if array[i] >= min_number and array[i] <= max_number:
        array_final.append(i)

print(f"Первоначальный массив: {array}")
print(f"Индексы значений массива в интервале между {min_number} и {max_number} = {array_final}")




# Эталонное решение: 
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
