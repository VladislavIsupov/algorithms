__author__ = "Владислав Исупов"

## Задачи к уроку №5

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections.

import collections

# Массив предприятий
firms = []
# Средняя прибыль
ave_profit = 0
# Создадим карточку предприятия
Firm = collections.namedtuple('Firm', ['name', 'quarters', 'profit'])

# Цикл для ввода данных предприятий
n = int(input("\nВведите количество предприятий: "))
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


