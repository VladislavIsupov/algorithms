__author__ = "Владислав Исупов"

## Задачи к уроку №7

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import timeit
from random import randint
import random

# Сортировка методом пузырька
def bubble(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# Гномья сортировка
def gnome(array):
    N = len(array)
    i = 1
    while i < N:
        if array[i-1] <= array[i]:
            i += 1
        else:
            array[i-1], array[i] = array[i], array[i-1]
            if i > 1:
                i -= 1
    return array

# Быстрая сортировка или сортировка Хоара
def quick(array):
    if len(array) <= 1:
        return array
    else:
        L = []
        R = []
        M = []
        rnd_elem = random.choice(array)

        for elem in array:
            if elem < rnd_elem:
                L.append(elem)
            elif elem > rnd_elem:
                R.append(elem)
            else:
                M.append(elem)

        return quick(L) + M + quick(R)

n = 10000  # размер массива
array_a = [randint(-10000, 10000) for i in range(n)]

print(array_a)
print(bubble(array_a.copy()))
print(gnome(array_a.copy()))
print(quick(array_a.copy()))

array_b = array_a.copy()
array_c = array_a.copy()
array_d = array_a.copy()

print(timeit.timeit("bubble(array_b)", setup="from __main__ import bubble, array_b", number=1))
print(timeit.timeit("gnome(array_c)", setup="from __main__ import gnome, array_c", number=1))
print(timeit.timeit("quick(array_d)", setup="from __main__ import quick, array_d", number=1))
print(timeit.timeit("array_a.sort()", setup="from __main__ import array_a", number=1))

'''
Время выполнение (сек.):

Массив 10000 элементов
Метод пузырка         - 14.36997213200084
Гномья сортировка     - 17.916162228008034
Быстрая сортировка    - 0.042156534997047856
Встроенная сортировка - 0.003948224999476224

Массив 10 элементов:
Метод пузырка         - 2.6258989237248898e-05
Гномья сортировка     - 2.213899279013276e-05
Быстрая сортировка    - 4.1065970435738564e-05
Встроенная сортировка - 5.937006790190935e-06

Сделал копии массивов, чтобы обеспечить равные условия для выполнения каждой функции. Копии были сделаны заранее,
чтобы время копирования не повлияло на результат.

Вывод: На больших массивах очевидно преимущество быстрой сортировки. Стандартная, встоення в python сортировка, 
выигрывает всегда.
На маленьких массивах быстрая сортировка проигрывает методу пузырька. Быстрее оказалась гномья сортировка.
Возможно, существует метод, который будет работать быстрее стандартного, на маленьких массивах, но, требуются 
дополнительные исследования. 
'''