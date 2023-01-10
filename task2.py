# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3,4, 5, 6]
my_list_second = []


def increase(listochek):
    listochek_second = []
    i = 0
    y = 1
    sum = 0
    while i < len(listochek) / 2:
        sum = listochek[i] * listochek[-y]
        listochek_second.append(sum)
        i += 1
        y += 1
    return listochek_second


print(f'{my_list} => {increase(my_list)}')
