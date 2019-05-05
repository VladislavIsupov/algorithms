__author__ = "Владислав Исупов"

## Задачи к уроку №6

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.
####################################################################################################################

# Сделаем анализ задачи к уроку №5. Для этого будем использвать модуль asizeof и profile

from pympler import asizeof

import collections

@profile
def my_func():
    # Переменная куда будем сохранять сколько выделено памяти для переменных
    result = ''
    # Массив предприятий
    firms = []
    result+=f'\nРазмер пустой firms - {asizeof.asizeof(firms)}'

    # Средняя прибыль
    ave_profit = 0
    result+=f'\nРазмер ave_profit - {asizeof.asizeof(ave_profit)}'

    # Создадим карточку предприятия
    Firm = collections.namedtuple('Firm', ['name', 'quarters', 'profit'])

    # Цикл для ввода данных предприятий
    n = int(input("\nВведите количество предприятий: "))
    result+=f'\nРазмер n - {asizeof.asizeof(n)}'

    for i in range(n):
        name = input(f"\nВведите название предприятия №{i+1}: ")
        quarters = []
        profit = 0
        for j in ["первый", "второй", "третий", "четвертый"]:
            x = int(input(f"\tВведите прибыль за {j} квартал: "))
            quarters.append(x)
            profit+=x
        firms.append(Firm(name, quarters, profit))
        ave_profit+=profit/n

    result += f'\nРазмер i - {asizeof.asizeof(i)}'
    result += f'\nРазмер name - {asizeof.asizeof(name)}'
    result += f'\nРазмер ave_profit - {asizeof.asizeof(ave_profit)}'
    result += f'\nРазмер firms - {asizeof.asizeof(firms)}'

    #print(firms)

    # Вывод результата

    print(f"\nСредняя прибыль: {ave_profit:.2f}")

    print("\nПредприятия с прибылью выше среднего:")
    for firm in firms:
        if firm.profit > ave_profit:
            print(f"\tПредприятие {firm.name} заработало {firm.profit}")

    print("\nПредприятия с прибылью ниже среднего:")
    for firm in firms:
        if firm.profit <= ave_profit:
            print(f"\tПредприятие {firm.name} заработало {firm.profit}")

    print(result)

if __name__ == '__main__':
    my_func()

# Данные ОС и python
# vlad@M50Vn:~$ inxi -S
# System:
#   Host: M50Vn Kernel: 4.15.0-20-generic x86_64 bits: 64 Desktop: Cinnamon 4.0.8
#   Distro: Linux Mint 19.1 Tessa
# Python 3.6.7 (default, Oct 22 2018, 11:32:17)
# [GCC 8.2.0] on linux

# Для трех предприятий получились такие размеры переменных:
# Размер пустой firms - 64
# Размер n - 32
# Размер i - 32
# Размер name - 56
# Размер ave_profit - 24
# Размер firms - 1248
# Размеры переменых позволяют предположить, что для работы программы потребовалось чуть более 1 кбайт памяти
# (если не учитывать память, занятую самим python)


# Данные профайлера:

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     18   26.914 MiB   26.914 MiB   @profile
#     19                             def my_func():
#     20                                 # Переменная куда будем сохранять сколько выделено памяти для переменных
#     21   26.914 MiB    0.000 MiB       result = ''
#     22                                 # Массив предприятий
#     23   26.914 MiB    0.000 MiB       firms = []
#     24   26.914 MiB    0.000 MiB       result+=f'\nРазмер пустой firms - {asizeof.asizeof(firms)}'
#     25
#     26                                 # Средняя прибыль
#     27   26.914 MiB    0.000 MiB       ave_profit = 0
#     28   26.914 MiB    0.000 MiB       result+=f'\nРазмер ave_profit - {asizeof.asizeof(ave_profit)}'
#     29
#     30                                 # Создадим карточку предприятия
#     31   26.914 MiB    0.000 MiB       Firm = collections.namedtuple('Firm', ['name', 'quarters', 'profit'])
#     32
#     33                                 # Цикл для ввода данных предприятий
#     34   26.914 MiB    0.000 MiB       n = int(input("\nВведите количество предприятий: "))
#     35   26.914 MiB    0.000 MiB       result+=f'\nРазмер n - {asizeof.asizeof(n)}'
#     36
#     37   26.914 MiB    0.000 MiB       for i in range(n):
#     38   26.914 MiB    0.000 MiB           name = input(f"\nВведите название предприятия №{i+1}: ")
#     39   26.914 MiB    0.000 MiB           quarters = []
#     40   26.914 MiB    0.000 MiB           profit = 0
#     41   26.914 MiB    0.000 MiB           for j in ["первый", "второй", "третий", "четвертый"]:
#     42   26.914 MiB    0.000 MiB               x = int(input(f"\tВведите прибыль за {j} квартал: "))
#     43   26.914 MiB    0.000 MiB               quarters.append(x)
#     44   26.914 MiB    0.000 MiB               profit+=x
#     45   26.914 MiB    0.000 MiB           firms.append(Firm(name, quarters, profit))
#     46   26.914 MiB    0.000 MiB           ave_profit+=profit/n
#     47
#     48   26.914 MiB    0.000 MiB       result += f'\nРазмер i - {asizeof.asizeof(i)}'
#     49   26.914 MiB    0.000 MiB       result += f'\nРазмер name - {asizeof.asizeof(name)}'
#     50   26.914 MiB    0.000 MiB       result += f'\nРазмер ave_profit - {asizeof.asizeof(ave_profit)}'
#     51   26.914 MiB    0.000 MiB       result += f'\nРазмер firms - {asizeof.asizeof(firms)}'
#     52
#     53                                 #print(firms)
#     54
#     55                                 # Вывод результата
#     56
#     57   26.914 MiB    0.000 MiB       print(f"\nСредняя прибыль: {ave_profit:.2f}")
#     58
#     59   26.914 MiB    0.000 MiB       print("\nПредприятия с прибылью выше среднего:")
#     60   26.914 MiB    0.000 MiB       for firm in firms:
#     61   26.914 MiB    0.000 MiB           if firm.profit > ave_profit:
#     62   26.914 MiB    0.000 MiB               print(f"\tПредприятие {firm.name} заработало {firm.profit}")
#     63
#     64   26.914 MiB    0.000 MiB       print("\nПредприятия с прибылью ниже среднего:")
#     65   26.914 MiB    0.000 MiB       for firm in firms:
#     66   26.914 MiB    0.000 MiB           if firm.profit <= ave_profit:
#     67   26.914 MiB    0.000 MiB               print(f"\tПредприятие {firm.name} заработало {firm.profit}")
#     68
#     69   26.914 MiB    0.000 MiB       print(result)

# Профайлер показал, что задача очень простая, интерпретатор python использует гораздо больше памяти чем наша программа.