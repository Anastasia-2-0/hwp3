# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 5, 6]
my_list_second = []

def increase(catalog):
    catalog_second = []
    i = 0
    y = 1
    sum = 0
    while i < len(catalog)/ 2 :
        sum = catalog[i] * catalog[-y]
        catalog_second.append(sum) 
        i+=1
        y+=1
    return catalog_second

print(f'{my_list} => {increase(my_list)}')