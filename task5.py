# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonnachi(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    return Fibonnachi(i-1) + Fibonnachi(i-2)


n = int(input(
    "Введите число:\n"))
lst = [Fibonnachi(i) for i in range(1, n+2)]

print(lst)
lst = lst[::-1] + lst[1:]
print(lst, '\n')
