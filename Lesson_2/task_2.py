# Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
new_list =list(range(101))
for num in new_list:
    if num % 2 == 0:
        print(new_list[num], end = ',')

