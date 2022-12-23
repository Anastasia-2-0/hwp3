# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list=[1.1, 1.2, 3.1, 5, 10.01]

def listFraction(listochek):
    i=0
    y=0
    value = 0
    empty_listochek = []
    for item in range(len(listochek)):     
        value=listochek[i]-int(listochek[i])
        if value != 0:
            empty_listochek.append(round(value,2))
            i+=1
            y+=1
        else:
            i+=1
            y+=1
    return empty_listochek


def maxNumber(listochek):
    i=0
    maxn = listochek[0]
    for iten in range(len(listochek)):
        if listochek[i] > maxn:
            maxn = listochek[i]
            i+=1
        else:
            i+=1
    return maxn

def minNumber(listochek):
    i=0
    minn=listochek[0]
    for iten in range(len(listochek)):
        if listochek[i] < minn:
            minn = listochek[i]
            i+=1
        else:
            i+=1
    return minn

print(f'{my_list} => {maxNumber(listFraction(my_list))-minNumber(listFraction(my_list))}')



        