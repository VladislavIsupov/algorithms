__author__ = "Владислав Исупов"

## Задачи к уроку №8

#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import timeit

def Number_SubString_Set(S):
    SubString = set()
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            #print(S[i:j])
            SubString.add(hash(S[i:j]))
    return len(SubString)

def Number_SubString_Dict(S):
    SubString = {}
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            #print(S[i:j+1])
            SubString[hash(S[i:j])] = hash(S[i:j])
    return len(SubString.keys())


S = str(input("Введите строку маленькими латинскими буквами: "))
N = len(S)
print(f"Строка {S} длинной {N}")

print(f"{Number_SubString_Set(S)} - количество подстрок, используя множество")
print(f"{Number_SubString_Dict(S)} - количество подстрок, используя словарь")

print(timeit.timeit("Number_SubString_Set(S)",  setup="from __main__ import Number_SubString_Set,  S", number=100000))
print(timeit.timeit("Number_SubString_Dict(S)", setup="from __main__ import Number_SubString_Dict, S", number=100000))

'''
Строка qwererty длинной 8
33 - количество подстрок, используя множество
33 - количество подстрок, используя словарь
2.1103081490145996
2.757940908020828

Решение с использованием множества работает быстрее

'''
