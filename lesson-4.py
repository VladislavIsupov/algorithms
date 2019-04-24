__author__ = "Владислав Исупов"

## Задачи к уроку №4

# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
# в рамках домашнего задания первых трех уроков.

import timeit

def overturn():
    chars = "76552432564875565353"
    result = ""
    for s in chars:
        result = s + result
    return result

def overturn2():
    chars = "76552432564875565353"
    result = chars[::-1]
    return result

def overturn3():
    chars = "76552432564875565353"
    result = ""
    for s in reversed(chars):
        result+=s
    return result

def overturn4():
    s = "76552432564875565353"
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

print(overturn())
print(overturn2())
print(overturn3())
print(overturn4())

print("1")
print(timeit.timeit("overturn()", setup="from __main__ import overturn", number=10000))
print(timeit.timeit("overturn()", setup="from __main__ import overturn", number=100000))
print(timeit.timeit("overturn()", setup="from __main__ import overturn", number=1000000))

print("2")
print(timeit.timeit("overturn2()", setup="from __main__ import overturn2", number=10000))
print(timeit.timeit("overturn2()", setup="from __main__ import overturn2", number=100000))
print(timeit.timeit("overturn2()", setup="from __main__ import overturn2", number=1000000))

print("3")
print(timeit.timeit("overturn3()", setup="from __main__ import overturn3", number=10000))
print(timeit.timeit("overturn3()", setup="from __main__ import overturn3", number=100000))
print(timeit.timeit("overturn3()", setup="from __main__ import overturn3", number=1000000))

print("4")
print(timeit.timeit("overturn4()", setup="from __main__ import overturn4", number=10000))
print(timeit.timeit("overturn4()", setup="from __main__ import overturn4", number=100000))
print(timeit.timeit("overturn4()", setup="from __main__ import overturn4", number=1000000))

# Результат
#
# 1
# 0.02408393799851183
# 0.29554303000622895
# 2.2787173700053245

# 2
# 0.002646908993483521
# 0.026156838997849263
# 0.2645166479924228

# 3
# 0.0272833460039692
# 0.2648481060023187
# 2.779104487010045

# 4
# 0.05704466000315733
# 0.5843008989904774
# 5.796441290003713

# Мы видим, что все алгоритмы имеют линейную сложность.
# Наиболее быстрый - второй алгоритм, с использованием срезов