# Владислав Исупов

## Задачи к уроку №1

print("Задача №1")
n = input("Введите трехзначное число: ")
sum = 0
product = 1
for i in n:
    sum+=int(i)
    product*=int(i)
print(f"Количество знаков {i}, Сумма цифр числа: {sum}, Произведение {product}")

##################################################################################

print("Задача №2")
n1 = 5
n2 = 6

print(f"{n1} И   {n2} = {n1 and n2}")
print(f"{n1} ИЛИ {n2} = {n1 or n2}")
print(f"сдвиг влево на два знака числа  {n1} = {n1<<2}")
print(f"сдвиг вправо на два знака числа {n1} = {n1>>2}")

##################################################################################

print("Задача №5")
import string
letter1 = str(input("Введите первую букву: "))
letter2 = str(input("Введите вторую букву: "))

letter1 = letter1.upper()
letter2 = letter2.upper()

СodeLett1 = ord(letter1)
СodeLett2 = ord(letter2)

СodeLat_A = ord('A')
СodeRus_A = ord('А')


if (СodeLett1 >= СodeRus_A):
    print(f"Первая буква находится на {СodeLett1 - СodeRus_A + 1} месте")
else:
    print(f"Первая буква находится на {СodeLett1 - СodeLat_A + 1} месте")

if (СodeLett2 >= СodeRus_A):
    print(f"Вторая буква находится на {СodeLett2 - СodeRus_A + 1} месте")
else:
    print(f"Вторая буква находится на {СodeLett2 - СodeLat_A + 1} месте")

if (СodeLett1 == СodeLett2):
    print("Выбраны две одинаковых буквы")
else:
    print(f"Между буквами находится {abs(СodeLett1 - СodeLett2) - 1} букв")

##################################################################################

print("Задача №6")

NumberLetter = int(input("Введите номер буквы в русском алфавите: "))
СodeRus_A = ord('А')

if (NumberLetter > 32):
    print("Номер буквы должен быть меньше 33")
else:
    print(f"Буква {chr(NumberLetter + СodeRus_A - 1)} имеет номер {NumberLetter}")

##################################################################################

print("Задача №8")

Year = int(input("Введите год: "))
if (Year%4 > 0):
    print(f"Год {Year} не является високосным")
else:
    print(f"Год {Year} - високосный")

##################################################################################

print("Задача №9")

Num1 = int(input("Введите первое число: "))
Num2 = int(input("Введите второе число: "))
Num3 = int(input("Введите третье число: "))

maxNum = max(Num1, Num2, Num3)
minNum = min(Num1, Num2, Num3)

if (Num1 != maxNum and Num1 != minNum):
    print(f"Первое число является средним")
elif (Num2 != maxNum and Num2 != minNum):
    print(f"Второе число является средним")
elif (Num3 != maxNum and Num3 != minNum):
    print(f"Третье число является средним")
else:
    print("Не получилось определить среднее число")
